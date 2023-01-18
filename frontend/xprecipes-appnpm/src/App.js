import React, { useState } from 'react';
import './App.css';
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import Dashboard from './components/dashboard/Dashboard';
import Preferences from './components/preferences/Preferences';
import NotFound from './components/notfound/NotFound';
import Login from './components/Login/Login'
import useToken from './components/app/useToken';




function App() {
  const { token, setToken } = useToken();

  if(!token) {
    return <Login setToken={setToken} />
  }

  return (
    <div className="wrapper">
      <h1>Application</h1>
      <BrowserRouter>
        <Routes path='/' fallback={<NotFound />}>
          <Route path='dashboard' element={<Dashboard />} />     
          <Route path='preferences' element={<Preferences />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
