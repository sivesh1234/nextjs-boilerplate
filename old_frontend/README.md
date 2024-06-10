## Getting Started

First, run the dev server for the front-end (in nextjs-boilerplate directory):



```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```
Then, initiate the fastAPI backend at port 8080 with:
```bash
uvicorn spotifyloginv2:app --reload --port 8080
```

Create a `.env.local` file in the root of the fastAPI directory with the following:
```bash
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

Go to http://localhost:8080/login to intiate the Spotify OAuth

Make sure the fastAPI redirects to the port of the front-end, default is:
```bash
origins = [
    "http://localhost:3004",  # Your Next.js frontend URL
]
```



