#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states_by_name(username, password, database, state_name):
    """
    Function to list all states from the database hbtn_0e_0_usa
    where the name matches the provided argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): The name of the state to search for.

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
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE %s", (state_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:5]
    list_states_by_name(username, password, database, state_name)
