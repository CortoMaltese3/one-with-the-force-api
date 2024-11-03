# One With The Force API

## Overview

The One With The Force API is a RESTful API built with Django, designed to interact with the Star Wars API (SWAPI) and provide users with information about Star Wars characters, films, and starships. It includes features to search and browse resources, as well as vote on favorites. This API also includes error handling and is thoroughly tested to ensure reliability. Users can deploy the API locally, in development, or in production environments using Docker.

## Features

- **Fetch Data from SWAPI**: Retrieve Star Wars data, including characters, films, and starships, from the SWAPI.
- **Resource Search and Filtering**: Search and filter resources by fields like name and title.
- **Vote on Favorites**: Allows users to vote for their favorite characters, films, and starships.
- **API Documentation**: Access interactive API documentation with Swagger and Redoc.
- **Detailed Exception Handling**: Error handling for various scenarios, including not-found resources and validation issues.

## Dependencies

The application relies on the **SWAPI** (https://swapi.dev) to fetch Star Wars data. Other dependencies are listed in `requirements.txt`.

## Setup and Running the Application

### Clone the Repository

To get started, clone the repository:

```bash
git clone https://github.com/CortoMaltese3/one-with-the-force-api.git
cd one-with-the-force-api
```

### Set Up a Local Environment

You have two main options for setting up a local environment: using a virtual environment (`venv`) or using Conda.

#### Using venv

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

#### Using Conda

1. Create a Conda environment:

   ```bash
   conda create --name force-api python=3.12
   conda activate force-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Setup

Before running the application, ensure you have a `.env` file in the root directory. This file is essential for configuring database settings, secret keys, and other environment-specific variables.

1. **Create a `.env` file** in the project root.
2. **Refer to the `env.template` file** for a list of required environment variables. Copy the structure from `env.template` and populate it with your own values.

### Docker Setup (Alternative)

The application can be run in a Dockerized environment with Docker Compose.

1. Make sure you have Docker and Docker Compose installed.
2. Run the application with Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Running in Production

In a production environment, Docker is recommended for consistency and easy deployment. To run the application in production:

1. Ensure Docker and Docker Compose are installed.
2. Follow the setup steps above.
3. Run the production configuration:
   ```bash
   docker-compose up --build
   ```

## API Endpoints

The following endpoints are available for interacting with the One With The Force API:

| Endpoint               | Method | Description                        |
| ---------------------- | ------ | ---------------------------------- |
| `/api/characters/`     | GET    | List all characters.               |
| `/api/characters/{id}` | GET    | Retrieve a single character by ID. |
| `/api/characters/`     | POST   | Create a new character.            |
| `/api/characters/{id}` | PUT    | Update a character by ID.          |
| `/api/characters/{id}` | DELETE | Delete a character by ID.          |
| `/api/films/`          | GET    | List all films.                    |
| `/api/films/{id}`      | GET    | Retrieve a single film by ID.      |
| `/api/films/`          | POST   | Create a new film.                 |
| `/api/films/{id}`      | PUT    | Update a film by ID.               |
| `/api/films/{id}`      | DELETE | Delete a film by ID.               |
| `/api/starships/`      | GET    | List all starships.                |
| `/api/starships/{id}`  | GET    | Retrieve a single starship by ID.  |
| `/api/starships/`      | POST   | Create a new starship.             |
| `/api/starships/{id}`  | PUT    | Update a starship by ID.           |
| `/api/starships/{id}`  | DELETE | Delete a starship by ID.           |

## Error Handling

The API provides detailed error handling, including:

- **404 Not Found**: Returned when a requested resource does not exist.
- **400 Bad Request**: Indicates a validation error with the client’s request.
- **500 Internal Server Error**: Catches unexpected server errors.
- **Custom Validation**: Specific validation errors are provided for detailed feedback, especially when creating or updating resources.

## API Documentation with Swagger and Redoc

The One With The Force API includes interactive API documentation with Swagger and Redoc:

- **Swagger UI**: Accessible at `/swagger/`, allowing interactive API testing.
- **Redoc**: Accessible at `/redoc/`, providing an alternative documentation interface.

## Linting and Testing

To ensure code quality and functionality, run the following commands:

- **Linting**: This project uses `pylint` to enforce coding standards. Run the following command to check for linting issues:

```bash
pylint api/ --fail-under=8
```

- **Running Tests**: This project uses pytest for running tests. Run the following command to execute all tests:

```bash
pytest --cov=api --cov-report=term-missing
```

## Running the Application Locally

After setup, run the application locally with:

```bash
python manage.py runserver
```

The application will be accessible at `http://localhost:8000`.

---

This API application leverages Django REST Framework to provide a structured, scalable, and well-documented API for Star Wars data, incorporating best practices in error handling, documentation, and testing to deliver a reliable and user-friendly experience.
