# Import your libraries
import pandas as pd

# Start writing code
product_logins.head()
product_logins["year"] = pd.DatetimeIndex(product_logins["login_date"]).year
product_logins[product_logins["year"] == 2016]["account_id"].drop_duplicates().count()
