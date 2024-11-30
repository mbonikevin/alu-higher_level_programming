#!/usr/bin/python3
"""
This script connects to the
'hbtn_0e_0_usa' database and lists all the states
from the 'states' table, displaying each state in the result.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)
