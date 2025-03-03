#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

    company1 = Company(name='Tech Corp', founding_year=2000)
    company2 = Company(name='DevWorks', founding_year=2010)

    dev1 = Dev(name='Alice')
    dev2 = Dev(name='Bob')

    session.add_all([company1, company2, dev1, dev2])
    session.commit()

   
    company1.give_freebie(dev1, "T-shirt", 10)
    company1.give_freebie(dev2, "Mug", 5)
    company2.give_freebie(dev1, "Sticker", 2)

    
    freebies = session.query(Freebie).all()
    for freebie in freebies:
        print(freebie.print_details())
    
    
    print(dev1.received_one("T-shirt"))  
    print(dev1.received_one("Hoodie"))  
