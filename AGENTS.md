# Project objectives
- Live noise detection that reports one of three states in an apartment:
  1. AC blower on (drowns out fridge compressor).
  2. Fridge compressor on (audible only when AC is off).
  3. Neither AC blower nor Fridge compressor is on.
- All data preparation and model training steps to achieve this.

# Reference material
[BEATs Source Code](reference/unilm/beats)

# Environment
- Always use `uv` for executing Python scripts.
- `./samples` contains steady-state, ~3-minute `.m4a` recordings for several states, all recorded at 44.1k Hz from a fixed position in the apartment

# Additional constraints
- No backwards compatibility.
- No fallback behaviors.
- No legacy code.