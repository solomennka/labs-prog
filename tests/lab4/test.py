import pytest
from src.lab4.database import base, engine, sessionlocal
from src.lab4.models import User, Book, Booking
from src.lab4.services import add_user, add_book, create_booking, delete_booking


@pytest.fixture(autouse=True)
def cleanup():
    """Fixture: create clean database before and after each test"""
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
    yield
    base.metadata.drop_all(engine)


def test_add_user():
    """Test: check user creation"""
    add_user("Alex", "alex@mail.com")
    session = sessionlocal()
    user = session.query(User).filter_by(email="alex@mail.com").first()
    assert user is not None
    assert user.name == "Alex"
    session.close()


def test_add_book():
    """Test: check book creation"""
    add_book("Harry Potter", "Rowling", 5)
    session = sessionlocal()
    book = session.query(Book).filter_by(title="Harry Potter").first()
    assert book is not None
    assert book.author == "Rowling"
    assert book.copies_available == 5
    session.close()


def test_create_booking():
    """Test: check booking creation"""
    add_user("Alex", "alex@mail.com")
    add_book("Book", "Author", 3)
    result = create_booking(1, 1)
    session = sessionlocal()
    booking = session.query(Booking).first()
    book = session.query(Book).first()
    assert result == "Booked"
    assert booking is not None
    assert book.copies_available == 2
    session.close()


def test_create_booking_no_copies():
    """Test: booking should fail if no copies available"""
    add_user("Alex", "alex@mail.com")
    add_book("Book", "Author", 0)
    result = create_booking(1, 1)
    assert result == "Book not available"


def test_delete_booking():
    """Test: check booking deletion"""
    add_user("Alex", "alex@mail.com")
    add_book("Book", "Author", 1)
    create_booking(1, 1)
    result = delete_booking(1)
    session = sessionlocal()
    booking = session.query(Booking).first()
    book = session.query(Book).first()
    assert result == "Deleted"
    assert booking is None
    assert book.copies_available == 1
    session.close()