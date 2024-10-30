# Smart Cab Application

The Smart Cab application is a RESTful API for managing cab allocation and searching for nearby cabs. It utilizes JWT for authentication and Redis for caching cab locations, providing an efficient and secure solution for cab management.

## Features

- User authentication with JWT
- Cab allocation based on employee location
- Search for nearby cabs
- Caching of cab locations using Redis
- Generation of random real-time cab locations

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Flask-JWT-Extended**: Extension for Flask that provides JWT support.
- **Redis**: In-memory data structure store for caching.
- **Random**: Python module to generate random real-time locations.

## Installation

### Prerequisites

- Python 3.x
- Redis server

### Setup

1. **Clone the repository**:

   git clone https://your-repo-url.git
   cd smart-cab

2. **Install required packages**: 

    redis-server

Application Structure
app.py: Main application file containing the API endpoints.
auth.py: Handles user authentication.
cab_allocation.py: Manages cab allocation and searches for nearby cabs.
cache.py: Provides caching functionality for cab locations.
real_time_location.py: Simulates the generation of random real-time locations for cabs.
monitoring.py: (Assumed to handle logging events related to user actions).

API Endpoints
The Smart Cab application exposes several API endpoints for user authentication, cab allocation, and searching for nearby cabs. Below are the details for each endpoint:

Home Route
GET /
Description: Returns a welcome message.
Response:
    "Hello, Smart Cab!"

User Authentication

Login
POST /login
Description: Authenticates a user and returns an access token.

Request Body:
{
    "username": "your_username",
    "password": "your_password"
}

Response:
On success
{
    "access_token": "your_jwt_token"
}

On failure (invalid credentials):
{
    "msg": "Bad username or password"
}
Status Code: 401 Unauthorized

Cab Management

Allocate Cab
POST /allocate_cab
Description: Allocates a cab based on the employee's location.
Authorization: Requires JWT token.
Request Body:
{
    "employee_location": "x,y"  // Example: "10,20"
}
Response:
{
    "allocated_cab": "cab_id"  // e.g., "cab1"
}


Search Nearby Cabs
GET /search_nearby_cabs
Description: Searches for nearby cabs based on the employee's location.
Authorization: Requires JWT token.
Query Parameters:
location: A string in the format "x,y" (e.g., "10,20").
Response:
{
    "cabs": ["cab1", "cab2"]  // List of nearby cabs
}
