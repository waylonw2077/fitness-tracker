# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import User, WorkoutPlan, Exercise, WorkoutProgress, FavoriteWorkout

# Routes
# User endpoints
class UserIdResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user.to_dict()
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        # Update user profile
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            # Update other user profile fields as needed
            db.session.commit()
            return {'message': 'User updated successfully'}
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        # Delete user account
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}
        return {'message': 'User not found'}, 404
    
class UserResource(Resource):
    def post(self):
        # Create a new user based on the request data
        data = request.get_json()
        user = User(username=data['username'],
                    email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201


class UserRegistrationResource(Resource):
    def post(self):
        # Create a new user based on the request data
        data = request.get_json()
        user = User(username=data['username'],
                    email=data['email'], password=data['password'])
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
        user = User.query.filter_by(
            username=username, password=password).first()

        if user:
            return {'message': 'Login successful'}, 200

        return {'message': 'Invalid username or password'}, 401


api.add_resource(UserIdResource, '/users/<int:user_id>')
api.add_resource(UserResource, '/users')
api.add_resource(UserRegistrationResource, '/register')
api.add_resource(UserLoginResource, '/login')

# WorkoutPlan endpoints
class WorkoutPlanIdResource(Resource):
    def get(self, workout_plan_id):
        workout_plan = WorkoutPlan.query.get(workout_plan_id)
        if workout_plan:
            return workout_plan.to_dict()
        return {'message': 'Workout plan not found'}, 404

    def put(self, workout_plan_id):
        print("PUT request received for workout plan ID:", workout_plan_id)
        # Update workout plan details
        workout_plan = WorkoutPlan.query.get(workout_plan_id)
        if workout_plan:
            print("Workout plan found:", workout_plan.to_dict())
            data = request.get_json()
            print("Received data:", data)
            workout_plan.title = data['title']
            workout_plan.description = data['description']
            # Update other workout plan fields as needed
            db.session.commit()
            print("Workout plan updated successfully")
            return {'message': 'Workout plan updated successfully'}
        print("Workout plan not found")
        return {'message': 'Workout plan not found'}, 404

    def delete(self, workout_plan_id):
        print("DELETE request received for workout plan ID:", workout_plan_id)
        # Delete workout plan
        workout_plan = WorkoutPlan.query.get(workout_plan_id)
        if workout_plan:
            print("Workout plan found:", workout_plan.to_dict())
            db.session.delete(workout_plan)
            db.session.commit()
            print("Workout plan deleted successfully")
            return {'message': 'Workout plan deleted successfully'}
        print("Workout plan not found")
        return {'message': 'Workout plan not found'}, 404

api.add_resource(WorkoutPlanIdResource, '/workout-plans/<int:workout_plan_id>')

class WorkoutPlanResource(Resource):
    def get(self):
        workout_plans = WorkoutPlan.query.all()
        return [plan.to_dict() for plan in workout_plans]

    def post(self):
        print("POST request received")
        # Create a new workout plan based on the request data
        data = request.get_json()
        print("Received data:", data)
        workout_plan = WorkoutPlan(
            title=data['title'], description=data['description'])
        
        db.session.add(workout_plan)
        db.session.commit()

        print("Workout plan created successfully")
        return {'message': 'Workout plan created successfully'}, 201
    
api.add_resource(WorkoutPlanResource, '/workout-plans')


# Exercise endpoints
class ExerciseIdResource(Resource):
    def get(self, exercise_id):
        # Get exercise by ID
        exercise = Exercise.query.get(exercise_id)
        if exercise:
            return exercise.to_dict()
        return {'message': 'Exercise not found'}, 404

    # def post(self):
    #     # Create a new exercise
    #     data = request.get_json()
    #     exercise = Exercise(
    #         title=data['title'], description=data['description'], sets=data['sets'], reps=data['reps'])
    #     db.session.add(exercise)
    #     db.session.commit()
    #     return {'message': 'Exercise created successfully'}, 201

    def put(self, exercise_id):
        # Update exercise details
        exercise = Exercise.query.get(exercise_id)
        if exercise:
            data = request.get_json()
            exercise.title = data['title']
            exercise.description = data['description']
            exercise.sets = data['sets']
            exercise.reps = data['reps']
            # Update other exercise fields as needed
            db.session.commit()
            return {'message': 'Exercise updated successfully'}
        return {'message': 'Exercise not found'}, 404

    def delete(self, exercise_id):
        # Delete exercise
        exercise = Exercise.query.get(exercise_id)
        if exercise:
            db.session.delete(exercise)
            db.session.commit()
            return {'message': 'Exercise deleted successfully'}
        return {'message': 'Exercise not found'}, 404

api.add_resource(ExerciseIdResource,
                '/exercises/<int:exercise_id>')

class ExerciseResource(Resource):
    def get(self):
        exercise = Exercise.query.all()
        return [plan.to_dict() for plan in exercise]

    def post(self):
        # Create a new exercise
        data = request.get_json()
        exercise = Exercise(
            title=data['title'], description=data['description'], sets=data['sets'], reps=data['reps'])
        db.session.add(exercise)
        db.session.commit()
        return {'message': 'Exercise created successfully'}, 201
    
api.add_resource(ExerciseResource, '/exercises')


# WorkoutProgress endpoints
class WorkoutProgressIdResource(Resource):
    def get(self, progress_id):
        # Get workout progress by ID
        progress = WorkoutProgress.query.get(progress_id)
        if progress:
            return progress.to_dict()
        return {'message': 'Workout progress not found'}, 404

    # def post(self):
    #     # Log workout progress
    #     data = request.get_json()
    #     progress = WorkoutProgress(date=data['date'], duration=data['duration'],
    #                                sets_completed=data['sets_completed'], reps_completed=data['reps_completed'])
    #     db.session.add(progress)
    #     db.session.commit()
    #     return {'message': 'Workout progress logged successfully'}, 201

    def put(self, progress_id):
        # Update workout progress details
        progress = WorkoutProgress.query.get(progress_id)
        if progress:
            data = request.get_json()
            progress.date = data['date']
            progress.duration = data['duration']
            progress.sets_completed = data['sets_completed']
            progress.reps_completed = data['reps_completed']
            # Update other workout progress fields as needed
            db.session.commit()
            return {'message': 'Workout progress updated successfully'}
        return {'message': 'Workout progress not found'}, 404

    def delete(self, progress_id):
        # Delete workout progress
        progress = WorkoutProgress.query.get(progress_id)
        if progress:
            db.session.delete(progress)
            db.session.commit()
            return {'message': 'Workout progress deleted successfully'}
        return {'message': 'Workout progress not found'}, 404


api.add_resource(WorkoutProgressIdResource,
                '/workout-progress/<int:progress_id>')

class WorkoutProgressResource(Resource):
    def get(self):
        wp = WorkoutProgressResource.query.all()
        return [plan.to_dict() for plan in wp]
    
    def post(self):
        # Log workout progress
        data = request.get_json()
        progress = WorkoutProgress(date=data['date'], duration=data['duration'],
                                sets_completed=data['sets_completed'], reps_completed=data['reps_completed'])
        db.session.add(progress)
        db.session.commit()
        return {'message': 'Workout progress logged successfully'}, 201
    
api.add_resource(WorkoutProgressResource,
                '/workout-progress')


class FavoritesIdResource(Resource):
    def get(self, user_id):
        # Fetch the favorite workouts for the specified user from the database
        user = User.query.get(user_id)
        if user:
            favorite_workouts = user.favorite_workouts
            return [workout.to_dict() for workout in favorite_workouts]
        return {'message': 'User not found'}, 404


    def delete(self, user_id, favorite_id):
        # Remove workout from favorites for the specified user
        favorite = FavoriteWorkout.query.filter_by(
            user_id=user_id, workout_id=favorite_id).first()
        if favorite:
            db.session.delete(favorite)
            db.session.commit()
            return {'message': 'Workout removed from favorites successfully'}
        return {'message': 'Favorite workout not found'}, 404


api.add_resource(FavoritesIdResource, '/favorites/<int:user_id>')

class FavoritesResource(Resource):
    def get(self):
        favorites = FavoriteWorkout.query.all()
        return [favorite.to_dict() for favorite in favorites]
    
    def post(self):
        # Mark workout as favorite
        data = request.get_json()
        favorite = FavoriteWorkout(
            workout_id=data['workout_id'], user_id=data['user_id'])
        db.session.add(favorite)
        db.session.commit()
        return {'message': 'Workout marked as favorite successfully'}, 201
    
api.add_resource(FavoritesResource, '/favorites')

# Main entry point
if __name__ == '__main__':
    app.run(port=5555, debug=True)
