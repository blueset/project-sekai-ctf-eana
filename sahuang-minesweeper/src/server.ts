import express from "express";
import ViteExpress from "vite-express";
import http from "http";
import { WebSocketServer } from "ws";
import { setupConnection } from "./ws/connection.js";

const app = express();

app.get("/message", (_, res) => res.send("Hello from express!"));

const server = http.createServer(app);
const wss = new WebSocketServer({ server, path: "/socket" });
setupConnection(wss);

server.listen(process.env.PORT || 8999, () => {
    console.log(`Server started on http://127.0.0.1:8999 :)`);
});

ViteExpress.bind(app, server);