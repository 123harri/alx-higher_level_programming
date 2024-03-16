#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    """
    Function to filter states by name and display matching values.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): State name to search for.

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
        query = f"SELECT * FROM states WHERE name = '{state_name}' ORDER BY id"
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)
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
    filter_states_by_name(username, password, database, state_name)
