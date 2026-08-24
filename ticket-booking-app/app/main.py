from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from . import models, schemas, auth

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Home
@app.get("/")
def home():
    return {"message": "Ticket Booking API Running"}


# Register
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = models.User(
        email=user.email,
        password=auth.hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


# Login
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    return {
        "message": "Login successful",
        "user_id": db_user.id
    }


# Create Event
@app.post("/events", response_model=schemas.EventResponse)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):

    new_event = models.Event(
        name=event.name,
        location=event.location,
        total_seats=event.total_seats,
        available_seats=event.total_seats
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event


# Get Events
@app.get("/events", response_model=list[schemas.EventResponse])
def get_events(db: Session = Depends(get_db)):

    events = db.query(models.Event).all()

    return events


# Book Ticket
@app.post("/book")
def book_ticket(booking: schemas.BookingCreate, db: Session = Depends(get_db)):

    event = db.query(models.Event).filter(
        models.Event.id == booking.event_id
    ).first()

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    if event.available_seats <= 0:
        raise HTTPException(status_code=400, detail="No seats available")

    new_booking = models.Booking(
        user_id=booking.user_id,
        event_id=booking.event_id
    )

    event.available_seats -= 1

    db.add(new_booking)
    db.commit()

    return {"message": "Ticket booked successfully"}