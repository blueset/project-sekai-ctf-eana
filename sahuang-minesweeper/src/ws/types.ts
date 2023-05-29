export interface Point {
    x: number;
    y: number;
}

export type Tile = "covered" | "key" | "bomb" | "c0" | "c1" | "c2" | "c3" | "c4" | "c5" | "c6" | "c7" | "c8";

export interface Message {
    hero: Point;
    map: Tile[][];
    numKeysRetrieved: number;
    livesRemaining: number;
}
