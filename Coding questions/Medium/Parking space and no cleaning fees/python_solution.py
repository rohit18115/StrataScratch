# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()
# airbnb_search_details['amenities'] = airbnb_search_details['amenities'].to_frame().applymap(str.lower)
airbnb_search_details[
    (airbnb_search_details["amenities"].str.contains("parking", case=False))
    & (airbnb_search_details["cleaning_fee"] == False)
]["neighbourhood"].unique()
#
