import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

function WorkoutPlans() {
  const [workoutPlans, setWorkoutPlans] = useState([]);

  useEffect(() => {
    // Fetch workout plans from the API
    fetch("/workout-plans")
      .then((response) => response.json())
      .then((data) => setWorkoutPlans(data))
      .catch((error) => console.error("Error fetching workout plans:", error));
  }, []);

  const handleFavorite = (workoutPlanId) => {
    // Find the workout plan by its ID in the workoutPlans array
    const updatedWorkoutPlans = workoutPlans.map((plan) => {
      if (plan.id === workoutPlanId) {
        // Toggle the favorite status of the workout plan
        return { ...plan, favorite: !plan.favorite };
      }
      return plan;
    });
  
    // Update the workoutPlans state with the updated array
    setWorkoutPlans(updatedWorkoutPlans);
  };
  

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
              {plan.favorite ? (
              <button onClick={() => handleFavorite(plan.id)}>Unfavorite</button>
            ) : (
              <button onClick={() => handleFavorite(plan.id)}>Favorite</button>
            )}
          </li>
        ))}

        </ul>
      )}
      <div>
        <Link to="/create-workout">Create Workout</Link>
        <Link to="/favorite-workouts">Favorite Workouts</Link>
      </div>
    </div>
  );
}

export default WorkoutPlans;
