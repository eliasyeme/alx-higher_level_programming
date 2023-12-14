#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the database
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

    session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session=False
    )
    session.commit()
    session.close()
