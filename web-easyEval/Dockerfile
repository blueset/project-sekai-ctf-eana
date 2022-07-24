FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080
ENV PORT=8080
ENV FLAG='vsctf{regExAin’tGoodEnufForWAF}'
CMD [ "node", "index.js" ]
# docker build --tag view-source-ctf-easy-eval .
# docker run -d --publish 32793:8080 --name view-source-ctf-easy-eval view-source-ctf-easy-eval
