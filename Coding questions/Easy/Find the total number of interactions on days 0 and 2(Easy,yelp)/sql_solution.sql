SELECT
 day,
 COUNT(*) AS n_interactions
FROM
 facebook_user_interactions
WHERE
 day = 0 OR 
 day = 2
GROUP BY day