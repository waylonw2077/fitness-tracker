import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <h1>Welcome to Fitness Progress Tracker</h1>
      <p>Track your fitness progress and achieve your goals!</p>
      <p>Sign up or log in to get started.</p>

      <Link to="/register">
        <button>Sign Up</button>
      </Link>

      <Link to="/login">
        <button>Login</button>
      </Link>
    </div>
  );
}

export default Home;
