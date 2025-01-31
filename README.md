# FAQ Project - Django REST API with Redis Caching

This is a Django-based FAQ REST API that supports:
- **WYSIWYG Editor Support (CKEditor)**
- **Multi-language Translations (Google Translate)**
- **Redis Caching for Performance Optimization**
- **Django Admin Panel for Management**

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/gnanashekar2004/faq_project.git
cd faq_project
```

### 2. Create Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
# For Linux/macOS:
source myenv/bin/activate
# For Windows:
myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Apply Migrations & Create Superuser
```bash
python manage.py makemigrations faq_app
python manage.py migrate
python manage.py createsuperuser
```

### 4. Start Redis Server
```bash
redis-server
```

### 5. Run Django Server
```bash
python manage.py runserver
```

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/faqs/` | Fetch FAQs in English (default) |
| GET | `/api/faqs/?lang=hi` | Fetch FAQs in Hindi |
| GET | `/api/faqs/?lang=bn` | Fetch FAQs in Bengali |
| POST | `/api/faqs/` | Add a new FAQ |
| PUT | `/api/faqs/{id}/` | Update an FAQ |
| DELETE | `/api/faqs/{id}/` | Delete an FAQ |

## 📌 Example API Usage

### Fetch FAQs in English
```bash
curl http://127.0.0.1:8000/api/faqs/
```

### Fetch FAQs in Hindi
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

### Fetch FAQs in Bengali
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```