
# Django Unfold Boilerplate

A clean and well-structured Django boilerplate built with [django-unfold](https://unfoldadmin.com/) for the admin panel and [DevBook Theme](https://github.com/xriley/DevBook-Theme) for the landing page. This project is designed to provide a solid foundation for building Django applications with a clean architecture.

## Features
- **Admin Panel**: Powered by django-unfold for a modern and sleek admin experience.
- **Landing Page**: Uses the DevBook theme for a professional and responsive frontend.
- **Task Queue**: Integrated with Celery for background job processing.
- **Database Support**: PostgreSQL with `psycopg2-binary`.
- **Extra Utilities**: Includes common Django extensions and type hinting support.

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL
- Docker (optional, for containerized deployment)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/vsnasc/django-unfold-boilerplate.git
   cd django-unfold-boilerplate
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Configure environment variables (e.g., `.env` file or export manually):
   ```env
   cp env.example env.dev
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - Admin panel: `http://127.0.0.1:8000/admin/`
   - Landing page: `http://127.0.0.1:8000/`

## Running with Docker
To use Docker, run:
```bash
docker-compose up --build
```

## Folder Structure
```
.
├── Dockerfile
├── README.md
├── app
│   ├── admin
│   ├── management
│   ├── migrations
│   ├── models
│   ├── tasks
│   ├── templates
│   ├── views
├── project
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
├── static
├── docker-compose.yml
├── manage.py
└── requirements.txt
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

