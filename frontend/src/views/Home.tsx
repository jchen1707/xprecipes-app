import React from 'react';
import { Link } from 'react-router-dom';
import { useMediaQuery } from 'react-responsive';
import './Home.scss';

const Home: React.FC = () => {
  const isTabletOrMobile = useMediaQuery({ maxWidth: 767 });

  return (
    <div className="home">
      <header className="header">
        <div className="header-content">
          <h1 className="header-title">Xprecipes</h1>
          <div className="header-actions">
            <Link to="/login" className="btn btn-login">Login</Link>
            <Link to="/register" className="btn btn-register">Register</Link>
          </div>
        </div>
      </header>
      <nav className={`nav ${isTabletOrMobile ? 'nav-mobile' : ''}`}>
        <Link to="/recipes" className="nav-item">Recipes</Link>
        <Link to="/ingredients" className="nav-item">Ingredient Storage</Link>
      </nav>
    </div>
  );
};

export default Home;
