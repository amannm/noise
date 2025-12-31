A strong “BEATs-first” way to do this (and what I’d call the most practical state-of-the-art for a single apartment + two sources) is:
	1.	use a big pretrained BEATs encoder as a frozen (or lightly fine-tuned) feature extractor,
	2.	train a small temporal head for frame-level multi-label detection (AC present? fridge present?), then
	3.	wrap it in a hysteresis + state-machine that turns “presence probabilities” into discrete on/off events.

That gets you robustness (BEATs), temporal stability (the head), and clean events (the state machine).

⸻

1) Why BEATs is a good fit here

BEATs is pretrained for general audio semantics via discrete-label prediction and transfers very well to downstream audio classification tasks. The original setup uses 16 kHz audio and 128-dim log-mel filterbanks (25 ms window / 10 ms hop) as input features.  ￼

There are also scaled BEATs-style general-purpose audio encoders published more recently (bigger model + broader pretraining data) that are competitive with much larger encoders—if you can run them in real time on your M4 Max, start there.  ￼

⸻

2) Data reality check (and how to still make this work)

With only four 3-minute “steady state” recordings, you can train a decent presence classifier (“AC present?”, “fridge present?”), but you cannot directly learn transitions (on/off boundaries) very well because you have no examples containing the switch moments.

The SOTA-ish workaround is:
	•	Train presence detection from your existing clips (weak labels).
	•	Then create events by detecting stable changes in presence probability over time (hysteresis + minimum-duration constraints).

If you can add just a little more data later, the highest ROI is: record a few sessions where you turn AC on/off and capture a few fridge cycles, and annotate approximate times. That lets you train the temporal head as true sound-event detection (SED).

⸻

3) Model pipeline (BEATs embeddings → temporal SED head)

A. Preprocess like BEATs expects
	•	Resample 44.1 kHz → 16 kHz (high-quality bandlimited resampling).
	•	Compute 128-bin log-mel filterbanks with ~25 ms / 10 ms hop (matches BEATs’ recipe).  ￼
Practical note: people have observed embedding differences depending on how resampling is done; use a high-quality resampler consistently.  ￼

B. Extract time-resolved embeddings (don’t throw away token info)

For event-ish problems, you generally want frame/token-level outputs from BEATs (a sequence over time), not just one globally pooled vector. Recent probing work highlights that aggressive global pooling can bottleneck information for dispersed, localized events.  ￼

So: run BEATs on sliding windows (e.g., 2–4 s window, 0.5–1.0 s hop), keep the per-patch/per-frame representations, and feed that sequence to a head.

C. Temporal head (small, fast, works great on-device)

Use a lightweight head that outputs two probabilities per frame:
	•	p(fridge_present)
	•	p(ac_present)

Good heads that are “SOTA in practice” for small-data SED on top of SSL embeddings:
	•	1D temporal CNN + (Bi)GRU
	•	Temporal Conformer-lite (if you want a bit more capacity)
	•	Transformer encoder with attentive pooling over time tokens

Train it as multi-label (sigmoid outputs) so all_on.wav naturally teaches co-occurrence.

If you want to be extra modern: you can also fuse embeddings from multiple SSL encoders (BEATs + another) for SED, but since you asked “based on BEATs,” I’d start with BEATs-only and only add fusion if needed.  ￼

D. Fine-tuning strategy (most common winning recipe)

In order of “least data → most data”:
	1.	Linear probe: freeze BEATs, train just the head (fastest, often surprisingly strong).
	2.	Partial fine-tune: unfreeze last N BEATs blocks + head.
	3.	Parameter-efficient fine-tune: LoRA/adapters on BEATs + head (great when you don’t want full finetune).

Given your tiny dataset, start with (1), then (2) if it’s not robust.

⸻

4) Turning presence into on/off events (state machine)

Once you have stable p(ac_present) and p(fridge_present) streams, emit events with:
	•	Smoothing: EMA or median filter over ~3–10 seconds
	•	Hysteresis: two thresholds
	•	ON if p > T_on for N_on seconds
	•	OFF if p < T_off for N_off seconds
(T_on > T_off prevents flapping)
	•	Minimum dwell time: e.g., don’t allow another transition for X seconds
	•	Optional: Viterbi/HMM over a 4-state combined space {00, 01, 10, 11} (none/fridge/ac/both) to enforce plausible transitions.

This is exactly the kind of “engineering wrapper” that makes weakly labeled training usable for clean events.

⸻

5) Real-time deployment on your MacBook (fast + clean)

A. Runtime
	•	Capture audio via CoreAudio (or sounddevice in Python)
	•	Process in chunks (e.g., 1 second)
	•	Maintain a rolling buffer for the BEATs window (e.g., 4 seconds)

B. Acceleration options

If you want this to be efficient and battery-friendly:
	•	Export the model to ONNX, run with onnxruntime using the CoreML Execution Provider (uses Apple hardware where possible).  ￼
	•	Or convert ONNX → Core ML using Core ML tools / converters.  ￼

(Practically: many folks prototype in PyTorch, then move to ONNX/CoreML once the model is stable.)

⸻

The “most state-of-the-art BEATs approach” in one sentence

Use a large pretrained BEATs encoder to produce time-resolved embeddings, train a small multi-label temporal SED head on sliding windows for “AC present / fridge present,” then convert the probability streams into on/off events with hysteresis + minimum-duration constraints (optionally with an HMM/Viterbi smoother), and deploy via ONNX→CoreML/onnxruntime-CoreML for on-device inference.  ￼

If you want, I can sketch a concrete window/hop configuration and thresholding recipe that tends to work well for appliances (and won’t spam false toggles).

---

Cool — here’s a concrete, “will actually run in your apartment” configuration + a thresholding/state-machine recipe that turns BEATs-based presence probabilities into clean:
	•	fridge on/off
	•	ac on/off

I’m going to assume you’ve already got (or will build) a model that outputs two probabilities per inference step:
	•	p_fridge = probability fridge is audible/present
	•	p_ac = probability AC is audible/present

Everything below is how to (a) run inference in real time and (b) convert those probabilities into stable events without flapping.

⸻

Recommended real-time windowing

Audio + inference cadence
	•	Capture chunk: 1.0 s audio frames from the mic
	•	Ring buffer: 6.0 s (keep last 6 seconds)
	•	Inference window: 4.0 s (read the newest 4 seconds from the ring buffer)
	•	Inference hop: every 0.5 s

Why this works:
	•	4 seconds is long enough to “hear” steady appliances and suppress brief transients.
	•	0.5 s hop gives quick-enough detection without burning CPU.

Preprocessing (match BEATs)
	•	Resample 44,100 → 16,000 Hz with a high-quality resampler (soxr is great).
	•	Compute 128-bin log-mel filterbank features with 25 ms window / 10 ms hop.
	•	Feed into BEATs, take time-resolved embeddings (not a single global pooled vector).

⸻

Smoothing that doesn’t lag too badly

You’ll get jitter in p_fridge and p_ac. Smooth before thresholding:

1) Median filter (kills spikes)
	•	Keep the last 9 inference points (~4.5 s since hop=0.5 s)
	•	p_med = median(last_9_probs)

2) EMA (stabilizes but still responsive)

Use an exponential moving average with time constant ~6 s:
	•	alpha = exp(-hop / tau) where hop=0.5, tau=6.0 → alpha ≈ exp(-0.0833) ≈ 0.92
	•	p_smooth = alpha * p_smooth_prev + (1 - alpha) * p_med

This combo is a sweet spot for appliance audio.

⸻

Hysteresis + hold-time thresholds (the core of clean events)

You want two thresholds per device:
	•	Turn ON threshold T_on (higher)
	•	Turn OFF threshold T_off (lower)

And two “must persist” durations:
	•	ON must persist N_on seconds
	•	OFF must persist N_off seconds

Good starting values (works surprisingly often)

AC (usually loud/steady)
	•	T_on_ac = 0.75
	•	T_off_ac = 0.35
	•	N_on_ac = 4.0 s  (needs 8 consecutive hops at 0.5 s)
	•	N_off_ac = 8.0 s (needs 16 hops)

Fridge (often quieter, more variable)
	•	T_on_fr = 0.65
	•	T_off_fr = 0.30
	•	N_on_fr = 6.0 s  (12 hops)
	•	N_off_fr = 12.0 s (24 hops)

Add a cooldown to stop rapid toggles:
	•	cooldown = 20 s (ignore further state changes for 20s after an event)

This yields stable, human-sensible events.

⸻

A calibration trick using only your four wavs

Even with just all_off.wav, ac_on.wav, fridge_on.wav, all_on.wav, you can set thresholds intelligently:
	1.	Run your model over each file and collect p_ac and p_fridge at every hop.
	2.	For each device:
	•	Let P_absent be probs from clips where that device is OFF
	•	Let P_present be probs from clips where that device is ON
	3.	Choose:
	•	T_off = percentile(P_absent, 95)  (high end of “definitely absent”)
	•	T_on  = percentile(P_present, 10) (low end of “definitely present”)
	4.	If T_on <= T_off (overlap), widen the gap manually (e.g. set T_off -= 0.05, T_on += 0.05) or increase smoothing / window length.

This usually produces much better thresholds than guessing.

⸻

Event logic (simple and robust)

Track each device independently with a tiny state machine:

State: is_on (bool)

Maintain two counters:
	•	on_count = consecutive hops with p_smooth >= T_on
	•	off_count = consecutive hops with p_smooth <= T_off

Rules:
	•	If is_on == False:
	•	increment on_count when above T_on, else reset
	•	when on_count * hop >= N_on and not in cooldown → emit device on, set is_on=True, reset counts, start cooldown timer
	•	If is_on == True:
	•	increment off_count when below T_off, else reset
	•	when off_count * hop >= N_off and not in cooldown → emit device off, set is_on=False, reset counts, start cooldown timer

⸻

Drop-in Python skeleton (state machine only)

import time
from dataclasses import dataclass

@dataclass
class HysteresisDetector:
    name: str
    hop_s: float
    T_on: float
    T_off: float
    N_on_s: float
    N_off_s: float
    cooldown_s: float

    is_on: bool = False
    on_count: int = 0
    off_count: int = 0
    cooldown_until: float = 0.0

    def update(self, p: float, now: float | None = None):
        """Return event string or None."""
        if now is None:
            now = time.time()

        in_cooldown = now < self.cooldown_until

        if not self.is_on:
            if p >= self.T_on:
                self.on_count += 1
            else:
                self.on_count = 0

            if (not in_cooldown) and (self.on_count * self.hop_s >= self.N_on_s):
                self.is_on = True
                self.on_count = 0
                self.off_count = 0
                self.cooldown_until = now + self.cooldown_s
                return f"{self.name} on"
        else:
            if p <= self.T_off:
                self.off_count += 1
            else:
                self.off_count = 0

            if (not in_cooldown) and (self.off_count * self.hop_s >= self.N_off_s):
                self.is_on = False
                self.on_count = 0
                self.off_count = 0
                self.cooldown_until = now + self.cooldown_s
                return f"{self.name} off"

        return None

Instantiate like:

ac = HysteresisDetector("ac", hop_s=0.5, T_on=0.75, T_off=0.35, N_on_s=4, N_off_s=8, cooldown_s=20)
fr = HysteresisDetector("fridge", hop_s=0.5, T_on=0.65, T_off=0.30, N_on_s=6, N_off_s=12, cooldown_s=20)

Then each inference hop (every 0.5s), call ac.update(p_ac_smooth) and fr.update(p_fr_smooth) and emit events when it returns a string.

⸻

One extra improvement that helps in apartments

If you get “false AC” when fridge is on (or vice versa), add a 4-state consistency pass:
	•	Compute both probabilities each hop
	•	Convert to a combined state among {none, fridge, ac, both} using the same hysteresis idea
	•	Optionally run a tiny Viterbi/HMM with high self-transition probability to prevent impossible rapid switching

But honestly: start with the independent detectors + cooldown. It’s usually enough.

⸻

---

