Resume Management System

This is a **Resume Management System** built with **Django** for the backend and **React** for the frontend. It allows users to upload, view, and delete resumes.

## Features

- **Upload resumes**: Users can upload their resumes in PDF format.
- **View resumes**: View a list of uploaded resumes with user details such as name, email, phone number, and skills.
- **Delete resumes**: Admin can delete uploaded resumes.

## Installation Instructions

Follow the instructions below to set up and run the project.

### Backend (Django)

Create a virtual environment and activate it:
python3 -m venv venv
venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py migrate

Start the Django development server:
python manage.py runserver
The backend will be running at http://localhost:8000.

###Frontend (React)

Install dependencies:
npm install

Run the React application:
npm start
The frontend will be running at http://localhost:3000

API Endpoints
The backend provides the following API endpoints:
GET /api/resumes/: Fetch all uploaded resumes.
POST /api/resumes/: Upload a new resume.
DELETE /api/resumes/{id}/: Delete a resume by its ID.

Dependencies
Backend (Django):
Django
Django REST Framework
Other dependencies specified in requirements.txt

Frontend (React):
React
Axios (for making API requests)
Other dependencies specified in package.json

How to Use the Application

Upload Resume: You can upload a resume by clicking the "Upload" button on the frontend, which will allow you to select a PDF file to upload.
View Resumes: All uploaded resumes will be displayed in a list, showing the user’s name, email, phone, and skills.
Delete Resume: You can delete a resume by clicking the "Delete" button next to the resume you want to remove.

