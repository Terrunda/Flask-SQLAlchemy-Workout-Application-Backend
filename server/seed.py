#!/usr/bin/env python3

from app import app
from models import Workout, WorkoutExercises, Exercise
from datetime import date.

with app.app_context():
    # reset data and add new example data, committing to db
    WorkoutExercises.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    # Sample exercise records
    exercise_1 = Exercise(name="Yoga", category="Flexibility", equipment_needed=False)

    exercise_2 = Exercise(name="Dumbbell rows", category="Strength", equipment_needed=True)

    exercise_3 = Exercise(name="Cycling", category="Cardiovascular", equipment_needed=False)

    exercise_4 = Exercise(name="Swimming", category="Cardiovascular", equipment_needed=False)

    exercise_5 = Exercise(name="Shoulder press", category="Strength", equipment_needed=True)


    # Sample Workout records.
    workout_1 = Workout(date=date(2026, 4, 18), duration_minutes=15, notes="Cardiovascular Training"
    )

    workout_2 = Workout(date=date(2026, 4, 15), duration_minutes=35, notes="General exercises.")
    
    workout_3 = Workout(date=date(2026, 4, 17), duration_minutes=40, notes="Strength exercises.")

    #  4. Creating WorkoutExercise 
    workout_exercise_1 = WorkoutExercises(workout=workout_3,exercise=exercise_2, sets=5, reps=10)

    workout_exercise_2 = WorkoutExercises(workout=workout_3, exercise=exercise_5, sets=5, reps=10)

    workout_exercise_3 = WorkoutExercises(workout=workout_1,exercise=exercise_3)

    workout_exercise_4 = WorkoutExercises(workout=workout_1,exercise=exercise_4)

    workout_exercise_5 = WorkoutExercises(workout=workout_2,exercise=exercise_3)

    workout_exercise_6 = WorkoutExercises(workout=workout_2,exercise=exercise_5, sets =10, reps=5)

    workout_exercise_7 = WorkoutExercises(workout=workout_2,exercise=exercise_1)



    db.session.add_all([
        exercise_1, exercise_2, exercise_3, exercise_4, exercise_5,
        workout_1, workout_2, workout_3,
        workout_exercise_1, workout_exercise_2, workout_exercise_3, workout_exercise_4, workout_exercise_5, workout_exercise_6, workout_exercise_7
    ])


    db.session.commit()