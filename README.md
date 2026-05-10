# 🛒 PhiMart - Django REST Framework eCommerce API

![Django](https://img.shields.io/badge/Django-Framework-green)
![DRF](https://img.shields.io/badge/DRF-REST_API-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![Swagger](https://img.shields.io/badge/API-Documentation-brightgreen)

PhiMart is a scalable and production-ready eCommerce REST API built using Django REST Framework (DRF).  
The project follows clean architecture principles and includes JWT authentication, cart management, order processing, reviews & ratings, pagination, custom permissions, service-layer architecture, and API documentation using Swagger.

Designed with maintainability and scalability in mind, PhiMart demonstrates backend engineering practices commonly used in modern eCommerce systems.

---

# 🚀 Features

## 🔐 Authentication & Authorization
- JWT Authentication using Djoser + Simple JWT
- User Registration & Login
- Token Refresh System
- Role-based Access Control
- Custom Permission Classes

## 🛍️ Product Management
- Product CRUD APIs
- Category-based Products
- Product Images
- Product Filtering & Searching
- Pagination Support

## 🛒 Cart System
- Create Cart
- Add/Update/Delete Cart Items
- Persistent Cart Functionality
- Cart Total Calculation

## 📦 Order Management
- Place Orders
- Order Item Management
- Order History
- Admin Order Control

## ⭐ Reviews & Ratings
- Product Reviews
- Rating System
- Validation for Rating Limits

## ⚙️ Architecture & Backend Features
- Service Layer Architecture
- Signals Implementation
- Custom Pagination
- Custom Permissions
- Serializer Validations
- Environment Variable Management
- PostgreSQL Database Integration

## 📄 API Documentation
- Swagger UI
- OpenAPI Documentation with drf_yasg

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Django | Backend Framework |
| Django REST Framework | REST API Development |
| PostgreSQL | Database |
| Djoser | Authentication Management |
| Simple JWT | JWT Authentication |
| drf_yasg | Swagger Documentation |
| Decouple | Environment Variable Management |
| Vercel | Deployment |

---
# 📁 Project Structure

```bash
phi_mart/
│
├── .phi_env/                  # Virtual environment
├── api/                       # API configuration and routing
├── fixtures/
│   └── product_data.json      # Sample product fixture data
│
├── media/                     # Uploaded media files
├── order/                     # Cart and order management app
├── phi_mart/                  # Main project settings folder
├── product/                   # Product and category management app
├── users/                     # User authentication and management app
│
├── .env                       # Environment variables
├── .gitignore
├── manage.py
└── requirements.txt
```

# ⚡ Installation & Setup

Follow these steps to set up the PhiMart project locally on your machine.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/phi_mart.git
cd phi_mart
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .phi_env
.phi_env\Scripts\activate
```

### Linux / MacOS

```bash
python3 -m venv .phi_env
source .phi_env/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory and add the following variables:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

---

## 4️⃣ PostgreSQL Database Setup

Create a PostgreSQL database matching the credentials provided in your `.env` file.

Example:

```sql
CREATE DATABASE phimart_db;
```

---

## 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Load Fixture Data (Optional)

To populate the database with sample product data:

```bash
python manage.py loaddata fixtures/product_data.json
```

---

## 7️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 8️⃣ Run Development Server

```bash
python manage.py runserver
```

The application will be available at:

```bash
http://127.0.0.1:8000/
```

---

# 📚 API Documentation

## Swagger UI

```bash
http://127.0.0.1:8000/swagger/
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc/
```

# 🔒 Permissions & Security

PhiMart implements multiple security and access control mechanisms to ensure secure API communication and protected resources.

### Security Features
- JWT Authentication using Djoser + Simple JWT
- Token Refresh & Verification System
- Protected API Endpoints
- Custom Permission Classes
- Role-based Authorization
- Secure Environment Variable Management using `.env`
- Serializer-level Data Validation
- Authentication-required Order & Cart Operations
- Admin-only Product Management APIs

---

# 🌍 Deployment

The PhiMart API is deployed on **Vercel** for fast and reliable hosting.

### Deployment Features
- Production-ready configuration
- Environment variable support
- PostgreSQL database integration
- Static & media handling support
- Scalable REST API architecture

---

# 📈 Future Improvements

The project is actively evolving, and several advanced features are planned for future releases.

### Planned Features
- Online Payment Gateway Integration
- Wishlist Functionality
- Coupon & Discount System
- Inventory & Stock Management
- Email Notifications
- Product Recommendation System
- API Rate Limiting & Throttling
- Docker Containerization
- CI/CD Pipeline Integration
- Redis-based Caching
- Async Task Processing with Celery

---

# 👨‍💻 Author

## Najim Ullah Rifat

Backend Developer focused on building scalable web applications using Django and Django REST Framework.

### Skills
- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- API Development
- Backend Architecture

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for personal and commercial purposes.