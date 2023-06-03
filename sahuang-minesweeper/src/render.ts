import type { Message, Point, Tile } from "./ws/types";

let main: HTMLElement;
let player: HTMLElement;

function populateField(map: Tile[][]) {
  const width = map[0].length, height = map.length;
  const sizer: HTMLDivElement = main.querySelector("#sizer")!;
  sizer.style.width = `calc(var(--cell-size) * ${width})`;
  sizer.style.height = `calc(var(--cell-size) * ${height})`;
  for (let i = 0; i < height; i++) {
    for (let j = 0; j < width; j++) {
      let cell: HTMLElement = main.querySelector(`#cell-${i}-${j}`)!;
      if (!cell) {
        cell = document.createElement("section");
        cell.id = `cell-${i}-${j}`;
        cell.style.top = `calc(var(--cell-size) * ${i})`;
        cell.style.left = `calc(var(--cell-size) * ${j})`;
        main.appendChild(cell);
      }
      cell.className = map[i][j];
    }
  }
}

function movePlayer(x: number, y: number) {
  player.style.transform = `translate(calc(var(--cell-size) * ${x}), calc(var(--cell-size) * ${y}))`;
}

let playerAnimationTimeout = -1;

type Direction = "up" | "down" | "left" | "right";

function startPlayerAnimation(direction: Direction) {
  if (playerAnimationTimeout >= 0) {
    clearTimeout(playerAnimationTimeout);
  }
  player.className = direction;
  player.dataset.direction = direction;
  playerAnimationTimeout = setTimeout(() => {
    player.className = "";
  }, 1000) as unknown as number;
}

function registerListeners(connection: WebSocket) {
  document.addEventListener("keydown", (evt) => {
    if (evt.key === "ArrowUp") {
      connection.send("up");
    } else if (evt.key === "ArrowDown") {
      connection.send("down");
    } else if (evt.key === "ArrowLeft") {
      connection.send("left");
    } else if (evt.key === "ArrowRight") {
      connection.send("right");
    }

    // TODO: Debug messages
    if (evt.key === "w") {
      connection.send("win");
    } else if (evt.key === "l") {
      connection.send("lose");
    }
  });

  player.addEventListener("transitionend", () => {
    player.scrollIntoView({
      behavior: "smooth",
      block: "center",
      inline: "center",
    });
  });
}

export const setupWithWebSocket = (winCallback: (flag: string) => void, loseCallback: () => void) => {
  main = document.querySelector("main")!;
  player = document.getElementById("player")!;
  const lives = document.getElementById("lives")!;
  const keys = document.getElementById("keys")!;
  let hasWon = false;

  let playerPos: Point | null = null;
  const connection = new WebSocket(
    `${location.protocol === "https:" ? "wss" : "ws"}://${location.host}/socket`
  );
  connection.addEventListener("open", () => {
    console.log("Connected!");
  });
  connection.addEventListener("message", (evt) => {
    const data: Message = JSON.parse(evt.data);
    if (data.flag) {
      hasWon = true;
      winCallback(data.flag);
      return;
    }
    populateField(data.map);
    if (playerPos) {
      movePlayer(data.hero.x, data.hero.y);
      if (data.hero.x === playerPos.x && data.hero.y < playerPos.y) {
        startPlayerAnimation("up");
      } else if (data.hero.x === playerPos.x && data.hero.y > playerPos.y) {
        startPlayerAnimation("down");
      } else if (data.hero.x < playerPos.x && data.hero.y === playerPos.y) {
        startPlayerAnimation("left");
      } else if (data.hero.x > playerPos.x && data.hero.y === playerPos.y) {
        startPlayerAnimation("right");
      }
    } else {
      player.classList.add("noTransition");
      movePlayer(data.hero.x, data.hero.y);
      player.classList.remove("noTransition");
    }
    playerPos = data.hero;
    player.scrollIntoView({
      behavior: "smooth",
      block: "center",
      inline: "center",
    });
    lives.textContent = data.livesRemaining.toString();
    keys.textContent = data.numKeysRetrieved.toString();
  });
  connection.addEventListener("close", () => {
    if (!hasWon) {
      loseCallback();
    }
  });
  registerListeners(connection);
};
