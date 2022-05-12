import pandas as pd
import numpy as np

fb_like = facebook_reactions[facebook_reactions["reaction"] == "like"]
result = fb_like.drop_duplicates(subset="friend")[["friend"]]
