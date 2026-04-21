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
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean, nullable=False)

    workout_entries = db.relationship("WorkoutExercises", back_populates='exercise')

    @validates('name')
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Exercise name is required and cannot be blank.")
        return value.strip()

# Workout table
class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable = False)
    duration_minutes = db.Column(db.Integer, nullable = False)
    notes = db.Column(db.Text)

    #Validation check for duration_minutes to
    @validates("duration_minutes")
    def validate_duration(self, key, value):
        if value <= 0:
            raise ValueError("Duration of workout time cannot be less than zero. Please select a positive value.")
        return value

    exercise_entries = db.relationship("WorkoutExercises", back_populates='workout')

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

    @validates('reps')
    def validate_reps(self, key, value):
        if value is not None and value <= 0:
            raise ValueError("Reps must be greater than 0.")
        return value

    @validates('sets')
    def validate_sets(self, key, value):
        if value is not None and value <= 0:
            raise ValueError("Sets must be greater than 0.")
        return value

