#!/usr/bin/python3

"""
    This script lists the first State object from the database hbtn_0e_6_usa
"""

if __name__ = "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    driver = "mysql+mysqldb"
    uname = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
            '{}://{}:{}@localhost:3306/{}'.format(
                driver,
                uname,
                password,
                dbname),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()
    print("Nothing" if not state else f"{state.id}: {state.name}")

    Session.close()
