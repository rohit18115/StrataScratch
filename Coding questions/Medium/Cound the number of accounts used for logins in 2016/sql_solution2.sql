select count (distinct account_id)
from (select account_id, extract('year' from login_date) as year
from product_logins) as sub
where year = 2016