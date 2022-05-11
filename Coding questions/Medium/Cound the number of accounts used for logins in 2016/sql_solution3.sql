select count(distinct account_id) as tot
from product_logins
where login_date<'2017-01-01' and login_date>='2016-01-01'