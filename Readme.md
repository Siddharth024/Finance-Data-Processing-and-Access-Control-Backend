# Finance Backend Assignment

Backend system for a finance dashboard that manages users, financial records, and analytics.
The project emphasizes clean architecture, scalability, and role-based access control (RBAC).

## Overview

The system allows different user roles to interact with financial data based on permissions and provides aggregated insights for dashboard visualization.

## Tech Stack

- Framework: FastAPI
- Database: MongoDB (Motor async driver)
- Authentication: JWT (access-token based)
- Validation: Pydantic
- Password Security: Bcrypt (Passlib)

## Key Features

### 1. User Management

- Create and manage users
- Role-based system:
  - Admin: Full access
  - Analyst: Read access + analytics access
  - Viewer: Read-only access
- User status management (active/inactive)

### 2. Authentication and Authorization

- JWT-based authentication
- Secure login flow
- Role-based access control via FastAPI dependencies

### 3. Financial Records Management

- Create, update, and delete financial records
- Record fields include:
  - Amount
  - Type (income/expense)
  - Category
  - Date
  - Notes
- Filtering support:
  - By type
  - By category
  - By date range
- Pagination support

### 4. Dashboard Analytics

- Total income
- Total expenses
- Net balance
- Category-wise breakdown
- Recent transactions
- Optional date filtering

Dashboard metrics are computed efficiently using MongoDB aggregation pipelines.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd Finance-backend-assignment
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
MONGO_URL=your_mongodb_connection_string
DB_NAME=finance_db
SECRET_KEY=your_secret_key
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Authentication Flow

1. Create a user (Admin recommended)
2. Login using `/auth/login`
3. Receive JWT access token
4. Use the token in Swagger Authorize as:

```text
Bearer <your_token>
```

## Role-Based Access Control

| Action | Viewer | Analyst | Admin |
| --- | --- | --- | --- |
| View Records | Yes | Yes | Yes |
| Create Records | No | No | Yes |
| Update/Delete Records | No | No | Yes |
| Dashboard Access | No | Yes | Yes |

## Example Dashboard Response

```json
{
  "summary": {
    "total_income": 50000,
    "total_expense": 20000,
    "net_balance": 30000
  },
  "category_breakdown": [
    { "category": "food", "total": 5000 },
    { "category": "rent", "total": 10000 }
  ],
  "recent_transactions": []
}
```

## Design Decisions

- FastAPI for async performance and automatic validation
- MongoDB for flexible schema and aggregation capabilities
- Service-layer architecture for separation of concerns
- Dependency injection for RBAC
- Aggregation pipelines for dashboard analytics

## Assumptions

- Single-tenant system (no organization separation)
- Basic authentication (no refresh-token flow)
- No frontend included
- Focus is on backend design and logic

## Possible Improvements

- Refresh-token mechanism
- Advanced analytics (monthly trends, forecasting)
- Unit and integration tests
- Docker containerization
- Rate limiting and caching

## Author

Siddharth Chaudhary

## Conclusion

This project demonstrates solid backend design principles including API structuring, RBAC, data validation, and efficient aggregation. The focus is on clean, maintainable, and logically structured implementation.
