FROM node:18
WORKDIR /app

RUN npm install

COPY . .
RUN npm run build 

CMD ["npx", "-y", "http-server", "-p", "8000", "/app/build"]