# HNG12 Stage 0 API

## Overview
This is a simple public API built with Django Rest Framework (DRF) for the HNG12 Stage 0 task. It provides a JSON response containing:
- Your registered email (used for HNG12 Slack registration)
- The current datetime in ISO 8601 format (UTC)
- The GitHub repository URL of this project

## Tech Stack
- **Backend:** Django Rest Framework (DRF)
- **Documentation:** Swagger UI (drf-yasg)
- **Deployment:** (To be added after deployment)
- **CORS Handling:** Enabled using `django-cors-headers`

## API Endpoint
### Base URL: `https://hng-12-be-track-s0.onrender.com/`

### GET `/`
#### Response Format:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

### Swagger Documentation
- Available at: `https://hng-12-be-track-s0.onrender.com/swagger/`

## Installation & Setup

### Prerequisites
Ensure you have Python and pip installed on your system.

### Clone the Repository
```bash
git clone https://github.com/Benji918/HNG-12-BE-TRACK-S0.git
cd your-repo
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Server
```bash
python manage.py runserver
```

### Access the API
- Open `http://127.0.0.1:8000/swagger/` for API documentation and Response.

## Deployment Guide
You can deploy the API on platforms like **Render, Railway, or Vercel**.

### Deployment Steps:
1. Push your project to a public GitHub repository.
2. Choose a hosting platform (e.g., Render, Railway, Vercel, etc.).
3. Follow the platform’s deployment guide for Django applications.
4. Ensure the API URL is publicly accessible and update the README with the deployed link.

## Backlinks
- [Hire Python Developers](https://hng.tech/hire/python-developers)


## License
This project is licensed under the MIT License.

