-- lists the number pof records with the same score in the second_tale
SELECT score, COUNT(*) AS number FROM second_table 
GROUP BY score ORDER BY number DESC;
