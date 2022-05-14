SELECT
 words1,
 words2
FROM
 google_word_lists
WHERE
 (words1 ILIKE 'g%' OR 
 words1 ILIKE '%,g%') OR 
 (words2 ILIKE 'g%' OR 
 words2 ILIKE '%,g%')