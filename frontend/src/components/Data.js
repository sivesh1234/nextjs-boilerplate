import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import Loader from 'react-loaders';
import 'loaders.css/loaders.min.css';
import { Tooltip } from 'react-tooltip'


const WEBSOCKET_URL = 'ws://localhost:8080/ws'; // Adjust this URL to match your WebSocket server
const API_BASE_URL = 'http://localhost:8080';

const Data = () => {
  const navigate = useNavigate();
  const [artists, setArtists] = useState(null);
  const [errorArtists, setErrorArtists] = useState(null);
  const [reccs, setReccs] = useState(null);
  const [errorReccs, setErrorReccs] = useState(null);
  // const [playlistId, setPlaylistId] = useState("4yFqCzL1KAsyR3p3Fd0PHn?si=db07deeb854949b4");
  const [highlightedArtists, setHighlightedArtists] = useState([]);
  const [highlightedReccs, setHighlightedReccs] = useState([]);

  const [playlistId, setPlaylistId] = useState(null);
  const num_jobs = 3;

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/fetch_results`, { withCredentials: true });
        if (response.status === 200) {
          const { job_1_result, job_2_result, job_3_result } = response.data;
          let results = 0;

          if (job_1_result) {
            setArtists(job_1_result);
            results++;
          }
          if (job_2_result) {
            setReccs(job_2_result);
            results++;
          }
          if (job_3_result) {
            setPlaylistId(job_3_result);
            results++;
          }

          // If no results, connect to WebSocket and wait for updates
          if (results !== num_jobs) {
            await connectWebSocket();
          }
        }
      } catch (error) {
        console.log(error);
        navigate('/');
      }
    };

    fetchResults();
  }, [navigate]);

  const get_user_id = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/get_user_id`, { withCredentials: true });
      if (response.status === 200) {
        return response.data.id;
      }
    } catch (error) { 
      console.log(error);
    }
  }

  const connectWebSocket = async () => {
    console.log("Connecting to WebSocket")
    const user_id = await get_user_id();
    console.log(user_id)

    const socket = new WebSocket(`${WEBSOCKET_URL}?user=${user_id}`);

    socket.onopen = () => {
      console.log('WebSocket connected');
    };

    socket.onmessage = (event) => {
      console.log('WebSocket message received:', event.data)
      const message = JSON.parse(event.data);
      console.log(message)
      if (message.job === 'job_1') {
        setArtists(message.result);
        // setPlaylistId(message.result.playlistId);
      } else if (message.job === 'job_2') {
        setReccs(message.result);
      } else if (message.job === 'job_3') {
        console.log("Playlist ID: ", message.result)
        setPlaylistId(message.result.playlist_id);
      }
    };

    socket.onclose = () => {
      console.log('WebSocket disconnected');
    };

    return socket;
  };

  const hoverArtist = (artist_name) => {
    if (reccs) {
      const recc_array = reccs.map((recc) => {
        if (recc.recc_from.includes(artist_name)) {
          return recc.name;
        }
      })
      console.log(recc_array)
      setHighlightedReccs(recc_array);
    }
  }

  const unhoverArtist = () => {
    setHighlightedReccs([]);
  }

  const hoverRecc = (recc) => {
    console.log(`Hovering over ${recc}`);
    setHighlightedArtists(recc.recc_from);
  }

  const unhoverRecc = () => {
    setHighlightedArtists([]);
  }
   
  console.log(highlightedArtists)

  return (
    <div className="flex flex-col lg:flex-row min-h-screen">
      {/* Left side (Playlist) */}
      <div className="w-full lg:w-1/2 p-4">
        <h2 className="text-2xl font-bold mb-4">Your Spotify Playlist</h2>
        {!playlistId ? (
          <div className="flex items-center justify-center h-full">
            <Loader type="line-scale-pulse-out" active color="#1dd660" />
          </div>
        ) : (
          <iframe
            title="Spotify Playlist"
            src={`https://open.spotify.com/embed/playlist/${playlistId}`}
            width="100%"
            height="100%"
            frameBorder="0"
            allowtransparency="true"
            allow="encrypted-media"
          ></iframe>
        )}
      </div>
      {/* Right side (Job Results) */}
      <div className="w-full lg:w-1/2 p-4">
        <div className="mb-4">
          <h3 className="text-2xl font-bold mb-4">Your Artists</h3>
          {artists === null ? (
            <div className="flex items-center justify-center h-full job-load-box animate-pulse bg-zinc-700 opacity-25 rounded-md">
              {/* <Loader type="ball-pulse" active color="#1dd660" /> */}
            </div>
          ) : errorArtists ? (
            <p className="text-red-500 text-center">{errorArtists}</p>
          ) : (
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4 justify-center items-center">
              {artists.map((artist, index) => {
                let classes = "rounded-md py-1 px-2 flex items-center justify-center animate-pop-in-late artist-box"
                const tooltip_text = artist.bio;
                const highlighted = highlightedArtists.includes(artist.name);
                if (highlighted) {
                  const artistIndex = index % 6;
                  classes += ` colour_${artistIndex} text-white`;
                } else {
                  classes += " bg-gray-100 text-gray-500";
                }
                return ( 
                  <div key={index} className={classes} onMouseEnter={() => {hoverArtist(artist.name)}} onMouseLeave={unhoverArtist} data-tooltip-id="my-tooltip" data-tooltip-content={tooltip_text}>
                    <p className="text-center">{artist.name}</p>
                    <Tooltip id="my-tooltip" style={{maxWidth: "250px"}}/>
                  </div>
                )
                })}
            </div>
          )}
        </div>
        <div>
          <h3 className="text-2xl font-bold mb-4">Recommended Artists</h3>
          {reccs === null ? (
            <div className="flex items-center justify-center h-full job-load-box animate-pulse bg-zinc-700 opacity-25 rounded-md">
              {/* <Loader type="ball-pulse" active color="#1dd660" /> */}
            </div>
          ) : errorReccs ? (
            <p className="text-red-500 text-center">{errorReccs}</p>
          ) : (
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4 justify-center items-center">
              {reccs.map((recc, index) => {
                let classes = "rounded-md py-1 px-2 flex items-center justify-center animate-pop-in-late artist-box"
                const tooltip_text = recc.bio;
                console.log(highlightedReccs)
                console.log(recc.name)
                const highlighted = highlightedReccs.includes(recc.name);
                if (highlighted) {
                  const reccIndex = index % 6;
                  classes += ` colour_${reccIndex} text-white`;
                } else {
                  classes += " bg-gray-100 text-gray-500";
                }
                console.log(classes)
                return ( 
                  <div key={index} onMouseEnter={() => {hoverRecc(recc)}} onMouseLeave={unhoverRecc} className={classes} data-tooltip-id="my-tooltip" data-tooltip-content={tooltip_text}>
                    <p className="text-center">{recc.name}</p>
                    <Tooltip id="my-tooltip" style={{maxWidth: "250px"}}/>
                  </div>
                )
                })}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Data;
