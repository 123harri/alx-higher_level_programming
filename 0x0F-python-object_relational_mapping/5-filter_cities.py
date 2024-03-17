#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    """
    Function to list all cities of a given state
    from the database hbtn_0e_4_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): Name of the state.

    Returns:
        None
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        query = "SELECT cities.id, cities.name FROM cities \
                 JOIN states ON states.id = cities.state_id \
                 WHERE states.name = %s \
                 ORDER BY cities.id"
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()
        for city in cities:
            print(city)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]
    list_cities_by_state(username, password, database, state_name)
