from database import engine, base
from database import sessionlocal
from models import User, Book, Booking

base.metadata.create_all(engine)
