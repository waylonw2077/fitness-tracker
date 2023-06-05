# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, WorkoutPlan

# Routes

# User endpoints
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user.to_dict()
        return {'message': 'User not found'}, 404

    def post(self):
        # Create a new user based on the request data
        data = request.get_json()
        user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

class UserRegistrationResource(Resource):
    def post(self):
        # Create a new user based on the request data
        data = request.get_json()
        user = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User registered successfully'}, 201

class UserLoginResource(Resource):
    def post(self):
        # Get user credentials from the request data
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Check if the username and password match a user in the database
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            return {'message': 'Login successful'}, 200

        return {'message': 'Invalid username or password'}, 401

api.add_resource(UserResource, '/users', '/users/<int:user_id>')
api.add_resource(UserRegistrationResource, '/register')
api.add_resource(UserLoginResource, '/login')

# WorkoutPlan endpoints
class WorkoutPlanResource(Resource):
    def get(self, workout_plan_id):
        workout_plan = WorkoutPlan.query.get(workout_plan_id)
        if workout_plan:
            return workout_plan.to_dict()
        return {'message': 'Workout plan not found'}, 404

    def post(self):
        # Create a new workout plan based on the request data
        data = request.get_json()
        workout_plan = WorkoutPlan(title=data['title'], description=data['description'])
        db.session.add(workout_plan)
        db.session.commit()
        return {'message': 'Workout plan created successfully'}, 201

api.add_resource(WorkoutPlanResource, '/workout-plans', '/workout-plans/<int:workout_plan_id>')

# Favorites endpoints
class FavoritesResource(Resource):
    def get(self, user_id):
        # Fetch the favorite workouts for the specified user from the database
        user = User.query.get(user_id)
        if user:
            favorite_workouts = user.favorite_workouts
            return [workout.to_dict() for workout in favorite_workouts]
        return {'message': 'User not found'}, 404

api.add_resource(FavoritesResource, '/favorites/<int:user_id>')

# Main entry point
if __name__ == '__main__':
    app.run(port=5555, debug=True)
