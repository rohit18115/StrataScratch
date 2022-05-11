import pandas as pd
import numpy as np

product_logins["login_date"] = pd.to_datetime(
    product_logins["login_date"], format="%Y-%m-%d"
)
year_2016 = product_logins[
    (product_logins["login_date"] > pd.Timestamp(2016, 1, 1))
    & (product_logins["login_date"] < pd.Timestamp(2016, 12, 31))
]
distinct_2016 = year_2016[["account_id"]].drop_duplicates()
result = len(distinct_2016)
