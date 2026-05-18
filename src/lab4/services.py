from models import User, Book, Booking
from database import sessionlocal
from datetime import date


def add_user(name: str, email: str):
    """
    Function that adds a new user to the database.
    @param name: str - user name
    @param email: str - user email
    """
    session = sessionlocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.close()


def add_book(title: str, author: str, copies: int):
    """
    Function that adds a new book to the database.
    @param title: str - book title
    @param author: str - book author
    @param copies: int - number of available copies
    """
    session = sessionlocal()
    book = Book(title=title, author=author, copies_available=copies)
    session.add(book)
    session.commit()
    session.close()


def create_booking(user_id: int, book_id: int) -> str:
    """
    Function that creates a booking for a book.
    Decreases available copies after booking.
    @param user_id: int - user identifier
    @param book_id: int - book identifier
    @return: str - booking status message
    """
    session = sessionlocal()
    book = session.query(Book).filter_by(id=book_id).first()
    if not book or book.copies_available <= 0:
        session.close()
        return "Book not available"

    booking = Booking(user_id=user_id, book_id=book_id, booking_date=date.today())
    book.copies_available -= 1
    session.add(booking)
    session.commit()
    session.close()
    return "Booked"


def delete_booking(booking_id: int) -> str:
    """
    Function that deletes a booking.
    Increases available copies after deletion.
    @param booking_id: int - booking identifier
    @return: str - deletion status message
    """
    session = sessionlocal()
    booking = session.query(Booking).filter_by(id=booking_id).first()
    if not booking:
        session.close()
        return "Not found"
    book = session.query(Book).filter_by(id=booking.book_id).first()
    if book:
        book.copies_available += 1
    session.delete(booking)
    session.commit()
    session.close()
    return "Deleted"
