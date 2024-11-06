# FastAPI Token Base

A Python project that implements a simple authentication system using **FastAPI** with token-based authentication. This project demonstrates how to secure API routes using tokens (e.g., OAuth2 or JWT) for authentication and authorization purposes.

## Features

- **Token Authentication**: Secures API endpoints using tokens, such as OAuth2 or JWT.
- **User Registration**: Allows users to register with a username and password.
- **User Login**: Allows users to log in and receive an authentication token.
- **Protected Routes**: Restricts access to certain routes, allowing only authenticated users to access them.
- **Token Validation**: Validates tokens for securing the routes and ensuring authenticated access.

## Requirements

- **Python 3.x**
- **FastAPI**
- **Pydantic** (for request validation)
- **Uvicorn** (for running the FastAPI application)
- **PyJWT** or **OAuth2** (for handling token encoding and decoding)
- **bcrypt** (for password hashing)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Fast_api_token_base.git
    cd Fast_api_token_base
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    To run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

### How to Use

1. **Register a User**: 
   - Send a POST request to `/register` with a `username` and `password`.
   - This will create a new user in the system.

2. **Login to Receive Token**:
   - Send a POST request to `/login` with the correct `username` and `password`.
   - The response will include a token.

3. **Access Protected Endpoints**:
   - Send a GET, POST, PUT, or DELETE request to the protected routes with the `Authorization` header containing the token:
     ```bash
     Authorization: Bearer your_token
     ```
   - This will grant access to restricted routes.

4. **Use Token for Authorization**:
   - Use the received token for subsequent requests to authorized routes, enabling secure access.

### Project Structure

- `main.py`: Contains the FastAPI application, routes, and token validation logic.
- `models.py`: Defines the database models using SQLAlchemy or any preferred ORM.
- `schemas.py`: Contains Pydantic models for request and response validation.
- `requirements.txt`: Lists necessary libraries like `FastAPI`, `PyJWT` or `OAuth2`, `bcrypt`, etc.

## Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.
