from flask import Flask, make_response, request
from flask_migrate import Migrate
from marshmallow import ValidationError

from models import Exercise, WorkoutExercises, Workout, db
from schemas import ExerciseSchema, WorkoutSchema, WorkoutExercisesSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
workout_exercises_schema = WorkoutExercisesSchema()

# Define Routes here
@app.route('/workouts', methods=['GET'])
def list_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts), 200)


@app.route('/workouts/<int:id>', methods=['GET'])
def list_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response({"error": "Workout not found."}, 404)
    return make_response(workout_schema.dump(workout), 200)


@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    try:
        workout = workout_schema.load(data, session=db.session)
        db.session.add(workout)
        db.session.commit()
        return make_response(workout_schema.dump(workout), 201)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 400)


@app.route('/exercises', methods=['GET'])
def list_exercises():
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)


@app.route('/exercises/<int:id>', methods=['GET'])
def list_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return make_response({"error": "Exercise not found."}, 404)
    return make_response(exercise_schema.dump(exercise), 200)


@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    try:
        exercise = exercise_schema.load(data, session=db.session)
        db.session.add(exercise)
        db.session.commit()
        return make_response(exercise_schema.dump(exercise), 201)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 400)


@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if not workout:
        return make_response({"error": "Workout not found."}, 404)
    if not exercise:
        return make_response({"error": "Exercise not found."}, 404)

    data = request.get_json()
    try:
        workout_exercise = WorkoutExercises(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=data.get("reps"),
            sets=data.get("sets"),
            duration_seconds=data.get("duration_seconds")
        )
        db.session.add(workout_exercise)
        db.session.commit()
        return make_response(workout_exercises_schema.dump(workout_exercise), 201)
    except Exception as e:
        db.session.rollback()
        return make_response({"error": str(e)}, 400)


if __name__ == '__main__':
    app.run(port=5555, debug=True)