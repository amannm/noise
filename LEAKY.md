You can avoid leaky splits without collecting any new audio by changing where you split and by enforcing temporal + group isolation. The main leakage in your setup comes from windowing a continuous recording and then randomly splitting the windows (adjacent windows share ~all the same background).

Here are the best options, in order of “least leaky” → “most practical” for only 4 files.

1) Split at the raw-audio level first (never split after windowing)

Rule: pick train/val/test time ranges on each .wav, then window inside each range.

Bad (leaky):
	•	Window entire file → shuffle windows → train/test split

Good:
	•	Choose contiguous ranges:
	•	train: 0:00–1:40
	•	gap: 1:40–1:55 (thrown away)
	•	val: 1:55–2:25
	•	gap: 2:25–2:40
	•	test: 2:40–3:00

Why the gaps? They “purge” overlap and slow drift, so your 2s windows with 0.5s hop can’t share content across splits.

Pick gap ≥ (window_length + a bit), e.g. if you use 2.0s windows, do 5–10s gap.

2) Use blocked / “purged” cross-validation instead of one random split

With only 3 minutes per file, you’ll get much more reliable estimates by doing blocked folds:

For each file:
	•	Divide into, say, 6 contiguous blocks of 30s.
	•	For fold k: test on block k, train on the other blocks,
	•	drop the neighboring blocks (purge) to avoid adjacency leakage.

This is the time-series equivalent of “GroupKFold + embargo”.

3) Keep groups separate when you can, but don’t destroy label coverage

A pure “leave-one-file-out” is clean but breaks label coverage (each file is basically one state). You can still use “group” ideas:
	•	Treat each contiguous segment as a group (not each window).
	•	Ensure no segment contributes windows to multiple splits.

So you still evaluate on held-out time segments, but keep all 4 states represented by drawing segments from each file.

4) Prevent “pipeline leakage” (easy to miss)

Even if you split correctly, these can leak:
	•	Normalization stats: if you compute mean/variance (of log-mel, embeddings, etc.), compute them on train only, then reuse for val/test.
	•	Threshold tuning / hysteresis: pick T_on/T_off, smoothing α, K using val only. Touching test for tuning is leakage.
	•	Stateful smoothing across boundaries: when you evaluate, reset EMA + state machine at the start of each split segment. Otherwise the model “remembers” test context.

5) If you need more robustness without “new samples,” use augmentation (not splitting tricks)

This doesn’t fix leakage, but it reduces overfitting to the specific noise print of each file:
	•	random gain
	•	random EQ / bandpass
	•	mix in low-level noise from all_off.wav (but only from train ranges!)
	•	time masking / specaugment-like masking on features

Key rule: augment only training windows.

⸻

A simple, strong recipe for your case
	•	Resample to 16 kHz mono
	•	Choose window=2.0s, hop=0.5s
	•	For each wav, define:
	•	train first 100s
	•	purge 10s
	•	val next 30s
	•	purge 10s
	•	test last 30s
	•	Window inside each region
	•	Tune thresholds on val; report final on test

This gives you a clean test that isn’t just “adjacent windows from the same moments”.

If you tell me your intended window/hop and whether you want cross-val or one held-out test, I can sketch the exact split indexing logic (time → sample indices) so it’s hard to mess up.