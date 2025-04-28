# WorkScholar Management System

## System Overview
WorkScholar is a Django-based web application designed to manage work-study programs. The system handles student workers, supervisors, and administrative tasks related to work schedules, time tracking, and payment management.

## System Architecture

### Backend Components
1. **User Management** (`accounts` app)
   - Custom User model with different role types:
     - Student Workers
     - Work Supervisors
     - Working Student Director
     - Administrator
   - Authentication and authorization system
   - Profile management

2. **Core Features**
   - Work Schedule Management
   - Time Sheet Tracking
   - Work Assignments
   - Notification System
   - Department Management

3. **Database**
   - SQLite3 (development)
   - Models include:
     - User
     - WorkSchedule
     - WorkAssignment
     - TimeSheet
     - Notification
     - LoginBackground

## Running Without Python Dependencies (Docker Setup)

### Prerequisites
- Docker
- Docker Compose

### Quick Start with Docker

1. **Create a Dockerfile in the root directory**
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

2. **Create a docker-compose.yml**
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
```

3. **Create a requirements.txt**
```
Django>=5.1.3
```

### Running the Application

1. **Build and start the container:**
```bash
docker-compose up --build
```

2. **Access the application:**
- Open a web browser and navigate to `http://localhost:8000`

3. **First-time setup:**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## System Structure

```
├── accounts/              # Main application directory
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── forms.py          # Form definitions
│   └── templates/        # HTML templates
├── static/               # Static files (CSS, JS, images)
├── media/               # User-uploaded files
└── workscholar/         # Project settings directory
    ├── settings.py      # Project settings
    └── urls.py          # URL configurations
```

## Features and Endpoints

1. **Authentication**
   - Login: `/accounts/login/`
   - Logout: `/accounts/logout/`
   - Password Reset: `/accounts/password_reset/`

2. **Dashboards**
   - Student Dashboard: `/dashboard/student/`
   - Supervisor Dashboard: `/dashboard/supervisor/`
   - Admin Dashboard: `/django-admin/`

3. **Work Management**
   - Time Sheets
   - Schedule Management
   - Work Assignments

## Security Considerations

- CSRF protection enabled
- Session security settings configured
- Secure cookie handling
- Password validation rules implemented
- User authentication required for sensitive operations

## Backup and Maintenance

1. **Database Backup**
```bash
docker-compose exec web python manage.py dumpdata > backup.json
```

2. **Restore Database**
```bash
docker-compose exec web python manage.py loaddata backup.json
```

## Troubleshooting

1. **Container Issues**
   - Check logs: `docker-compose logs`
   - Restart containers: `docker-compose restart`

2. **Database Issues**
   - Reset migrations: `docker-compose exec web python manage.py migrate`
   - Clear database: Remove db.sqlite3 and run migrations again

## Support
For technical support or questions, please create an issue in the repository.