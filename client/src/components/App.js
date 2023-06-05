import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Home from "./components/Home";
import Register from "./components/Register";
import Login from "./components/Login";
import WorkoutPlans from "./components/WorkoutPlans";
import CreateWorkout from "./components/CreateWorkout";
import ProgressTracker from "./components/ProgressTracker";
import Favorites from "./components/Favorites";

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
        <Route path="/favorites" component={Favorites} />
      </Switch>
    </div>
  );
}

export default App;
