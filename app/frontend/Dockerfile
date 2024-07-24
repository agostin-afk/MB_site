FROM node:alpine


COPY appmb /appmb
COPY package*.json ./appmb/package*.json



WORKDIR /appmb

RUN npm install

RUN npm run build

CMD ["npm", "start"]