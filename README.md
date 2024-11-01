
# Company Course Management Platform

This project is a **Company Course Management System** designed to display and manage courses assigned to employees. The system allows employees to view their assigned courses and track their progress, while administrators manage the creation and assignment of courses.

## Table of Contents
- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Features](#future-features)
- [Contributors](#contributors)

## About the Project

The Course Management Platform provides a streamlined way for companies to assign training and development courses to their employees. Unlike typical course platforms where users enroll themselves, this system allows the company’s admin team to assign courses to specific employees.

Key Features:
- **Admin Functionality**: Admins can add, update, and delete courses. They also assign courses to employees.
- **Employee Functionality**: Employees can only view the courses assigned to them by the company and track their progress through each course.
- **Role-Based Access Control**: Admins manage courses and user assignments, while employees have a limited view to track their progress.

## Technologies Used

This project was built using the following technologies:

- **HTML**: Provides the structure for the web pages.
- **CSS**: Used for styling and layout.
- **JavaScript**: Adds dynamic interaction and functionality to the user interface.
- **Bootstrap**: A responsive framework that ensures the website is mobile-friendly and easy to navigate.
- **Django**: A robust Python web framework that handles the backend logic, including course management, user authentication, and database interaction.
- **Python**: Used for the backend logic and powering the Django framework.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/course-management-platform.git
   ```

2. Navigate to the project directory:
   ```bash
   cd course-management-platform
   ```

3. Install the Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create an admin user to manage the platform:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://localhost:8000` to view the application.

## Usage

- **Admin Users**:
  - Admin users can log in and access the admin dashboard to add, update, and delete courses.
  - Admins assign courses to employees based on their roles and needs. Employees cannot self-enroll.
  
- **Employee Users**:
  - Employees log in to view their assigned courses.
  - They can track progress on the courses and mark them as completed.

### Admin Workflow

1. Add new courses via the admin interface.
2. Assign courses to employees.
3. Track which employees have completed their assigned courses.

### Employee Workflow

1. Log in to view courses that have been assigned by the company.
2. Track your progress and mark courses as completed when done.

## Future Features

Planned future improvements include:
- **Notification System**: Notify employees when new courses are assigned.
- **Completion Certificates**: Generate certificates for employees who complete their courses.
- **Reporting Dashboard**: A dashboard for admins to track employee progress and course completion statistics.
- **Enhanced Course Content**: Support for multimedia (videos, quizzes) within courses to improve the learning experience.

## Contributors

This project was developed by:

- **Ramy Rashad**
- **Ahmed Elgendy**
- **Saged Ryan**
