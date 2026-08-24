from pydantic import BaseModel

# User schemas
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str


# Event schemas
class EventCreate(BaseModel):
    name: str
    location: str
    total_seats: int


class EventResponse(BaseModel):
    id: int
    name: str
    location: str
    total_seats: int
    available_seats: int

    class Config:
        from_attributes = True


# Booking schemas
class BookingCreate(BaseModel):
    user_id: int
    event_id: int