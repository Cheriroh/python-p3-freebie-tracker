#!/usr/bin/env python3

from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(name='Tech Corp', founding_year=2000)
company2 = Company(name='DevWorks', founding_year=2010)
dev1 = Dev(name='Alice')
dev2 = Dev(name='Bob')

session.add_all([company1, company2, dev1, dev2])
session.commit()

company1.give_freebie(session, dev1, "T-shirt", 10)
company1.give_freebie(session, dev2, "Mug", 5)
company2.give_freebie(session, dev1, "Sticker", 2)

session.commit()

print("Database seeded successfully!")
