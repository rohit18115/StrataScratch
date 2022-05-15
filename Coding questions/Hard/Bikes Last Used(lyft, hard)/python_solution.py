import pandas as pd

result = (
    dc_bikeshare_q1_2012.groupby("bike_number")["end_time"]
    .max()
    .to_frame("last_used")
    .reset_index()
    .sort_values(by="last_used", ascending=False)
)
