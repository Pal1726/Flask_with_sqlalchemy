
# Blog-Project-by-Flask with SQLalchemy
#project overview
This Flask application, built with SQLAlchemy and MySQL, enables users to register, log in, and manage posts. Users can create, edit, and delete their own posts while enjoying a secure and personalized experience. It combines robust authentication and efficient database management to deliver a seamless, user-friendly blogging platform.

## Table of Contents

1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Database Initialization and Configuration](#database-initialization-and-configuration)
7. [Running the Application](#running-the-application)
8. [Functionalities](#functionalities)

## Introduction

Register as a new user.
Log in securely with authentication.
Create new posts.
Edit your own posts.
Delete posts you’ve created.
Manage a personalized user experience.
Efficiently handle data with SQLAlchemy and MySQL integration.
Experience a simple and user-friendly interface.


## Technology Stack

### Frontend

- HTML
- CSS

### Backend

- Python
- Flask (Web Framework)
- MySQL (Database)
- SQLalchemy(python sql toolkit)

## Project Structure

The project directory includes the following files and directories:

- `__init__.py`: Initializes the Flask application with SQLAlchemy, configures the MySQL database, sets up blueprints for authentication and blog features, and ensures the instance folder exists.
- `db.py`: Manages database operations, including getting a database session, closing it, and initializing tables. It also provides CLI commands to reset and initialize the database, integrating with 
 Flask's lifecycle.
-`auth.py`: Manages user authentication, including registration, login, and logout. It uses SQLAlchemy for database queries, securely hashes passwords, tracks logged-in users, and includes a `login_required` decorator to protect views.
- `blog.py`: Handles blog post management, including displaying posts, creating new posts, updating existing ones, and deleting posts. It uses SQLAlchemy for database operations, integrates user authentication, and protects routes with a `login_required` decorator.
- `models.py`: Defines database models using SQLAlchemy. Includes `User` for storing user credentials and associating users with posts, and `Post` for storing blog post details with a relationship to the user who created them.

##### Directory 
- `templates` : This directory contain all the HTML files.
- `static` : This directory contain CSS and image files.

## Prerequisites

Before proceeding with the installation and execution of the application, ensure you have the following dependencies installed on your system:

- Python 3.x
- Git
- MySQL server installed and running.

## Installation

1. Clone the GitHub repository to your desired location:

   ```bash
   https://github.com/Pal1726/flaskr_sqlalchemy.git
   ```

2. Navigate to the  directory:

   ```bash
   cd flaskr_sqlalchemy

   ```
3. Then activate the virtual environment:

   ```bash
   . .venv/bin/activate
   ```
 
4. Install the required packages and libraries by executing:

   ```bash
   pip install -r requirements.txt
   ```

5. If you're encountering an error in installing requirements.txt then do this:
   ```bash
   sudo apt install libmysqlclient-dev
   ```
## Database Initialization and Configuration

Before running the application, it's essential to initialize the database and configure the connection. Follow these steps:

1. Import the database schema by running the SQL script (`schema.sql`) provided in the repository. This script will set up the required tables and initial data.
##### (a) Using MySQL Interpreter

1. **Login to MySQL Interpreter**

    ```bash
    mysql -u root -p
    ```
    
4. **Import the SQL script**

    ```sql
    source /path/to/schema.sql;
    ```


#### After importing the database, update the database configuration as mentioned in the next step.    

3. Update the MySQL database configuration in the `__init__.py` file. Open `__init__.py` and provide your MySQL database connection details as follows:

   ```python
   db_config = {
       "host": "your_database_host",
       "user": "your_database_user",
       "password": "your_database_password",
       "database": "your_database_name"
   }
   ```

   Save the changes.



## Running the Application


Navigate out of this directory:
```bash
  cd ..
   ```

To launch the application, execute the following command:

   ```bash
   export FLASK_APP=flaskr_sqlalchemy
   export FLASK_ENV=development
   flask run
   ```

This command will start the Flask development server, and you can access the Blog Application in your web browser at http://localhost:5000.

## Functionalities

The Blog Application offers the following essential functionalities:

1.User Registration
2.User login
3.Create Posts
4.View Posts
5.Edit Posts
6.Delete Posts
7.Authorization
8.Error Handling
9.Database Management
10.Command-Line Utility

Users can easily perform CRUD operations on these components, enabling them to add, view, update, or delete entries as necessary.

