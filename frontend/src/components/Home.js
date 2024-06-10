import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8080';

const Home = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const checkAuth = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/check_auth`, { withCredentials: true });
        if (response.status === 200) {
          navigate('/data');
        }
      } catch (error) {
        console.log('User is not authenticated');
      }
    };

    checkAuth();
  }, [navigate]);

  const handleLogin = async () => {
      const apiBaseUrl = process.env.REACT_APP_API_BASE_URL;
  
      try {
        const response = await fetch(`${apiBaseUrl}/login`, {
          method: 'GET',
          credentials: 'include',
        });
  
        if (response.ok) {
          const data = await response.json();
          window.location.href = data.auth_url;  // Directly redirect the browser
        } else {
          console.error('Login failed');
        }
      } catch (error) {
        console.error('Error during login:', error);
      }
    };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Login with Spotify</h1>
      <button
        className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600"
        onClick={handleLogin}
      >
        Login with Spotify
      </button>
    </div>
  );
};

export default Home;
