"""
Script to list all available API endpoints in the project.
Run with: python api_endpoints.py
"""

import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_project.settings')
django.setup()

from django.urls import get_resolver
from django.core.management import call_command

def list_api_endpoints():
    """List all API endpoints in the project."""
    print("=" * 50)
    print("Book Management API - Available Endpoints")
    print("=" * 50)
    
    print("\n## Basic API Endpoints:")
    print("- Authors List/Create: http://127.0.0.1:8000/api/authors/")
    print("- Author Detail/Update/Delete: http://127.0.0.1:8000/api/authors/{id}/")
    print("- Categories List/Create: http://127.0.0.1:8000/api/categories/")
    print("- Category Detail/Update/Delete: http://127.0.0.1:8000/api/categories/{id}/")
    print("- Books List/Create: http://127.0.0.1:8000/api/books/")
    print("- Book Detail/Update/Delete: http://127.0.0.1:8000/api/books/{id}/")
    
    print("\n## Filtering Examples:")
    print("- Get books by author: http://127.0.0.1:8000/api/books/?author=1")
    print("- Get books by category: http://127.0.0.1:8000/api/books/?categories=2")
    print("- Get published books: http://127.0.0.1:8000/api/books/?is_published=true")
    
    print("\n## Search Examples:")
    print("- Search books by title: http://127.0.0.1:8000/api/books/?search=django")
    print("- Search authors by name: http://127.0.0.1:8000/api/authors/?search=martin")
    
    print("\n## Ordering Examples:")
    print("- Order books by title: http://127.0.0.1:8000/api/books/?ordering=title")
    print("- Order books by price (descending): http://127.0.0.1:8000/api/books/?ordering=-price")
    
    print("\n## Admin Interface:")
    print("- Admin login: http://127.0.0.1:8000/admin/")
    
    print("\n" + "=" * 50)
    print("To test these endpoints, first run the server with:")
    print("python manage.py runserver")
    print("=" * 50)

if __name__ == "__main__":
    list_api_endpoints() 