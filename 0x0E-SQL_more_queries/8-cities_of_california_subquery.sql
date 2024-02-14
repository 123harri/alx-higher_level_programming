-- List all cities of California from the hbtn_0d_usa database.
-- List all cities of California
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = @california_id
ORDER BY cities.id ASC;
