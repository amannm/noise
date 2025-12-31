# Approximate latency for a state change

latency ≈ window_sec
       + (ceil(agg_window_n / 2) - 1) * hop_sec   # median needs majority of new-state windows
       + (debounce_k - 1) * hop_sec               # debouncer
       + processing_lag                           # queue delay if inference is slow

# Worst‑case (more conservative)

If you want a safe upper bound (median doesn’t flip until the whole history fills with new state):

latency ≈ window_sec
       + (agg_window_n - 1) * hop_sec
       + (debounce_k - 1) * hop_sec
       + processing_lag


latency = 6.0

latency += (ceil(7/2) - 1) * 1.5
latency += (7 - 1) * 1.5

latency += (2 - 1) * 1.5
latency += 1