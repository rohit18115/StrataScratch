# Import your libraries
import pandas as pd

# Start writing code
facebook_reactions.head()
facebook_likes = facebook_reactions[["friend", "post_id", "reaction"]]
facebook_likes[facebook_likes["reaction"] == "like"].groupby(
    "friend"
).sum().reset_index()["friend"]
