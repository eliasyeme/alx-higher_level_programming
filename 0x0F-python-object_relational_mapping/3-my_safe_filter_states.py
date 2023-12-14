#!/usr/bin/python3
"""
display all values in the states table of hbtn_0e_0_usa
where name matches the argument. Safe from MySQL injections!
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
    matching = sys.argv[4]
    cursor.execute(
        """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC
        """,
        (matching,),
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
