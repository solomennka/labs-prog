from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///library.db", echo=True)
base = declarative_base()
sessionlocal=sessionmaker(bind=engine)