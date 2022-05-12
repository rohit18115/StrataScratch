import pandas as pd
import numpy as np

days = facebook_user_interactions[
    (facebook_user_interactions["day"] == 0) | (facebook_user_interactions["day"] == 2)
]
result = (
    days.groupby(["day"])
    .size()
    .to_frame("n_interations")
    .reset_index()
    .sort_values("day")
)
