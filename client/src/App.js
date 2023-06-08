// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Home from "./components/Home";
import Register from "./components/Register";
import Login from "./components/Login";
import WorkoutPlans from "./components/WorkoutPlans";
import CreateWorkout from "./components/CreateWorkout";
import ProgressTracker from "./components/ProgressTracker";
import './App.css'


function App() {
  // Code goes here!

  return (
    <div>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/register" component={Register} />
        <Route path="/login" component={Login} />
        <Route path="/workout-plans" component={WorkoutPlans} />
        <Route path="/create-workout" component={CreateWorkout} />
        <Route path="/progress-tracker" component={ProgressTracker} />
      </Switch>
    </div>
  );
}

export default App;
