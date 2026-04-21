from flask import Flask, make_response
from flask_migrate import Migrate

from models import Exercise, WorkoutExercises, Workout, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here
@app.route('/workouts', methods=['GET']):
def list_workouts():
    pass
    # Function returns a list of workouts

@app.route('/workouts/<int:id>', methods=['GET']):
def list_workout(id):
    pass
    # This function returns a workout based on the returned id.

@app.route('/workouts/<int:id>', methods=['POST']):
def create_workout():
    pass
    # Function creates a workout.

@app.route('/exercises', methods=['GET']):
def list_exercises():
    pass
    # Function lists all exercises.

@app.route('/exercises/<int:id>', methods=['GET']):
def list_exercise(id):
    pass
    # Function shows an exercises and its associated workouts.

@app.route('/exercises', methods=['POST']):
def create_exercise():
    pass
    # Function creates an exercise.


@app.route('workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=['POST']):
def add_exercise_to_workout(workout_id, exercise_id):
    pass
    # Function adds an exercise to a workout, including reps/sets/duration

if __name__ == '__main__':
    app.run(port=5555, debug=True)