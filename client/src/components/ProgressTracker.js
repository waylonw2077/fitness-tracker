import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './progresstracker.css';

function ProgressTracker() {
  const [workoutProgress, setWorkoutProgress] = useState([]);
  const [newProgress, setNewProgress] = useState({
    exercise_id: '',
    date: '',
    duration: '',
    sets_completed: '',
    reps_completed: '',
    notes: '',
  });

  useEffect(() => {
    fetchWorkoutProgress();
  }, []);

  const fetchWorkoutProgress = () => {
    fetch('api/workout-progress', {
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => setWorkoutProgress(data))
      .catch((error) => console.error('Error fetching workout progress:', error));
  };

  const fetchExercises = () => {
    fetch('api/exercises', {
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => setWorkoutProgress(data))
      .catch((error) => console.error('Error fetching exercises:', error));
  };

  useEffect(() => {
    fetchExercises();
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewProgress((prevProgress) => ({
      ...prevProgress,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch('api/workout-progress', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newProgress),
    })
      .then((response) => response.json())
      .then((data) => {
        // Clear the form and fetch the updated workout progress
        setNewProgress({
          exercise_id: '',
          date: '',
          duration: '',
          sets_completed: '',
          reps_completed: '',
          notes: '',
        });
        fetchWorkoutProgress();
      })
      .catch((error) => console.error('Error adding workout progress:', error));
  };

  const getExerciseName = (exerciseId) => {
    const exercise = workoutProgress.find((progress) => progress.exercise_id === exerciseId);
    return exercise ? exercise.name : '';
  };

  return (
    <div className='progress-tracker-container'>
      <h2 className='container'>Workout Progress</h2>

      <form className='progress-tracker-form' onSubmit={handleSubmit}>
        <label htmlFor="exercise_id">Exercise:</label>
        <select
          id="exercise_id"
          name="exercise_id"
          value={newProgress.exercise_id}
          onChange={handleInputChange}
        >
          <option value="">Select an exercise</option>
          {workoutProgress.map((exercise) => (
            <option key={exercise.id} value={exercise.id}>
              {exercise.name}
            </option>
          ))}
        </select>

        <label htmlFor="date">Date:</label>
        <input
          type="date"
          id="date"
          name="date"
          value={newProgress.date}
          onChange={handleInputChange}
        />

        <label htmlFor="duration">Duration (minutes):</label>
        <input
          type="number"
          id="duration"
          name="duration"
          value={newProgress.duration}
          onChange={handleInputChange}
        />

        <label htmlFor="sets_completed">Sets Completed:</label>
        <input
          type="number"
          id="sets_completed"
          name="sets_completed"
          value={newProgress.sets_completed}
          onChange={handleInputChange}
        />

        <label htmlFor="reps_completed">Reps Completed:</label>
        <input
          type="number"
          id="reps_completed"
          name="reps_completed"
          value={newProgress.reps_completed}
          onChange={handleInputChange}
        />

        <label htmlFor="notes">Notes:</label>
        <textarea
          id="notes"
          name="notes"
          value={newProgress.notes}
          onChange={handleInputChange}
        ></textarea>

        <button className='btn' type="submit">Add Progress</button>
      </form>
      <nav className="bottom-nav">
        <Link to="/">Home</Link>
        <Link to="/workout-plans">Workout Plans</Link>
        <Link to="/progress-tracker">Progress Tracker</Link>
      </nav>

      <div>
        {workoutProgress.map((progress) => (
          <div key={progress.id}>
            <p>Exercise: {getExerciseName(progress.exercise_id)}</p>
            <p>Date: {progress.date}</p>
            <p>Duration: {progress.duration} minutes</p>
            <p>Sets Completed: {progress.sets_completed}</p>
            <p>Reps Completed: {progress.reps_completed}</p>
            <p>Notes: {progress.notes}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProgressTracker;
