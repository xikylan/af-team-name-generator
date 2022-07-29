import './App.css';
import { Button } from '@appfolio/react-gears';
import HomeScreen from "./components/HomeScreen";


function App() {
  return (
    <div className="App"  style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '75vh',
    }}>
        <HomeScreen/>
    </div>
  );
}

export default App;
