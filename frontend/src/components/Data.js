import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const WEBSOCKET_URL = 'ws://localhost:8080/ws'; // Adjust this URL to match your WebSocket server
const API_BASE_URL = 'http://localhost:8080';

const Data = () => {
  const navigate = useNavigate();
  const [job1Result, setJob1Result] = useState(null);
  const [job2Result, setJob2Result] = useState(null);
  const [playlistId, setPlaylistId] = useState(null);

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/fetch_results`, { withCredentials: true });
        if (response.status === 200) {
          const { job_1_result, job_2_result } = response.data;
          let hasResults = false;

          if (job_1_result) {
            setJob1Result(job_1_result);
            setPlaylistId(job_1_result.playlistId);
            hasResults = true;
          }
          if (job_2_result) {
            setJob2Result(job_2_result);
            hasResults = true;
          }

          // If no results, connect to WebSocket and wait for updates
          if (!hasResults) {
            connectWebSocket();
          }
        }
      } catch (error) {
        console.log(error)
        navigate('/');
      }
    };

    fetchResults();
  }, [navigate]);

  const connectWebSocket = () => {
    const socket = new WebSocket(WEBSOCKET_URL);

    socket.onopen = () => {
      console.log('WebSocket connected');
    };

    socket.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (message.job === 'job_1') {
        setJob1Result(message.result);
        setPlaylistId(message.result.playlistId);
      } else if (message.job === 'job_2') {
        setJob2Result(message.result);
      }
    };

    socket.onclose = () => {
      console.log('WebSocket disconnected');
    };

    return () => {
      socket.close();
    };
  };

  return (
    <div className="flex min-h-screen">
      <div className="w-1/2 p-4">
        <h2 className="text-2xl font-bold mb-4">Spotify Playlist</h2>
        {!playlistId ? (
          <p>Loading playlist...</p>
        ) : (
          <iframe
            title="Spotify Playlist"
            src={`https://open.spotify.com/embed/playlist/${playlistId}`}
            width="100%"
            height="380"
            frameBorder="0"
            allowtransparency="true"
            allow="encrypted-media"
          ></iframe>
        )}
      </div>
      <div className="w-1/2 p-4">
        <h2 className="text-2xl font-bold mb-4">Job Results</h2>
        <div className="mb-4">
          <h3 className="text-xl font-semibold">Job 1 Result</h3>
          {job1Result ? (
            <pre>{JSON.stringify(job1Result, null, 2)}</pre>
          ) : (
            <p>Waiting for job 1 result...</p>
          )}
        </div>
        <div>
          <h3 className="text-xl font-semibold">Job 2 Result</h3>
          {job2Result ? (
            <pre>{JSON.stringify(job2Result, null, 2)}</pre>
          ) : (
            <p>Waiting for job 2 result...</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Data;
