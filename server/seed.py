#!/usr/bin/env python3

from app import app
from models import db, User, WorkoutPlan, Exercise

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")

        # Create sample users
        user1 = User(username='john', email='john@example.com', password='password')
        user2 = User(username='jane', email='jane@example.com', password='password')
        db.session.add_all([user1, user2])

        # Create sample workout plans
        workout_plan1 = WorkoutPlan(title='Beginner Plan', description='A workout plan for beginners')
        workout_plan2 = WorkoutPlan(title='Advanced Plan', description='An advanced workout plan')
        db.session.add_all([workout_plan1, workout_plan2])

        # Create sample exercises
        exercise1 = Exercise(title='Push-ups', workout_plan_id=workout_plan1.id)
        exercise2 = Exercise(title='Squats', workout_plan_id=workout_plan1.id)
        exercise3 = Exercise(title='Deadlifts', workout_plan_id=workout_plan2.id)
        db.session.add_all([exercise1, exercise2, exercise3])

        # Commit the changes to the database
        db.session.commit()

        print("Seed complete!")
