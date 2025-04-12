# Django Blog Project

A blog application built with Django 5.1.7. This project allows users to create, edit, and publish blog posts.

## Features

- Blog post creation and management
- Admin interface for content management
- User authentication
- Responsive design

## Requirements

- Python 3.12+
- Django 5.1.7
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd Django_Blog
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000/admin/ to access the admin interface.

## Project Structure

- `blog/` - The main blog application
- `mysite/` - Project settings and configuration
- `manage.py` - Django's command-line utility for administrative tasks

## Contributing

Feel free to fork the project and submit pull requests.

## License

This project is open source and available under the [MIT License](LICENSE). 