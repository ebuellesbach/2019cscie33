import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("yelp.csv") as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)
            # break

if __name__ == "__main__":
    main()
