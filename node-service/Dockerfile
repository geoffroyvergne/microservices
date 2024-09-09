FROM node:slim

COPY src ./src
COPY package.json ./package.json
RUN npm install

RUN adduser --system --group app-user

EXPOSE 3000
USER app-user

CMD ["node", "src/app.js"]
