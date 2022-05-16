# Import your libraries
import pandas as pd

# Start writing code
winemag_p2[
    (winemag_p2["taster_name"] == "Roger Voss") & ~(winemag_p2["region_1"].isnull())
]["variety"].unique()
