import './assets/styles/main.scss'
import Frame from './Frame'
import { Info } from './Info'
import Instances from './Instances'
import { SnackbarProvider } from 'notistack'


function App() {
  return (
    <SnackbarProvider>
      <Frame title="Challenges" subtitle="Launch instances">
        <Info>
          <p>
            All challenge instances have a duration of 5 minutes. You may initiate a new instance only after the previous one has stopped.
          </p>
          <p>
            Every instance is associated with your team's CTFd account. You must be logged in to access the launcher.
          </p>
        </Info>
        <Instances />
      </Frame>
    </SnackbarProvider>
  )
}

export default App
