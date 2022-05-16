import pandas as pd
import numpy as np

result = winemag_p2[
    (winemag_p2["region_1"].notnull()) & (winemag_p2["taster_name"] == "Roger Voss")
][["variety"]].drop_duplicates()
