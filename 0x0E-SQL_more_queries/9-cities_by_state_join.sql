-- List all cities in the hbtn_0d_usa database with city id, city name, and state name.
-- List all cities with city id, city name, and state name
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
