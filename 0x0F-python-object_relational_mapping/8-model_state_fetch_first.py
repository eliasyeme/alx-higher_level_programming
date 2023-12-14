#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    port = 3306

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:{}/{}".format(
            user_name, password, port, db_name
        ),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
