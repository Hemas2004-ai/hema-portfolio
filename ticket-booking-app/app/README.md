# Ticket Booking API (FastAPI)

# Overview
This is a Ticket Booking REST API built using FastAPI, SQLAlchemy, and SQLite.
It supports user registration, login, event creation, viewing events, and booking tickets.

# Features

- User Registration
- User Login
- Create Events
- View Events
- Book Tickets
- Automatic seat availability tracking

# Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Pydantic

# Installation

Create virtual environment:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run server:
uvicorn app.main:app --reload

Open docs:
http://127.0.0.1:8000/docs

# API Endpoints

POST /register  
POST /login  
POST /events  
GET /events  
POST /book  

# Author

Reddy Hema Sri Asritha