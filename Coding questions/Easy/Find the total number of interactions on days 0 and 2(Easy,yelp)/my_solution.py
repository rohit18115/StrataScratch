# Import your libraries
import pandas as pd

# Start writing code
facebook_user_interactions.head()
facebook_iter = (
    facebook_user_interactions[
        (facebook_user_interactions["day"] == 0)
        | (facebook_user_interactions["day"] == 2)
    ]
    .groupby("day")
    .size()
    .reset_index()
)
