#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
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

    for instance in session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id
    ):
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))

    session.close()
