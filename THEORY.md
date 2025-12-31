Cool — if AC and fridge can overlap, you want a multi-label detector: two independent “is fridge ON?” and “is AC ON?” heads, each driven by a strong pretrained embedding model, plus smoothing + hysteresis to emit clean ON/OFF events.

Below is a practical, “SOTA in spirit” pipeline that works well on macOS and with small data.

⸻

1) Model choice (pretrained embeddings)

Pick one embedding backbone and stick with it:

Top-tier (strong general audio):
	•	BEATs embeddings (excellent for general acoustic events)
	•	AST / PaSST / HTS-AT embeddings (AudioSet-pretrained transformers; also very strong)

Pragmatic note: These are heavy-ish but fine on a Mac laptop if you compute embeddings at ~1–2 Hz. If you want ultra-lightweight later, you can distill to a tiny model once it works.

Recommended for your use: BEATs or AST embeddings → simple heads.

⸻

2) Turn your 3 clips into a multi-label training set

You currently have:
	•	all_off.wav  → labels: fridge=0, ac=0
	•	fridge_on.wav → fridge=1, ac=0  (mostly)
	•	ac_on.wav → fridge=0, ac=1  (mostly)

You don’t have “both on” real audio, but you can still train multi-label heads.

Windowing

Slice into short frames:
	•	window: 1.6s
	•	hop: 0.8s (50% overlap)

For each window, compute an embedding vector e.

Training targets (two binaries)
	•	y_fridge ∈ {0,1}
	•	y_ac ∈ {0,1}

For fridge classifier:
	•	positives: windows from fridge_on.wav
	•	negatives: windows from all_off.wav and ac_on.wav
(similar for AC classifier: negatives include fridge_on.wav)

This teaches each head to ignore the other device as “background-ish” when it’s not the target.

⸻

3) Handle overlap: add synthetic “both on” augmentation (big win)

Because real overlap acoustics can differ, the simplest improvement is to create mixed training windows:

For random aligned windows:
	•	take a window from fridge_on
	•	take a window from ac_on
	•	optionally add a little from all_off
	•	mix audio: mix = a*fridge + b*ac + c*off with random gains

Label those mixed windows:
	•	fridge=1, ac=1

This is surprisingly effective for steady appliances (hum/tonals), even though it’s not a perfect room-interaction simulation.

If you can, the best thing is also to record one extra 3-minute “both_on.wav” to validate and calibrate thresholds, but mixing usually gets you most of the way.

⸻

4) Classifier head: keep it tiny

On top of embeddings:
	•	Logistic regression (or linear SVM) per device is a great default.
	•	If you want even simpler: centroid/prototype (mean embedding of ON vs OFF) with cosine similarity.

With small data, linear heads usually beat fancy deep heads.

⸻

5) Real-time event emission: smoothing + hysteresis + state machine

Frame-level predictions will bounce. Turn them into events like this:

Smoothing

Maintain a rolling average of probabilities:
	•	e.g. 5–15 seconds window (appliances are stable; longer smoothing helps)

Hysteresis thresholds

Two thresholds per device:
	•	turn ON when smoothed prob > T_on for K_on consecutive frames
	•	turn OFF when smoothed prob < T_off for K_off consecutive frames
with T_on > T_off (prevents chatter)

Minimum durations (optional but recommended)
	•	don’t allow ON→OFF unless it stayed ON at least, say, 10–20s
	•	same for OFF→ON (prevents “one-frame blips”)

This is what makes it feel like a reliable “event detector” instead of a twitchy classifier.

⸻

6) macOS implementation notes (mic + performance)

Mic streaming (Python):
	•	sounddevice is the easiest on macOS (CoreAudio under the hood).
	•	Buffer audio into your window size, compute embedding, update states.

Compute rate: you usually don’t need high frequency
	•	run embedding inference at 1–2 embeddings/second (0.5–1.0s hop is plenty)
	•	that’s typically enough to detect appliance transitions with a few-second delay

Acceleration:
	•	PyTorch on macOS can use MPS (Apple Silicon GPU) for speedups, but CPU is often fine if you keep the rate low.

⸻

7) Calibration + evaluation (what to do with only 3 files)

Do this so you don’t fool yourself:
	•	Split each WAV by time (e.g., first 2 minutes train, last 1 minute test), not random windows (random leaks near-identical frames).
	•	Pick thresholds (T_on/T_off) to minimize false events on the held-out segments.
	•	Then test by running live and logging predictions while you toggle devices.

⸻

Best “next step” to make this robust

Even though you can start with just your three clips, the biggest jump in real performance comes from adding:
	1.	a “both on” recording (3 minutes is plenty), and
	2.	a few short “real-world negatives” (talking, footsteps, microwave, sink water, etc.) from the same mic position.

That prevents the classic failure mode: the model confidently calls “AC on” when a truck passes outside.

⸻

If you want, I can sketch a concrete project layout (Python) for macOS:
	•	offline script: window → embeddings → train 2 logistic regressions → save
	•	online script: mic stream → embeddings → smooth → state machine → print/JSON events

(And if you tell me your mic sample rate and whether you’re on Apple Silicon, I’ll suggest sane window/hop + smoothing defaults.)

---

Cool — if AC and fridge can overlap, you want a multi-label detector: two independent “is fridge ON?” and “is AC ON?” heads, each driven by a strong pretrained embedding model, plus smoothing + hysteresis to emit clean ON/OFF events.

Below is a practical, “SOTA in spirit” pipeline that works well on macOS and with small data.

⸻

1) Model choice (pretrained embeddings)

Pick one embedding backbone and stick with it:

Top-tier (strong general audio):
	•	BEATs embeddings (excellent for general acoustic events)
	•	AST / PaSST / HTS-AT embeddings (AudioSet-pretrained transformers; also very strong)

Pragmatic note: These are heavy-ish but fine on a Mac laptop if you compute embeddings at ~1–2 Hz. If you want ultra-lightweight later, you can distill to a tiny model once it works.

Recommended for your use: BEATs or AST embeddings → simple heads.

⸻

2) Turn your 3 clips into a multi-label training set

You currently have:
	•	all_off.wav  → labels: fridge=0, ac=0
	•	fridge_on.wav → fridge=1, ac=0  (mostly)
	•	ac_on.wav → fridge=0, ac=1  (mostly)

You don’t have “both on” real audio, but you can still train multi-label heads.

Windowing

Slice into short frames:
	•	window: 1.6s
	•	hop: 0.8s (50% overlap)

For each window, compute an embedding vector e.

Training targets (two binaries)
	•	y_fridge ∈ {0,1}
	•	y_ac ∈ {0,1}

For fridge classifier:
	•	positives: windows from fridge_on.wav
	•	negatives: windows from all_off.wav and ac_on.wav
(similar for AC classifier: negatives include fridge_on.wav)

This teaches each head to ignore the other device as “background-ish” when it’s not the target.

⸻

3) Handle overlap: add synthetic “both on” augmentation (big win)

Because real overlap acoustics can differ, the simplest improvement is to create mixed training windows:

For random aligned windows:
	•	take a window from fridge_on
	•	take a window from ac_on
	•	optionally add a little from all_off
	•	mix audio: mix = a*fridge + b*ac + c*off with random gains

Label those mixed windows:
	•	fridge=1, ac=1

This is surprisingly effective for steady appliances (hum/tonals), even though it’s not a perfect room-interaction simulation.

If you can, the best thing is also to record one extra 3-minute “both_on.wav” to validate and calibrate thresholds, but mixing usually gets you most of the way.

⸻

4) Classifier head: keep it tiny

On top of embeddings:
	•	Logistic regression (or linear SVM) per device is a great default.
	•	If you want even simpler: centroid/prototype (mean embedding of ON vs OFF) with cosine similarity.

With small data, linear heads usually beat fancy deep heads.

⸻

5) Real-time event emission: smoothing + hysteresis + state machine

Frame-level predictions will bounce. Turn them into events like this:

Smoothing

Maintain a rolling average of probabilities:
	•	e.g. 5–15 seconds window (appliances are stable; longer smoothing helps)

Hysteresis thresholds

Two thresholds per device:
	•	turn ON when smoothed prob > T_on for K_on consecutive frames
	•	turn OFF when smoothed prob < T_off for K_off consecutive frames
with T_on > T_off (prevents chatter)

Minimum durations (optional but recommended)
	•	don’t allow ON→OFF unless it stayed ON at least, say, 10–20s
	•	same for OFF→ON (prevents “one-frame blips”)

This is what makes it feel like a reliable “event detector” instead of a twitchy classifier.

⸻

6) macOS implementation notes (mic + performance)

Mic streaming (Python):
	•	sounddevice is the easiest on macOS (CoreAudio under the hood).
	•	Buffer audio into your window size, compute embedding, update states.

Compute rate: you usually don’t need high frequency
	•	run embedding inference at 1–2 embeddings/second (0.5–1.0s hop is plenty)
	•	that’s typically enough to detect appliance transitions with a few-second delay

Acceleration:
	•	PyTorch on macOS can use MPS (Apple Silicon GPU) for speedups, but CPU is often fine if you keep the rate low.

⸻

7) Calibration + evaluation (what to do with only 3 files)

Do this so you don’t fool yourself:
	•	Split each WAV by time (e.g., first 2 minutes train, last 1 minute test), not random windows (random leaks near-identical frames).
	•	Pick thresholds (T_on/T_off) to minimize false events on the held-out segments.
	•	Then test by running live and logging predictions while you toggle devices.

⸻

Best “next step” to make this robust

Even though you can start with just your three clips, the biggest jump in real performance comes from adding:
	1.	a “both on” recording (3 minutes is plenty), and
	2.	a few short “real-world negatives” (talking, footsteps, microwave, sink water, etc.) from the same mic position.

That prevents the classic failure mode: the model confidently calls “AC on” when a truck passes outside.

⸻

If you want, I can sketch a concrete project layout (Python) for macOS:
	•	offline script: window → embeddings → train 2 logistic regressions → save
	•	online script: mic stream → embeddings → smooth → state machine → print/JSON events

(And if you tell me your mic sample rate and whether you’re on Apple Silicon, I’ll suggest sane window/hop + smoothing defaults.)

---

Nice — 44.1 kHz input on a MacBook Pro (M4 Max) is a great setup. The only “gotcha” is that most SOTA embedding backbones (BEATs/AST) expect 16 kHz, so you’ll resample the mic stream and then run embeddings at ~1–2 Hz.

Here’s a concrete, high-performing recipe you can implement.

⸻

Recommended approach (multi-label + pretrained embeddings)

Backbone

Use BEATs (or AST) as a frozen embedding extractor:
	•	mic audio @ 44.1k → resample to 16k
	•	frame audio into windows
	•	get embedding vector per window

Heads (multi-label)

Train two independent binary classifiers on embeddings:
	•	fridge_on? (yes/no)
	•	ac_on? (yes/no)

This supports simultaneous activation naturally.

Eventing

For each device:
	•	smooth probability over time (EMA or moving average)
	•	hysteresis thresholds (T_on > T_off)
	•	state machine emits: fridge_on, fridge_off, ac_on, ac_off

⸻

Strong defaults for your exact scenario

Windowing / inference rate

Appliance sounds are slow-changing; don’t over-sample:
	•	window_len = 2.0 s
	•	hop = 0.5 s (2 embeddings/sec)
	•	embedding SR = 16,000 Hz → 32,000 samples/window

This is responsive enough to catch transitions with a few seconds delay, and stable enough to avoid chatter.

Smoothing

Use EMA per device probability:
	•	EMA half-life: 5–8 seconds
	•	(equivalently: alpha = 1 - exp(-hop / tau) with tau ≈ 7s)

Hysteresis + debouncing

Start here, then tune from logs:
	•	T_on = 0.80
	•	T_off = 0.35
	•	require K_on = 4 consecutive frames above T_on (≈2s)
	•	require K_off = 8 consecutive frames below T_off (≈4s)
	•	optional: min ON duration 10s to prevent spurious off blips

⸻

Training data strategy from your three WAVs (plus overlap)

Build labeled windows

From:
	•	all_off.wav → fridge=0, ac=0
	•	fridge_on.wav → fridge=1, ac=0
	•	ac_on.wav → fridge=0, ac=1

For fridge head:
	•	positives = fridge_on
	•	negatives = all_off and ac_on

For ac head:
	•	positives = ac_on
	•	negatives = all_off and fridge_on

Add synthetic “both on” examples (recommended)

Because you will see overlap in real life, create mixed windows:
	•	mix = a*fridge + b*ac + c*off with random gains
	•	label: fridge=1, ac=1

This one trick usually improves overlap behavior a lot.

⸻

Implementation sketch (Python)

Offline: extract embeddings + train heads
	•	Extract embeddings for all windows (and mixed windows)
	•	Train 2× logistic regression (or linear SVM)
	•	Save: model weights + thresholds + smoothing params

Core pieces you’ll use:
	•	soundfile or torchaudio to load WAVs
	•	torchaudio.transforms.Resample(44100, 16000)
	•	transformers to run BEATs/AST embeddings
	•	sklearn.linear_model.LogisticRegression
	•	joblib.dump() to save

Online: stream mic → resample → window → embed → classify → state machine
	•	sounddevice for CoreAudio mic input on macOS
	•	maintain a ring buffer at 44.1k
	•	whenever you have 2.0s of audio, resample that window to 16k, embed, classify

⸻

State machine logic (clean ON/OFF events)

This is the part that makes it feel reliable:

class HysteresisEmitter:
    def __init__(self, Ton=0.8, Toff=0.35, Kon=4, Koff=8, min_on_s=10.0, hop_s=0.5):
        self.Ton, self.Toff = Ton, Toff
        self.Kon, self.Koff = Kon, Koff
        self.min_on_frames = int(min_on_s / hop_s)
        self.state = False
        self.above, self.below = 0, 0
        self.on_frames = 0

    def update(self, p):
        events = []
        if not self.state:
            self.above = self.above + 1 if p >= self.Ton else 0
            if self.above >= self.Kon:
                self.state = True
                self.on_frames = 0
                self.above = 0
                events.append("on")
        else:
            self.on_frames += 1
            if self.on_frames < self.min_on_frames:
                return events
            self.below = self.below + 1 if p <= self.Toff else 0
            if self.below >= self.Koff:
                self.state = False
                self.below = 0
                events.append("off")
        return events


⸻

Practical notes for BEATs/AST on a MacBook Pro M4 Max
	•	CPU will likely be enough at 2 embeddings/sec, but you can try PyTorch MPS for extra headroom.
	•	Keep the backbone frozen; train only the linear heads.
	•	Resampling from 44.1k → 16k is standard and won’t hurt appliance detection.

⸻

The single best extra recording (if you do one)

Record 3 minutes with both AC+fridge on. That’s the highest ROI data you can add. If you don’t want to, synthetic mixing will still work surprisingly well, but real overlap audio helps threshold calibration.

⸻

If you want, paste a directory listing (or just confirm the filenames), and I’ll give you a ready-to-run minimal project skeleton:
	•	train.py (windowing, embedding extraction, synthetic mixing, training, save)
	•	listen.py (mic stream, inference, JSON events)