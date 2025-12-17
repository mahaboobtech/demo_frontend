# VR App Study Management

This project is a web application designed to manage studies related to VR applications. It provides functionalities for handling user data, study configurations, certificates, announcements, and an admin dashboard.

## Setup Instructions

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.x**: Download and install from [python.org](https://www.python.org/downloads/).
*   **pip**: Python's package installer (usually comes with Python).

### 1. Clone the Repository

If you haven't already, clone the project repository to your local machine:

```bash
git clone https://github.com/mahaboobtech/demo_frontend.git
cd VR app study managment
```

### 2. Create a Virtual Environment (Recommended)

It's good practice to use a virtual environment to manage project dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

*   **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Apply database migrations to set up the database schema:

```bash
python manage.py migrate
```

You might also want to create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your superuser account.

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application should now be accessible in your web browser at `http://127.0.0.1:8000/`.
