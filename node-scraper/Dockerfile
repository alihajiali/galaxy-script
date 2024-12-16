FROM mcr.microsoft.com/playwright:v1.39.0-focal

ENV AUTH_TOKEN="your_static_token_here"

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "main.js"]
