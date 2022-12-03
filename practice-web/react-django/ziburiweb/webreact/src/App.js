import './App.css';
import Detail from './component/Detail';
import Footer from './component/Footer';
import Header from './component/Header';
import Main from './component/Main';
import Window from './component/Window';
import WindowRe from './component/WindowRe';
import ApiContextProvider from "./context/ApiContext";

function App() {
  return (
    <div className="App">
      <ApiContextProvider>
        <Header />
        <Window />
        <Main />
        <Detail />
        <WindowRe />
        <Footer />
      </ApiContextProvider>
    </div>
  );
}

export default App;
