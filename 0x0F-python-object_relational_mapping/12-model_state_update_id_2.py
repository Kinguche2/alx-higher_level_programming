#!/usr/bin/python3
"""
Adds state object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy import update

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = update(State).where(State.id == "2").values(name="New Mexico").\
            execution_options(synchronize_session="fetch")

    session.execute(stmt)
