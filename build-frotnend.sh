rm -rf glastojam/static

cd frontend

npm run build

cp -r build/ ../glastojam/static