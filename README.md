# Flask SQLAlchemy Workout Application Backend

## Description
This repository is a submission created for the submission: <br> [Link to assigment](https://moringa.instructure.com/courses/1389/assignments/87555).

The workout application is built using the following libraries:
- Flask = "2.2.2"
- Flask-Migrate = "3.1.0"
- flask-sqlalchemy = "3.0.3"
- Werkzeug = "2.2.2"
- importlib-metadata = "6.0.0"
- importlib-resources = "5.10.0"
- ipdb = "0.13.9"
- marshmallow = "3.20.1"

In the shortest words possible: <br>
**The Flask application enables users to `track workouts` and their `associated exercises`.**

# Relations
It is built on a relational database with 3 tables:
- Exercise: To track individual exercises
- Workout: To track workouts
- WorkoutExercises: The junction table linking the `Workout table` to the  `Exercise table`.

## Installation steps.

Remember to switch to a **virtual environment**, such as `venv`.
### 1. Install dependencies
```bash
pipenv install
pipenv shell
```

### 2. Change the directory to the server
```bash
cd server
```

### 2. Set up the database
Run these commands in the terminal
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 3. Seed the database
```bash
python seed.py
```

To run the app, type:
```bash
python app.py
or 
flask run
```
in the terminal.

Once the Flask app is running, you can check the routes defined to view the data stored.
---

Routes defined include: 
---
### `GET /workouts`
Returns a list of all workouts.

### `GET /workouts/<int:id>`
Returns a single workout by ID.

### `POST /workouts`
Creates a new workout.



## Exercise Routes

### `GET /exercises`
Returns a list of all exercises.

### `GET /exercises/<int:id>`
Returns a single exercise by ID along with its associated workouts.

### `POST /exercises`
Creates a new exercise.

## Workout Exercise Routes

### `POST /workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises`
Adds an exercise to a workout with optional reps, sets, and duration.

