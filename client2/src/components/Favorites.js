import React, { useState, useEffect } from "react";

function Favorites() {
  const [favoriteWorkouts, setFavoriteWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch the list of favorite workouts from the API
    fetch("/favorites")
      .then((response) => response.json())
      .then((data) => {
        setFavoriteWorkouts(data);
        setLoading(false);
      })
      .catch((error) => console.error("Error fetching favorite workouts:", error));
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h2>Favorite Workouts</h2>
      {favoriteWorkouts.length === 0 ? (
        <p>No favorite workouts.</p>
      ) : (
        <ul>
          {favoriteWorkouts.map((workout) => (
            <li key={workout.id}>
              <h3>{workout.title}</h3>
              <p>{workout.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Favorites;
