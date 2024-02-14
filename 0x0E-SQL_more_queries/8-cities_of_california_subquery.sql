-- List all cities of California from the hbtn_0d_usa database.
-- List all cities of California
SELECT id, name 
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
