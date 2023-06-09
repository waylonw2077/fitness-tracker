import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import './workoutplans.css';

function WorkoutPlans() {
  const [workoutPlans, setWorkoutPlans] = useState([]);

  useEffect(() => {
    // Fetch workout plans from the API
    fetch("/workout-plans")
      .then((response) => response.json())
      .then((data) => {
        setWorkoutPlans(data);
      })
      .catch((error) => console.error("Error fetching workout plans:", error));
  }, []);

  const deleteWorkoutPlan = (planId) => {
    fetch(`/workout-plans/${planId}`, {
      method: "DELETE",
    })
      .then((response) => response.json())
      .then((data) => {
        // Remove the deleted workout plan from the state
        setWorkoutPlans((prevPlans) =>
          prevPlans.filter((plan) => plan.id !== planId)
        );
      })
      .catch((error) =>
        console.error("Error deleting workout plan:", error)
      );
  };

  return (
    <div className='workout-plans-container'>
      <div className='navbar'>
        <h2>Workout Plans</h2>
      </div>
      {workoutPlans.length === 0 ? (
        <p>No workout plans available.</p>
      ) : (
        <ul>
          {workoutPlans.map((plan) => (
            <li key={plan.id}>
              <h3>{plan.title}</h3>
              <p>{plan.description}</p>
              <button className='btn' onClick={() => deleteWorkoutPlan(plan.id)}>
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
      <nav className='bottom-nav'>
        <Link to="/" className='navbar-link'>Home</Link>
        <Link to="/create-workout">Create Workout</Link>
        <Link to="/progress-tracker">Progress Tracker</Link>
      </nav>
    </div>
  );
}

export default WorkoutPlans;
