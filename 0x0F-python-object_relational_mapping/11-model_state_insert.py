#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]
    port = 3306
    state_name = "Louisiana"

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:{}/{}".format(
            user_name, password, port, db_name
        ),
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
