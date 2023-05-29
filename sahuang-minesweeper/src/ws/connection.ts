import { WebSocketServer } from "ws";
import { Message, Point, Tile } from "./types";

const WIDTH = 100;
const HEIGHT = 30;
const possibleTiles = ["covered", "key", "bomb", "c0", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"] as const;

function generateMap(): Tile[][] {
    const map: Tile[][] = [];
    for (let i = 0; i < HEIGHT; i++) {
        map[i] = [];
        for (let j = 0; j < WIDTH; j++) {
            map[i][j] = possibleTiles[Math.floor(Math.random() * possibleTiles.length)];
        }
    }
    return map;
}

function buildMessage(hero: Point): Message {
    return {
        hero,
        map: generateMap(),
        numKeysRetrieved: Math.floor(Math.random() * 10),
        livesRemaining: Math.floor(Math.random() * 10),
    };
}

function buildMessageJson(hero: Point): string {
    return JSON.stringify(buildMessage(hero));
}

export function setupConnection(wss: WebSocketServer) {
    wss.on('connection', (ws) => {
        let position = {
            x: Math.floor(Math.random() * WIDTH),
            y: Math.floor(Math.random() * HEIGHT)
        };

        ws.addEventListener('message', ({ data }) => {
            if (data === "up") {
                position.y = Math.max(0, position.y - 1);
            } else if (data === "down") {
                position.y = Math.min(HEIGHT - 1, position.y + 1);
            } else if (data === "left") {
                position.x = Math.max(0, position.x - 1);
            } else if (data === "right") {
                position.x = Math.min(WIDTH - 1, position.x + 1);
            }
            ws.send(buildMessageJson(position));
        });

        // send immediatly a feedback to the incoming connection    
        ws.send(buildMessageJson(position));
    });
}