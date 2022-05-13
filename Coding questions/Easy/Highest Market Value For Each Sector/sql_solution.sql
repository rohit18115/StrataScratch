SELECT
    sector,
    max(marketvalue) AS max_marketvalue
FROM forbes_global_2010_2014
GROUP BY 
    sector
ORDER BY 
    max_marketvalue DESC
