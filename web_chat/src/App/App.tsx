import { useEffect, useState } from 'react';
import './App.css';
import AppContext from '../utils/AppContext';
import { BASE_API_URL } from '../utils/constants';
import IAppContext from '../utils/IAppContext';
import { Outlet } from 'react-router-dom';

function App() {
  const [appContextValue, setAppContextValue] = useState<IAppContext>({});
  useEffect(() => {
    fetch(`${BASE_API_URL}/getUserAndBotInfo`, {
      method: 'GET', 
    })
      .then((resp) => resp.json())
      .then((response) => {
        setAppContextValue({
          ...appContextValue,
          bot: response.bot,
          user: response.user,
        });
      });
  }, []) // eslint-disable-line react-hooks/exhaustive-deps
  useEffect(() => {
    // TODO: ask user something in case of inactivity for 1 min.
  }, [])

  return (    
    <AppContext.Provider value={appContextValue}>
        <div className="App">
            <header>AI Replica</header>
            <Outlet />
            <footer>AI Replica</footer>
        </div>
    </AppContext.Provider>
  );
}

export default App;
