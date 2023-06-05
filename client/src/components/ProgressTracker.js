import React, { useState, useEffect } from "react";

function ProgressTracker() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch the list of workouts from the API
    fetch("/workout-plans")
      .then((response) => response.json())
      .then((data) => {
        setWorkouts(data);
        setLoading(false);
      })
      .catch((error) => console.error("Error fetching workouts:", error));
  }, []);

  const handleExerciseCompletion = (workoutId, exerciseId) => {
    // Send a request to the API to mark the exercise as completed for the user
    // You can use the workoutId and exerciseId to identify the specific exercise

    // Example code:
    fetch(`/workout-plans/${workoutId}/exercises/${exerciseId}/complete`, {
      method: "POST",
      // Additional request options (e.g., headers, body) can be added here
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response if needed
        console.log(data);
      })
      .catch((error) =>
        console.error("Error marking exercise completion:", error)
      );
  };

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h2>Progress Tracker</h2>
      {workouts.length === 0 ? (
        <p>No workouts available.</p>
      ) : (
        <ul>
          {workouts.map((workout) => (
            <li key={workout.id}>
              <h3>{workout.title}</h3>
              <p>{workout.description}</p>
              {workout.exercises.length === 0 ? (
                <p>No exercises available for this workout.</p>
              ) : (
                <ul>
                  {workout.exercises.map((exercise) => (
                    <li key={exercise.id}>
                      <p>{exercise.title}</p>
                      <button
                        onClick={() =>
                          handleExerciseCompletion(workout.id, exercise.id)
                        }
                      >
                        Mark as Completed
                      </button>
                    </li>
                  ))}
                </ul>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProgressTracker;
