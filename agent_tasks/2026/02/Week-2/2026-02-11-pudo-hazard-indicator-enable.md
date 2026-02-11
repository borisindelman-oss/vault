# 2026-02-11 — PUDO hazard indicator enablement

## Summary
- Enabled hazard as a representable indicator class for parking/PUDO model outputs.
- Kept non-parking models on the existing default 3-class indicator head.
- Made indicator CE loss logic class-count aware so labels are validated against logits width instead of hardcoded `0..2`.

## Code Changes
- `wayve/ai/si/configs/parking/parking_config.py`
  - Set `num_indicator_classes=4` in `ParkingOutputAdaptorCfg`.
- `wayve/ai/zoo/outputs/output_adaptor.py`
  - Added `num_indicator_classes` argument (default `3`) and plumbed it into `IndicatorOutputHead`.
- `wayve/ai/zoo/outputs/indicator_output_head.py`
  - Added configurable `num_indicator_classes`.
- `wayve/ai/zoo/losses/imitation_losses.py`
  - Updated indicator CE masking/clamping to use `indicator_probs.shape[-1]`.
- `wayve/ai/zoo/losses/kd_loss.py`
  - Updated indicator CE masking/clamping to use `indicator_probs.shape[-1]`.
- `wayve/ai/zoo/outputs/test/test_indicator_output_head.py`
  - Added regression test for 4-class indicator head behavior.

## Validation
- `python -m py_compile wayve/ai/zoo/outputs/indicator_output_head.py wayve/ai/zoo/outputs/output_adaptor.py wayve/ai/zoo/losses/imitation_losses.py wayve/ai/zoo/losses/kd_loss.py wayve/ai/si/configs/parking/parking_config.py`
- `bazel test //wayve/ai/zoo:test_outputs_py_test --nocache_test_results --test_arg=-k=test_indicator_output_head`
- `bazel test //wayve/ai/zoo:test_losses_py_test --nocache_test_results --test_arg=-k=indicator_cross_entropy_loss`

## Notes
- The deployment wrapper DILC behavior remains unchanged: parking can still zero indicator input when `dilc_on=False`.
