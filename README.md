Here's the updated README with the detailed API documentation included:

---

# Django Project

Welcome to the Django Project repository! This project provides a RESTful API for managing clients and their associated projects. You can interact with the API endpoints using the provided [Postman collection](https://app.getpostman.com/join-team?invite_code=30ba54f70aa76d222fa87e1cc99a09d9&target_code=8d2b7e6de73a907e3969c7b95cd91458).

## Features

- Manage clients with their details.
- Assign projects to clients and users.
- Retrieve and update client and project data.

## Prerequisites

- Python 3.8+
- Django 4.x
- PostgreSQL or any other preferred database (adjust settings in `settings.py`)
- Optional: Docker for containerized deployment

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/001AM/nimap.git
   cd machinetest
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Update `DATABASES` in `settings.py` as needed.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

   The server will be running at `http://127.0.0.1:8000`.

## API Endpoints

The following API endpoints allow interaction with the clients and projects in this Django project:

### Clients

- **List of All Clients**

  **GET** `/clients/`

  **Response:**
  ```json
  [
    {
      "id": 1,
      "client_name": "Nimap",
      "created_at": "2019-12-24T11:03:55.931739+05:30",
      "created_by": "Rohit"
    },
    {
      "id": 2,
      "client_name": "Infotech",
      "created_at": "2019-12-24T11:03:55.931739+05:30",
      "created_by": "Rohit"
    }
  ]
  ```

- **Create a New Client**

  **POST** `/clients/`

  **Request Body:**
  ```json
  {
    "client_name": "company A"
  }
  ```

  **Response:**
  ```json
  {
    "id": 3,
    "client_name": "company A",
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Rohit"
  }
  ```

- **Retrieve Client Info with Projects**

  **GET** `/clients/:id`

  **Response:**
  ```json
  {
    "id": 2,
    "client_name": "Infotech",
    "projects": [
      {
        "id": 1,
        "name": "project A"
      }
    ],
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Rohit",
    "updated_at": "2019-12-24T11:03:55.931739+05:30"
  }
  ```

- **Update Client Info**

  **PUT/PATCH** `/clients/:id`

  **Request Body:**
  ```json
  {
    "client_name": "company A"
  }
  ```

  **Response:**
  ```json
  {
    "id": 3,
    "client_name": "company A",
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Rohit",
    "updated_at": "2019-12-24T11:03:55.931739+05:30"
  }
  ```

- **Delete a Client**

  **DELETE** `/clients/:id`

  **Response:** 204 No Content

---

### Projects

- **Create a New Project**

  **POST** `/projects/`

  **Request Body:**
  ```json
  {
    "project_name": "Project A",
    "client_id": 1,
    "users": [1]
  }
  ```

  **Response:**
  ```json
  {
    "id": 3,
    "project_name": "Project A",
    "client": "Nimap",
    "users": [
      {
        "id": 1,
        "name": "Rohit"
      }
    ],
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "Ganesh"
  }
  ```

- **List of All Projects Assigned to the Logged-in User**

  **GET** `/projects/`

  **Response:**
  ```json
  [
    {
      "id": 1,
      "project_name": "Project A",
      "client_name": "Client A",
      "created_at": "2019-12-24T11:03:55.931739+05:30",
      "created_by": "Ganesh"
    },
    {
      "id": 2,
      "project_name": "Project B",
      "client_name": "Client B",
      "created_at": "2019-12-24T11:03:55.931739+05:30",
      "created_by": "Ganesh"
    }
  ]
  ```

---

## Postman Collection

To test the API endpoints, you can use the provided Postman collection:

- [**Postman Collection Link**](https://app.getpostman.com/join-team?invite_code=30ba54f70aa76d222fa87e1cc99a09d9&target_code=8d2b7e6de73a907e3969c7b95cd91458)

   This collection includes all the API endpoints with example requests and responses. Simply import the link above into your Postman workspace to start testing.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This updated README now includes comprehensive API documentation, installation instructions, and how to interact with the project using the Postman collection link. Let me know if you'd like further adjustments!
