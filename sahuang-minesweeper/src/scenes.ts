import { animateCloud } from './clouds.ts';
import { setupWithWebSocket } from './render.ts'

export function renderTitle() {
    document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
        <article class="title">
            <h1>Minesweeper Adventure</h1>
            <section>
                <p>Conubia curabitur metus integer cubilia tempor lorem facilisis mattis rutrum euismod, justo bibendum orci ultrices tincidunt odio nulla commodo.</p>
                <button id="start">Start</button>
            </section>
        </article>
    `;
    const stopAnimation = animateCloud();

    document.querySelector<HTMLButtonElement>('#start')!.addEventListener('click', () => {
        stopAnimation();
        renderField();
    });
}

export function renderField() {
    document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
        <article id="field">
            <main>
                <section id="player" data-direction="up"></section>
                <div id="sizer"></div>
            </main>
            <footer>
                <div><b>Lives</b>: <span id="lives">3</span></div>
                <div><b>Level</b>: <span id="level">3</span></div>
                <div><b>Keys</b>: <span id="keys">0</span> / <span id="totalKeys">10</span></div>
                
            </footer>
        </article>
    `;

    setupWithWebSocket(renderWin, renderLose);
}

export function renderWin(flag: string) {
    document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
        <article class="title">
            <h1>You win!</h1>
            <section>
                <p>Flag: <code>${flag}</code></p>
            </section>
        </article>
    `;
    animateCloud();
}

export function renderLose() {
    document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
    <article class="title">
        <h1>You lose.</h1>
        <section>
            <p>Conubia curabitur metus integer cubilia tempor lorem facilisis mattis rutrum euismod, justo bibendum orci ultrices tincidunt odio nulla commodo.</p>
            <button id="restart">Restart</button>
        </section>
    </article>
    `;
    const stopAnimation = animateCloud();

    document.querySelector<HTMLButtonElement>('#restart')!.addEventListener('click', () => {
        stopAnimation();
        renderField();
    });
}