from sqlalchemy_serializer import SerializerMixin
from config import db

# User model
class User(db.Model, SerializerMixin):
    __tablename__ = 'user'  # Update the table name to 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # Relationships
    workout_progress = db.relationship('WorkoutProgress', backref='user_wp', lazy=True)
    favorite_workouts = db.relationship('FavoriteWorkout', backref='user_fw', lazy=True)

# WorkoutPlan model
class WorkoutPlan(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    # Relationships
    exercises = db.relationship('Exercise', backref='workout_exercises', lazy=True)
    favorite_workouts = db.relationship('FavoriteWorkout', backref='workout_fav', lazy=True)

# Exercise model
class Exercise(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    workout_plan_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Relationships
    workout_plan_rel = db.relationship('WorkoutPlan', backref='exercise_list', lazy=True)
    workout_progress = db.relationship('WorkoutProgress', backref='exercise', lazy='dynamic')

# WorkoutProgress model
class WorkoutProgress(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    date = db.Column(db.Date)
    duration = db.Column(db.Integer)
    sets_completed = db.Column(db.Integer)
    reps_completed = db.Column(db.Integer)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Relationships
    user_rel = db.relationship('User', backref=db.backref('workout_progress_rel', order_by=id), lazy=True)
    exercise_rel = db.relationship('Exercise', lazy=True)

# FavoriteWorkout model
class FavoriteWorkout(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workout_plan_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Relationships
    user_rel = db.relationship('User', backref=db.backref('favorite_workouts_user_rel', order_by=id), lazy=True)
    workout_plan_rel = db.relationship('WorkoutPlan', backref=db.backref('favorite_workouts_rel', order_by=id), lazy=True)
