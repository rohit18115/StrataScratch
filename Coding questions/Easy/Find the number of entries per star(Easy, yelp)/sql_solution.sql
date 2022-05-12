SELECT 
    stars,
    count(*) AS n_entries
FROM yelp_reviews
GROUP BY 
    stars
ORDER BY
    stars