import React, { useState } from "react";
import { Link } from "react-router-dom";

function CreateWorkout() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    // Perform validation on form fields
    if (!title || !description) {
      setMessage("Please fill in all fields.");
      return;
    }

    // Create the workout plan by making a POST request to the API
    fetch("/workout-plans", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title, description }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === "Workout plan created successfully") {
          setMessage(data.message);
          setTitle("");
          setDescription("");
        } else {
          setMessage("Failed to create workout plan.");
        }
      })
      .catch((error) => console.error("Error creating workout plan:", error));
  };

  return (
    <div>
      <h2>Create Workout</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Title:</label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
        </div>
        <button type="submit">Create</button>
        <Link to="/workout-plans">Back to Workout Plans</Link>
      </form>
    </div>
  );
}

export default CreateWorkout;
