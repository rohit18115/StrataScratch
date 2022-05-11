SELECT 
    count(distinct account_id) AS n_logins
FROM product_logins
WHERE 
    login_date BETWEEN '2016-01-01' AND '2016-12-31'