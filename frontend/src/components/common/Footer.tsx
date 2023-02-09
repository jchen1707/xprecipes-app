import React from 'react';
import './footer.scss';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-800 p-4">
      <div className="container mx-auto text-center text-white">
        <p>Copyright &copy; {new Date().getFullYear()} Your App</p>
      </div>
    </footer>
  );
};

export default Footer;
