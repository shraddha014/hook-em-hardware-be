# hook-em-hardware-be
Hook'em Hardware is one stop hardware shop
This is the backend of our application.
Here is our Project Plan: https://docs.google.com/document/d/1kmE1pjdTlKd4LvHaeC_ubv213oRRwGWsRQKqEAKpi_s/edit?usp=sharing

Hook Em Hardware - Backend

Welcome to the backend repository for the Hook Em Hardware project! This backend system is designed to support the hardware management web application, enabling users to manage accounts, projects, and hardware checkouts/check-ins seamlessly. The backend handles all the core functionality, including user authentication, project management, and hardware resource tracking.

Project Overview
Hook Em Hardware is a comprehensive web application that streamlines the management of hardware resources. This backend is built using Flask and provides a RESTful API for the frontend to interact with. The backend handles requests related to user management, project management, and hardware operations, ensuring a smooth and efficient user experience.

Features
User Authentication: Securely create accounts, log in, and manage user sessions.
Project Management: Create, join, and manage multiple projects, enabling collaboration and resource management.
Hardware Management: Track hardware checkouts and check-ins, ensuring efficient resource utilization.
API Endpoints: Provides a set of RESTful endpoints for the frontend to interact with, supporting various operations like user registration, login, project creation, and hardware management.
Code Structure
The backend is organized into several modules, each handling different aspects of the application:

project_list.py: Manages the list of projects and related operations.
routes.py: Defines the routes for the API endpoints, linking frontend requests to backend operations.
create_projects.py: Handles the creation and management of projects within the system.
Register.py: Manages user registration and authentication.
hardware.py: Manages hardware checkouts and check-ins, tracking usage across projects.
login.py: Manages user login
API Endpoints
Here’s a summary of the key API endpoints provided by the backend:

User Authentication:
POST /register: Register a new user.
POST /login: Authenticate a user.
Project Management:
POST /create_project: Create a new project.
GET /projects: Retrieve the list of projects.
Hardware Management:
POST /checkout_hardware: Check out hardware for a project.
POST /checkin_hardware: Check in hardware to a project.
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.7 or later
Flask
pip (Python package manager)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/hook-em-hardware-backend.git
Navigate to the project directory:

bash
Copy code
cd hook-em-hardware-backend
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Project
Start the Flask development server:

bash
Copy code
flask run
Access the API locally:

The API will be accessible at http://localhost:5000.
Technologies Used
Flask: Python web framework for building the backend API.
SQLite: Database for storing user, project, and hardware data.
Python: The primary programming language for the backend.
Contributing
We welcome contributions to the project. Please fork the repository and submit a pull request with your proposed changes.

Fork the repository.
Create a new branch: git checkout -b my-new-feature.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin my-new-feature.
Submit a pull request.

Contributors
Karen Yin, Shraddha, Gowri Vasista, Alison Quan, Darren Ding, Jess Yang
