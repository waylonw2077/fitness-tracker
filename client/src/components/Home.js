import React from "react";
import { Link } from "react-router-dom";
import './home.css';

function Home() {
  return (
    <div>
      <img
        src="https://media.istockphoto.com/id/1237011854/photo/smiling-woman-checking-her-physical-activity-on-smartwatch-young-female-athlete-looking-on.jpg?s=612x612&w=0&k=20&c=s-JPlTYUoExPELxOEo-i-u1p36a3IM8l8kba71RN10w="
        alt="Fitness Progress"
        className="left-image"
      />

      <div className="content">
        <h1>Welcome to Fitness Progress Tracker</h1>
        <p>Track your fitness progress and achieve your goals!</p>
        <p>Sign up or log in to get started.</p>

        <Link to="/register">
          <button class='btn'>Sign Up</button>
        </Link>

        <Link to="/login">
          <button class='btn'>Login</button>
        </Link>
      </div>
    </div>
  );
}

export default Home;