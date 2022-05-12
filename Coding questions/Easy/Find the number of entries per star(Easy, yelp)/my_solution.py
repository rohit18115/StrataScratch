import pandas as pd

yelp_reviews.head()
stars_order = yelp_reviews.groupby("stars").size().reset_index()
stars_order.columns = ["stars", "nums"]
stars_order.sort_values(by="nums")
