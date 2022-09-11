#!/usr/bin/python3
"""
Script that lists all states
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curs = db.cursor()
    curs.execute("SELECT * \
    FROM states \
    FROM cities;")
    city = curs.fetchall()

    for city in cities:
        print(cities)
