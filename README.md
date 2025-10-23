# Phishing Portal

A Django-based phishing simulation platform with role-based access control, email tracking, and educational content.

## Features

- **Role-Based Access Control**: Admin, Instructor, and Recipient roles
- **Instructor Analytics Dashboard**: Real-time metrics and engagement tracking
- **Email Tracking System**: Track opens, clicks, reports, and landing page views
- **Educational Content**: Phishing awareness training pages
- **Docker Support**: Easy deployment with PostgreSQL database

## Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git (to clone the repository)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/roshan-raya/phishing-portal.git
   cd phishing-portal
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Web App: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

### Default Users

The application comes with pre-configured users:

**Admin User:**
- Username: `adminuser`
- Password: `ChangeMe123!`

**Instructor:**
- Username: `instructor1`
- Password: `Instructor123!`

**Recipient:**
- Username: `recipient1`
- Password: `Recipient123!`

## User Roles

### Admin
- Full system access
- User management
- System configuration

### Instructor
- Create and manage campaigns
- View analytics dashboard
- Track recipient engagement
- Monitor phishing simulation results

### Recipient
- Access educational content
- Report suspicious emails
- Complete phishing awareness training

## Project Structure

```
phishing-portal/
├── accounts/          # User authentication and roles
├── campaigns/         # Email templates and campaigns
├── recipients/        # Recipient lists and contacts
├── landing/          # Educational landing pages
├── tracking/         # Email tracking and analytics
├── dashboard/        # Role-based dashboards
├── templates/        # HTML templates
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Development

### Local Development (without Docker)

1. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL database**
   - Install PostgreSQL
   - Create database: `phishing_portal`
   - Update settings in `phishing_portal/settings.py`

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

## Docker Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Stop services
docker-compose down

# Rebuild containers
docker-compose up --build

# View logs
docker-compose logs -f
```

## Database

The application uses PostgreSQL with the following default settings:
- Database: `phishing_portal`
- User: `postgres`
- Password: `postgres`
- Host: `db` (Docker) or `localhost` (local)
- Port: `5432`

## Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME=phishing_portal
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
```

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change ports in docker-compose.yml
   ports:
     - "8001:8000"  # Use port 8001 instead
   ```

2. **Database connection issues**
   ```bash
   # Check if PostgreSQL container is running
   docker-compose ps
   
   # Restart database
   docker-compose restart db
   ```

3. **Permission issues**
   ```bash
   # Fix file permissions
   sudo chown -R $USER:$USER .
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please create an issue on GitHub.
