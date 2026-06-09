# Inventory Management System

A simple Inventory Management System built using Flask, PostgreSQL (Neon), SQLAlchemy, and Flask-Migrate.

## Features

- Add Products
- View Products
- Inventory Dashboard
- PostgreSQL Database (Neon)
- SQLAlchemy ORM
- Flask-Migrate Database Migrations
- Responsive Web Interface

---

## Project Structure

```text
inventory-management/
│
├── app.py
├── models.py
├── config.py
├── .env
├── requirements.txt
│
├── migrations/
│
├── templates/
│   ├── index.html
│   └── dashboard.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## Prerequisites

Install:

- Python 3.10+
- Git
- Neon PostgreSQL Account

---

## Clone Repository

```bash
git clone <repository-url>
cd inventory-management
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv env
```

Activate:

```bash
env\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv env
source env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is empty, install manually:

```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install python-dotenv
pip install psycopg2-binary
```

---

## Create a Neon Database

### Step 1: Create a Neon Account

Visit:

https://neon.tech

Create a free account and create a new project.

---

### Step 2: Copy Connection String

After creating the database, Neon provides a connection string similar to:

```text
postgresql://username:password@host/database?sslmode=require
```

Example:

```text
postgresql://neondb_owner:YOUR_PASSWORD@ep-example.us-east-1.aws.neon.tech/neondb?sslmode=require
```

Copy your own connection string.

---

## Create .env File

Create a file named:

```text
.env
```

Add:

```env
DATABASE_URL=postgresql://username:password@host/database?sslmode=require
```

Example:

```env
DATABASE_URL=postgresql://neondb_owner:YOUR_PASSWORD@ep-example.us-east-1.aws.neon.tech/neondb?sslmode=require
```

**Do not commit your .env file to GitHub.**

---

## Initialize Database

Run:

```bash
flask --app app db upgrade
```

This creates the required tables in the Neon PostgreSQL database.

---

## Run the Application

```bash
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

---

## Open in Browser

Inventory Page:

```text
http://127.0.0.1:5000/inventory
```

Dashboard:

```text
http://127.0.0.1:5000/dashboard-page
```

API Routes:

```text
http://127.0.0.1:5000/products
```

```text
http://127.0.0.1:5000/dashboard
```

---

## Database Migrations

Create a migration:

```bash
flask --app app db migrate -m "migration message"
```

Apply migration:

```bash
flask --app app db upgrade
```

---

## Technologies Used

- Flask
- PostgreSQL
- Neon Database
- SQLAlchemy ORM
- Flask-Migrate
- HTML
- CSS
- JavaScript

---

## Security Note

The `.env` file contains database credentials and should never be pushed to GitHub.

Add this to `.gitignore`:

```text
.env
env/
__pycache__/
```

---

## Author

Developed as an academic Inventory Management System project using Flask and PostgreSQL.
