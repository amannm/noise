# Project objectives
- Live noise detection that reports one of three states in an apartment:
  1. AC blower on (drowns out fridge compressor).
  2. Fridge compressor on (audible only when AC is off).
  3. Neither AC blower nor Fridge compressor is on.
- All data preparation and model training steps to achieve this.

# Reference material
[BEATs Source Code](reference/unilm/beats)
[CoreML Tools](reference/coremltools)
[CoreML Documentation](reference/coreml-docs)

# Environment
- **Always** use `uv` for working with Python.

# Additional constraints
- Deliver a *quality* implementation, **NOT** a quick one.
- No backwards compatibility.
- No fallback behaviors.
- No legacy code.