# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details[airbnb_search_details["city"] == "LA"][
    "neighbourhood"
].drop_duplicates()
# another way to do it: #airbnb_search_details[airbnb_search_details['city']=='LA']['neighbourhood'].unique()
