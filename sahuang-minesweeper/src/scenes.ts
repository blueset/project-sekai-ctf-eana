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
                Lives: <span id="lives">3</span>, Keys: <span id="keys">0</span> / <span id="totalKeys">10</span>
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