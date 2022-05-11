# Import your libraries
import pandas as pd

# Start writing code
product_logins.head()

x = product_logins.loc[product_logins["login_date"].str.contains("2016")]
result = x["account_id"].drop_duplicates()
result = len(result)
