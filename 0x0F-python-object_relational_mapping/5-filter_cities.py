#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (state_name,),
    )

    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()
