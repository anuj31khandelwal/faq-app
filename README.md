# Multilingual FAQ System

A Django-based FAQ management system with multilingual support, WYSIWYG editor integration, and automatic translation capabilities.

## Features 🚀

- Multi-language support (English, Hindi, Bengali)
- WYSIWYG editor for rich text formatting
- Automatic translation using Google Translate API
- Redis-based caching for improved performance
- RESTful API with language selection
- Docker support for easy deployment
- Comprehensive admin interface

## Technical Stack

- **Backend**: Django 5.0.2
- **API**: Django REST Framework 3.14.0
- **Editor**: CKEditor
- **Cache**: Redis
- **Translation**: Google Translate API
- **Containerization**: Docker & Docker Compose

## Quick Start 🚀

### Using Docker

1. Clone the repository:
```bash
git clone https://github.com/yourusername/faq-system.git
cd faq-system
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

3. Build and run with Docker:
```bash
docker-compose up --build
```

4. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## API Documentation 📚

### Endpoints

#### List FAQs
```bash
GET /api/faqs/
```

Parameters:
- `lang`: Language code (en, hi, bn)
- `search`: Search query

Example:
```bash
# Get FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi

# Search FAQs
curl http://localhost:8000/api/faqs/?search=django
```

#### Get Single FAQ
```bash
GET /api/faqs/{id}/
```

Example Response:
```json
{
    "id": 1,
    "question": "What is Django?",
    "answer": "Django is a high-level Python web framework...",
    "created_at": "2024-02-02T10:00:00Z",
    "updated_at": "2024-02-02T10:00:00Z",
    "language": "en"
}
```

#### Create FAQ
```bash
POST /api/faqs/
```

Request Body:
```json
{
    "question": "What is Django?",
    "answer": "Django is a web framework..."
}
```

## Running Tests 🧪

```bash
# Run all tests
pytest

# Run with coverage
coverage run -m pytest
coverage report
```

## Contributing 🤝

1. Fork the repository
2. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes following conventional commits:
```bash
git commit -m "feat: Add new feature"
git commit -m "fix: Fix bug in translation"
git commit -m "docs: Update API documentation"
```

4. Push to your branch and create a Pull Request

### Commit Convention

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation updates
- `style:` Code style changes
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

## Deployment 🚀

### Heroku Deployment

1. Install Heroku CLI
2. Login to Heroku:
```bash
heroku login
```

3. Create Heroku app:
```bash
heroku create your-app-name
```

4. Add Redis add-on:
```bash
heroku addons:create heroku-redis:hobby-dev
```

5. Configure environment variables:
```bash
heroku config:set DJANGO_SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
```

6. Deploy:
```bash
git push heroku main
```


