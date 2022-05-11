SELECT 
    DISTINCT neighbourhood
FROM airbnb_search_details
WHERE 
    amenities ILIKE '%parking%' AND
    cleaning_fee is FALSE