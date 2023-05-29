import './style.scss'
import { setupWithWebSocket } from './render.ts'

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
<article>
  <main>
    <section id="player" data-direction="up"></section>
    <div id="sizer"></div>
  </main>
  <footer>
    Lives: <span id="lives">3</span>, Keys: <span id="keys">0</span> / <span id="totalKeys">10</span>
  </footer>
</article>
`

setupWithWebSocket();