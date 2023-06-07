from sqlalchemy_serializer import Serializer
from config import db

# User model
class User(db.Model, ):
    __tablename__ = 'user'  # Update the table name to 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }
    
    # Relationships
    workout_progress = db.relationship('WorkoutProgress', backref='user_wp', lazy=True)
    favorite_workouts = db.relationship('FavoriteWorkout', backref='user_fw', lazy=True)

# WorkoutPlan model
class WorkoutPlan(db.Model, ):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            
        }
    # Relationships
    exercises = db.relationship('Exercise', backref='workout_exercises', lazy=True)
    favorite_workouts = db.relationship('FavoriteWorkout', backref='workout_fav', lazy=True)

# Exercise model
class Exercise(db.Model, ):
    id = db.Column(db.Integer, primary_key=True)
    workout_plan_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'workout_plan_id': self.workout_plan_id,
            'title': self.title,
            'description': self.description,
            'sets': self.sets,
            'reps': self.reps,
            
        }
    # Relationships
    workout_plan_rel = db.relationship('WorkoutPlan', backref='exercise_list', lazy=True)
    workout_progress = db.relationship('WorkoutProgress', backref='exercise', lazy='dynamic')

# WorkoutProgress model
class WorkoutProgress(db.Model, ):
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

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'exercise_id': self.exercise_id,
            'date': self.date,
            'duration': self.duration,
            'sets_completed': self.sets_completed,
            'reps_completed': self.reps_completed,
            'notes': self.notes,
            
        }

    # Relationships
    user_rel = db.relationship('User', backref=db.backref('workout_progress_rel', order_by=id), lazy=True)
    exercise_rel = db.relationship('Exercise', lazy=True)

# FavoriteWorkout model
class FavoriteWorkout(db.Model, ):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workout_plan_id = db.Column(db.Integer, db.ForeignKey('workout_plan.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'workout_plan_id': self.workout_plan_id,
            
        }

    # Relationships
    user_rel = db.relationship('User', backref=db.backref('favorite_workouts_user_rel', order_by=id), lazy=True)
    workout_plan_rel = db.relationship('WorkoutPlan', backref=db.backref('favorite_workouts_rel', order_by=id), lazy=True)
