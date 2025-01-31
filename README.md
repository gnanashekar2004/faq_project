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

### 4. Install and Start Redis Server

#### For Windows:
1. Download Redis for Windows from [Github Releases](https://github.com/microsoftarchive/redis/releases)
2. Extract the downloaded `.zip` file to a permanent location (e.g., `C:\Redis`)
3. Add Redis to System PATH:
   - Right-click on 'This PC' or 'My Computer'
   - Click 'Properties'
   - Click 'Advanced system settings'
   - Click 'Environment Variables'
   - Under 'System Variables', find and select 'Path'
   - Click 'Edit'
   - Click 'New'
   - Add the full path to your Redis folder (e.g., `C:\Redis`)
   - Click 'OK' on all windows to save changes
   - **Restart any open Command Prompt or terminal windows**

4. Verify installation by opening a new Command Prompt and running:
```cmd
redis-server
```
You should see logs indicating Redis has started on `127.0.0.1:6379`

#### For Linux (Ubuntu/Debian):
```bash
# Update package list
sudo apt update

# Install Redis
sudo apt install redis-server

# Start Redis service
sudo systemctl start redis
```

#### For macOS:
```bash
# Using Homebrew
brew install redis

# Start Redis service
brew services start redis
```

### 5. Run Django Server
```bash
python manage.py runserver
```

### 6. Access Admin Interface
- Visit `http://127.0.0.1:8000/admin` in your browser
- Log in with your superuser credentials created in step 3
- Use the WYSIWYG editor to create and manage FAQs through a user-friendly interface

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