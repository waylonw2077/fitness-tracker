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
              <button>Track Progress</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ProgressTracker;
