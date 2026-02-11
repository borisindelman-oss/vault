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

## Notebook snippet
```python
import asyncio
import os
import numpy as np

import wayve.ai.lib.data.storage.binary_keys as BK
from wayve.ai.language.action.interfaces import FRAME_PATH
from wayve.ai.lib.data.pipes.utils import cache_and_load_npz_file_async
from wayve.ai.lib.map_async import get_loop


def load_timestamps_unixus(run_id: str) -> np.ndarray:
    meta_data = asyncio.run_coroutine_threadsafe(
        cache_and_load_npz_file_async(run_id, os.path.join(FRAME_PATH, "metadata"), "~/.cache/frame_meta_data"),
        get_loop(),
    ).result()
    key = f"{run_id}{BK.FRAMES_METADATA_TIMESTAMP_KEY_SUFFIX}"
    return np.sort(meta_data[key])


def resolve_offsets_to_unixus(
    timestamps_unixus: np.ndarray,
    offsets,
    offset_unit: str = "microseconds",
):
    first_ts = int(timestamps_unixus[0])
    offset_us_values = []
    for value in offsets:
        if value >= 1e12:
            offset_us_values.append(int(value) - first_ts)
        elif offset_unit == "seconds":
            offset_us_values.append(int(value * 1e6))
        else:
            offset_us_values.append(int(value))

    timestamp_offset = timestamps_unixus - first_ts
    resolved = []
    for offset_us in offset_us_values:
        idx = int(np.abs(timestamp_offset - offset_us).argmin())
        resolved.append(int(timestamps_unixus[idx]))
    return resolved


run_id = "<run_id>"
offsets_us = [7322705269, 7351671913]
timestamps_unixus = load_timestamps_unixus(run_id)
resolved = resolve_offsets_to_unixus(timestamps_unixus, offsets_us, offset_unit="microseconds")
list(zip(offsets_us, resolved))
```
