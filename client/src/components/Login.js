import React, { useState } from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import './login.css';

function Login() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const history = useHistory();

  const handleSubmit = (e) => {
    e.preventDefault();

    // Create an object with username, email, and password
    const credentials = {
      username: username,
      email: email,
      password: password,
    };

    // Send a POST request to the login endpoint
    axios
      .post("/login", credentials)
      .then((response) => {
        // Login successful
        setMessage(response.data.message);
        setUsername("");
        setEmail("");
        setPassword("");

        // Redirect to workout plans page
        history.push("/workout-plans");
      })
      .catch((error) => {
        // Login failed
        setMessage(error.response.data.message);
      });
  };

  return (
    <div className="login-container">
      <form className="login-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button className="btn" type="submit">Login</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default Login;
