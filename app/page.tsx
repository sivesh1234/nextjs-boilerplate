"use client";

import React, { useEffect, useState } from 'react';

export default function Component() {
  const [artists, setArtists] = useState<string[]>([]);
  const [clashes, setClashes] = useState<any[]>([]);
  const [loadingArtists, setLoadingArtists] = useState(true);
  const [loadingClashes, setLoadingClashes] = useState(true);
  const [playlistId, setPlaylistId] = useState<string | null>(null);
  const [errorArtists, setErrorArtists] = useState<string | null>(null);
  const [errorClashes, setErrorClashes] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://localhost:8080/artists')
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error fetching data: ${response.statusText}`);
        }
        return response.json();
      })
      .then(data => {
        setArtists(data.artists);
        setLoadingArtists(false);
      })
      .catch(error => {
        setErrorArtists(error.message);
        setLoadingArtists(false);
      });
  }, []);

  useEffect(() => {
    console.log("Fetching clashes data...");
    fetch('http://localhost:8080/clashes')
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error fetching data: ${response.statusText}`);
        }
        return response.json();
      })
      .then(data => {
        console.log("Fetched clashes data:", data);
        setClashes(data.clashes);
        setLoadingClashes(false);
      })
      .catch(error => {
        setErrorClashes(error.message);
        setLoadingClashes(false);
      });
  }, []);

  useEffect(() => {
    console.log("Fetching playlist ID...");
    fetch('http://localhost:8080/playlist_id')
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error fetching playlist ID: ${response.statusText}`);
        }
        return response.json();
      })
      .then(data => {
        console.log("Fetched playlist ID:", data);
        setPlaylistId(data.playlist_id);
      })
      .catch(error => {
        console.error("Error fetching playlist ID:", error);
      });
  }, []);

  const handleSpotifyLogin = () => {
    const clientId = process.env.NEXT_PUBLIC_SPOTIFY_CLIENT_ID; // Replace with your Spotify client ID
    const redirectUri = process.env.NEXT_PUBLIC_SPOTIFY_REDIRECT_URI; // Replace with your redirect URI
    const scopes = [
      'user-read-private',
      'user-read-email',
      // Add more scopes as needed
    ];
    const authEndpoint = 'https://accounts.spotify.com/authorize';
    const responseType = 'token';

    window.location.href = `${authEndpoint}?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scopes.join('%20')}&response_type=${responseType}`;
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-extrabold mb-4 text-center">GlastoJam</h1>
      <div className="mb-8">
        <h2 className="text-2xl font-bold mb-4 text-center">Artists On Your Spotify</h2>
        {loadingArtists ? (
          <p className="text-center">Loading...</p>
        ) : errorArtists ? (
          <p className="text-red-500 text-center">{errorArtists}</p>
        ) : (
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4 justify-center items-center">
            {artists.map((artist, index) => (
              <div key={index} className="bg-gray-100 rounded-md p-4 flex items-center justify-center">
                <p className="text-gray-500 text-center">{artist}</p>
              </div>
            ))}
          </div>
        )}
      </div>
      <div className="bg-white rounded-lg shadow-md p-6 flex justify-center">
        <div id="playlist-preview">
          {playlistId ? (
            <iframe
              src={`https://open.spotify.com/embed/playlist/${playlistId}`}
              width="300"
              height="380"
              frameBorder="0"
              allowTransparency="true"
              allow="encrypted-media"
            ></iframe>
          ) : (
            <p>Loading playlist...</p>
          )}
        </div>
      </div>
      <h2 className="text-2xl font-bold mt-8 mb-4 text-center">Schedule Clashes</h2>
      {loadingClashes ? (
        <p className="text-center">Loading...</p>
      ) : errorClashes ? (
        <p className="text-red-500 text-center">{errorClashes}</p>
      ) : clashes.length > 0 ? (
        <div className="bg-white rounded-lg shadow-md p-6">
          <ul className="space-y-4">
            {clashes.map((clash) => (
              <li key={clash.id} className="flex items-center justify-between bg-red-100 rounded-md p-4">
                <div className="flex items-center">
                  <TriangleIcon className="w-6 h-6 text-red-500 mr-4" />
                  <div>
                    <h3 className="text-lg font-semibold text-black">
                      {clash.artists.map((artist, index) => `${artist} [${clash.stages[index]}]`).join(" vs. ")}
                    </h3>
                    <p className="text-black">Clash on {new Date(clash.start).toLocaleDateString()}</p>
                  </div>
                </div>
                <div className="text-black">
                  {new Date(clash.start).toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
                  &nbsp;-&nbsp;
                  {new Date(clash.end).toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
                </div>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p className="text-gray-500 text-center">No clashes found!</p>
      )}
    </div>
  );
}

function TriangleIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M13.73 4a2 2 0 0 0-3.46 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z" />
    </svg>
  );
}
