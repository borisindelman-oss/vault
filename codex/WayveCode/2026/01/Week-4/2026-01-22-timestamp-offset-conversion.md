# Timestamp offset → timestamp_unixus (Zak branch)

## Overview
Documented the offset-to-absolute timestamp conversion logic used in Zak's branch for `timestamp_unixus` lookups, with notes for microsecond offsets.

## Source
- `origin/zmurez/trt:wayve/ai/language/action/demo/demo.py#get_corrected_timestamp_unixus`

## Code snippet (Zak branch)
```python
def get_corrected_timestamp_unixus(run_id: str, timestamp_or_offset_str: str) -> int:
    timestamp_unixus = int(timestamp_or_offset_str)
    if timestamp_unixus <= 1e10:
        timestamp_unixus_since_start_of_run = int(float(timestamp_or_offset_str) * 1e6)
        time_table_df = get_run_df(run_id)
        index = (time_table_df["timestamp_offset"] - timestamp_unixus_since_start_of_run).abs().idxmin()
        timestamp_unixus = int(time_table_df.loc[index]["timestamp_unixus"])
    return timestamp_unixus
```

## Notes
- The code treats small values as offsets since run start and snaps to the nearest recorded `timestamp_unixus`.
- If your offsets are already in **microseconds**, skip the `* 1e6` conversion and match directly against `timestamp_offset`.
