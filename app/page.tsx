"use client";

import Image from "next/image";
import GlastoPlaylist from '../components/glasto-playlist.tsx'

/**
 * v0 by Vercel.
 * @see https://v0.dev/t/Z37PGNhPiQ3
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */

export default function Component() {
  const artists = [
    "Dua Lipa",
    "Harry Styles",
    "Billie Eilish",
    "The Weeknd",
    "Bad Bunny",
    "Taylor Swift",
    "Ed Sheeran",
    "Ariana Grande",
    "Drake",
    "Rihanna",
  ];

  const handleSpotifyLogin = () => {
    const clientId = 'YOUR_SPOTIFY_CLIENT_ID'; // Replace with your Spotify client ID
    const redirectUri = 'YOUR_REDIRECT_URI'; // Replace with your redirect URI
    const scopes = [
      'user-read-private',
      'user-read-email',
      // Add more scopes as needed
    ];
    const authEndpoint = 'https://accounts.spotify.com/authorize';
    const responseType = 'token';

    const authUrl = `${authEndpoint}?client_id=${clientId}&redirect_uri=${encodeURIComponent(redirectUri)}&scope=${encodeURIComponent(scopes.join(' '))}&response_type=${responseType}`;

    window.location.href = authUrl;
  };

  const clashes = [
    {
      id: 1,
      artists: ["Dua Lipa", "Harry Styles"],
      start: "2023-06-24T19:00:00",
      end: "2023-06-24T19:30:00",
    },
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-4">Your Festival Playlist</h1>
      <div className="mb-8">
        <h2 className="text-2xl font-bold mb-4">Performing Artists</h2>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          {artists.map((artist, index) => (
            <div key={index} className="bg-gray-100 rounded-md p-4 flex items-center justify-center">
              <p className="text-gray-500">{artist}</p>
            </div>
          ))}
        </div>
      </div>
      <div className="bg-white rounded-lg shadow-md p-6">
      <button
          onClick={handleSpotifyLogin}
          className="bg-green-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-green-600 transition duration-300"
        >
          Login with Spotify
        </button>
      </div>
      <h2 className="text-2xl font-bold mt-8 mb-4">Schedule Clashes</h2>
      {clashes.length > 0 ? (
        <div className="bg-white rounded-lg shadow-md p-6">
          <ul className="space-y-4">
            {clashes.map((clash) => (
              <li key={clash.id} className="flex items-center justify-between bg-red-100 rounded-md p-4">
                <div className="flex items-center">
                  <TriangleIcon className="w-6 h-6 text-red-500 mr-4" />
                  <div>
                    <h3 className="text-lg font-semibold">{clash.artists.join(" vs. ")}</h3>
                    <p className="text-gray-500">Clash</p>
                  </div>
                </div>
                <div className="text-gray-500">
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
        <p className="text-gray-500">No clashes found!</p>
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
