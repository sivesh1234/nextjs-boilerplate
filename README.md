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

Make sure the fastAPI redirects to the port of the front-end, default is:
```bash
origins = [
    "http://localhost:3004",  # Your Next.js frontend URL
]
```



