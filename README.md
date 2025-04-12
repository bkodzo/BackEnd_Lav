# Book Management API

A simple REST API for managing books, authors, and categories using Django and PostgreSQL.

## Features

- CRUD operations for Books, Authors, and Categories
- Filtering, searching, and ordering capabilities
- RESTful API endpoints with Django REST Framework
- PostgreSQL database integration

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Setup Instructions

### 1. Clone the repository

```bash
git clone ...
cd book_management_api
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

Create a PostgreSQL database named `book_management` with:
- Username: postgres
- Password: postgres
- Host: localhost
- Port: 5432

Or update the database settings in `book_project/settings.py` to match your configuration.

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/api/

## API Endpoints

- Authors: `/api/authors/`
- Categories: `/api/categories/`
- Books: `/api/books/`

## Filtering Examples

- Get books by a specific author: `/api/books/?author=1`
- Get books in a specific category: `/api/books/?categories=2`
- Search books by title: `/api/books/?search=django`
- Order books by price: `/api/books/?ordering=price` (use `-price` for descending)

## Admin Interface

Access the Django admin interface at http://127.0.0.1:8000/admin/ using your superuser credentials. 

## Development Branches

- `master`: Main production branch with stable features
- `altbranch`: Development branch for new features and testing 