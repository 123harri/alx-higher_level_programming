#!/usr/bin/python3
""" Lists all cities of a given state from the database hbtn_0e_0_usa. """

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Execute SQL query to fetch cities of the given state
    cur.execute("""SELECT cities.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()

    # Extract city names from the result and print them
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db.close()
