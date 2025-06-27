import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import Nav from './components/Nav.tsx'

createRoot(document.getElementById('root')!).render(
  <div className='main'>
    <Nav/>
    <App />
  </div >,
)
