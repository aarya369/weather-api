# Weather API

A FastAPI application that fetches historical weather data from the Open-Meteo Archive API and stores it in a PostgreSQL database.

## Features

* Fetch historical weather data from Open-Meteo
* Store weather observations in PostgreSQL
* REST API built using FastAPI
* SQLAlchemy ORM for database operations
* Dockerized deployment using Docker Compose
* Automated API testing

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Docker Compose
* Requests
* Pytest

## Project Structure

```text
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── app/
    ├── __init__.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── crud.py
    ├── weather_service.py
    ├── main.py
    └── test_weather.py
```

## How It Works

1. User sends a request to the FastAPI application.
2. FastAPI calls the Open-Meteo Archive API.
3. Weather data is returned in JSON format.
4. The application stores selected fields in PostgreSQL.
5. Stored weather data can be retrieved through API endpoints.

## Running the Project

### Prerequisites

* Docker Desktop

### Clone the Repository

```bash
git clone https://github.com/aarya369/weather-api.git
cd weather-api
```

### Start the Application

```bash
docker compose up --build
```

This command:

* Starts PostgreSQL
* Creates the `weatherdb` database
* Builds the FastAPI container
* Starts the API server

## API Documentation

After startup, open:

```text
http://localhost:8000/docs
```

FastAPI automatically generates interactive Swagger documentation.

## Database

Database: `weatherdb`

The application uses PostgreSQL running inside Docker and persists data using Docker volumes.

## Data Source

Historical weather data is fetched from:

https://archive-api.open-meteo.com/v1/archive

## Future Improvements

* Add weather statistics endpoints
* Add data visualization dashboard
* Add forecasting models
* Add authentication and user management
* Add CI/CD pipeline

## Author

Aarya Mehta
