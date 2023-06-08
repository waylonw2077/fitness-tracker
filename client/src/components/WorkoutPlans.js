import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

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

  return (
    <div>
      <h2>Workout Plans</h2>
      {workoutPlans.length === 0 ? (
        <p>No workout plans available.</p>
      ) : (
        <ul>
          {workoutPlans.map((plan) => (
            <li key={plan.id}>
              <h3>{plan.title}</h3>
              <p>{plan.description}</p>
            </li>
          ))}
        </ul>
      )}
      <div>
        <Link to="/create-workout">Create Workout</Link>
        <Link to="/favorites">Favorite Workouts</Link>
      </div>
    </div>
  );
}

export default WorkoutPlans;
