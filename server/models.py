from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData


metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

# Define Models here
# Exercise table
class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

    exercise_entries = db.relationship("WorkoutExercises", back_populates='workout')


# Workout table
class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration = db.Column(db.Integer)
    notes = db.Column(db.Text)

    workout_entries = db.relationship("WorkoutExercises", back_populates='exercise')

# Workout exercises table (junction table for many to many relationship)
class WorkoutExercises(db.Model):
    __tablename__ = 'workoutexercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # Relationship objects
    workout = db.relationship("Workout", back_populates="exercise_entries")
    exercise = db.relationship("Exercise", back_populates="workout_entries")

