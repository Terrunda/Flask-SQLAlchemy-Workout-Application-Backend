from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(load_default=None)
    equipment_needed = fields.Bool(load_default=None)

    @validates("name")
    def validate_name(self, value):
        if not value or not value.strip():
            raise ValidationError("Exercise name is required and cannot be blank.")


class WorkoutExercisesSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(load_default=None)
    sets = fields.Int(load_default=None)
    duration_seconds = fields.Int(load_default=None)

    exercise = fields.Nested(ExerciseSchema, only=("id", "name"), dump_only=True)

    @validates("reps")
    def validate_reps(self, value):
        if value is not None and value <= 0:
            raise ValidationError("Reps must be greater than 0.")

    @validates("sets")
    def validate_sets(self, value):
        if value is not None and value <= 0:
            raise ValidationError("Sets must be greater than 0.")

    @validates("duration_seconds")
    def validate_duration_seconds(self, value):
        if value is not None and value <= 0:
            raise ValidationError("Duration in seconds must be greater than 0.")


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(load_default=None)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str(load_default=None)

    exercise_entries = fields.Nested(WorkoutExercisesSchema, many=True, dump_only=True)

    @validates("duration_minutes")
    def validate_duration(self, value):
        if value is None or value <= 0:
            raise ValidationError("Duration must be greater than 0.")