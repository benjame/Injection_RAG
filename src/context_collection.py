import subprocess
import datetime
import argparse
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy ORM base class
Base = declarative_base()

# Define the sqlmap_executions table as an ORM class
class SqlmapExecution(Base):
    __tablename__ = 'sqlmap_executions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    execution_time = Column(String, nullable=False)
    execution_date = Column(String, nullable=False)
    sqlmap_options = Column(Text, nullable=False)
    sqlmap_output = Column(Text, nullable=False)

# Function to create the database and table
def create_database(db_name):
    engine = create_engine(f'sqlite:///{db_name}')
    Base.metadata.create_all(engine)
    return engine

# Function to insert execution details into the database
def insert_execution(session, user_name, options, output):
    timestamp = datetime.datetime.now()
    execution_time = timestamp.strftime("%H:%M:%S")
    execution_date = timestamp.strftime("%Y-%m-%d")
    execution = SqlmapExecution(
        user_name=user_name,
        execution_time=execution_time,
        execution_date=execution_date,
        sqlmap_options=options,
        sqlmap_output=output
    )
    session.add(execution)
    session.commit()

def run_sqlmap(command, session, user_name, options):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output = ""
    for line in process.stdout:
        print(line, end='')  # Print the output to the console
        output += line

    process.stdout.close()
    process.wait()

    insert_execution(session, user_name, options, output)

def user_loop(session):
    while True:
        # Request user input
        url = input("Enter the target URL: ")
        user_name = input("Enter your name: ")
        sqlmap_args = input("Enter any additional sqlmap arguments (leave blank for none): ")

        # Construct the sqlmap command
        sqlmap_command = ["sqlmap", "-u", url]
        if sqlmap_args:
            sqlmap_command.extend(sqlmap_args.split())

        options = " ".join(sqlmap_command)
        
        # Run sqlmap and store the output
        run_sqlmap(sqlmap_command, session, user_name, options)

        # Ask the user if they want to continue
        cont = input("Do you want to run another command? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    # Define the database name
    db_name = 'sqlmap_output.db'
    engine = create_database(db_name)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Start the user input loop
    user_loop(session)