import pandas as pd
import numpy as np

df_sent = fb_friend_requests[fb_friend_requests.action == "sent"]
df_accepted = fb_friend_requests[fb_friend_requests.action == "accepted"]
new_df = pd.merge(
    df_sent,
    df_accepted,
    how="left",
    left_on=["user_id_sender", "user_id_receiver"],
    right_on=["user_id_sender", "user_id_receiver"],
)
accepted_count = new_df.groupby(["date_x"]).count().reset_index()
accepted_count["acceptance_rate"] = (
    accepted_count["action_y"] / accepted_count["action_x"]
)
result = accepted_count[["date_x", "acceptance_rate"]]
result
