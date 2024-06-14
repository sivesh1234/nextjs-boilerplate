export default {
  reactStrictMode: true,
  webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
    config.plugins.push(
      new webpack.DefinePlugin({
        'process.env.NEXT_PUBLIC_SPOTIFY_CLIENT_ID': JSON.stringify(process.env.NEXT_PUBLIC_SPOTIFY_CLIENT_ID),
        'process.env.NEXT_PUBLIC_SPOTIFY_REDIRECT_URI': JSON.stringify(process.env.NEXT_PUBLIC_SPOTIFY_REDIRECT_URI),
        'process.env.NEXT_PUBLIC_API_BASE_URL': JSON.stringify(process.env.NEXT_PUBLIC_API_BASE_URL),
      })
    );
    return config;
  },
};
