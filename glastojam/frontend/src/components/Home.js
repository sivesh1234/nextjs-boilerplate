import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import backgroundImage from '../img/glasto-poster4.jpeg'; // Adjust the path as necessary


const API_BASE_URL = 'http://localhost:8080/api';

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
    console.log('Logging in...');
  
      try {
        const response = await axios.get(`${API_BASE_URL}/login`, { withCredentials: true });
  
        if (response.status == 200) {
          const data = response.data;
          window.location.href = data.auth_url;  // Directly redirect the browser
        } else {
          console.error('Login failed');
        }
      } catch (error) {
        console.log("in error")
        console.log(error)
        console.error('Error during login:', error);
      }
    };

    return (
      <div className="flex flex-col lg:flex-row min-h-screen">
        {/* Left side (Login) */}
        <div className="flex flex-1 items-center justify-center bg-black p-4">
          <div className="home-page flex flex-col items-center justify-center min-h-screen w-full lg:min-h-0">
            <h1 className="text-5xl font-bold mb-6 text-white">GlastoJam</h1>
            <button
              className="bg-green-500 font-bold text-white px-4 py-2 rounded-md hover:bg-green-600"
              onClick={handleLogin}
            >
              Login with Spotify
            </button>
          </div>
        </div>
  
        {/* Right side (Image) */}
        <div
          className="hidden lg:block lg:w-1/2 bg-cover bg-center"
          style={{
            backgroundImage: `url(${backgroundImage})`,
            backgroundSize: 'auto 100%',
            backgroundRepeat: 'no-repeat',
            backgroundPosition: 'center right'
          }}
        ></div>
      </div>
    );
};

export default Home;
