from database import engine, base
from database import sessionlocal
from models import User, Book, Booking
from services import add_user

session = sessionlocal()
add_user("Alex", "alex@mail.com")

users = session.query(User).all()
print(users)