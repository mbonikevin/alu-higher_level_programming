#!/usr/bin/python3
"""
Test script for deleting States with a name containing the letter 'a'
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Add initial data
    initial_states = [
        State(name='6GXGSB'),
        State(name='58PWVI'),
        State(name='1L8YLW'),
        State(name='P9IMKP'),
        State(name='6EI7ZK'),
        State(name='1W2PXD'),
        State(name='PaDEBU'),
        State(name='VH0OHF'),
        State(name='1FDNSC'),
        State(name='O11FX9'),
        State(name='9MH3ND'),
        State(name='Va667Q'),
        State(name='RJEUQW'),
        State(name='RR93B9'),
        State(name='RM26XB'),
        State(name='03B5RL'),
        State(name='TLL9HW'),
        State(name='VTK0NR'),
        State(name='SDWJ5J'),
        State(name='OZZGK9'),
        State(name='797YH1'),
        State(name='X2FKCD'),
        State(name='VZYRKF'),
        State(name='IO1PE5'),
        State(name='K83J6a'),
        State(name='ELEGPY'),
        State(name='4ECKHT'),
        State(name='HLCDZL'),
        State(name='Y0K47C'),
        State(name='X2ONDG')
    ]
    
    for state in initial_states:
        session.add(state)
    
    session.commit()

    # Run the script to delete states with 'a' in the name
    import subprocess
    subprocess.call(['./13-model_state_delete_a.py', sys.argv[1], sys.argv[2], sys.argv[3]])

    # Print remaining states
    remaining_states = session.query(State).order_by(State.id).all()
    for state in remaining_states:
        print(f"{state.id}\t{state.name}")
    
    session.close()
