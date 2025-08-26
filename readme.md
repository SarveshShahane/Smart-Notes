# Django Notes App

A simple Django-based Notes Application with full CRUD (Create, Read, Update, Delete) functionality and a built-in search feature.

## Features
- Create, view, update, and delete notes
- Search notes by keywords or tags
- Responsive and modern UI with Bootstrap
- Flash messages for user feedback

## Getting Started

### Prerequisites
- Python 3.8+
- Django 4.x or 5.x

### Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory:
   ```sh
   cd "Notes App/notes_app"
   ```
3. Install dependencies:
   ```sh
   pip install django
   ```
4. Run migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Open your browser and go to `http://127.0.0.1:8000/`

## Usage
- Use the navigation bar to create a new note, search, or view all notes.
- Edit or delete notes directly from the home page.

## Project Structure
```
notes_app/
├── notes/                # Django app for notes
│   ├── models.py         # Note model
│   ├── views.py          # Views for CRUD and search
│   ├── urls.py           # App URLs
│   └── templates/notes/  # HTML templates
├── notes_app/            # Project settings
│   ├── settings.py
│   └── urls.py
├── templates/            # Base templates
│   └── base.html
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
```

## License
This project is licensed under the MIT License.
