import { useEffect, useState } from 'react';
import './App.css';
import Chat from '../Chat/Chat';
import SideSection from '../SideSection/SideSection';
import AppContext from '../utils/AppContext';
import { BASE_API_URL } from '../utils/constants';
import IAppContext from '../utils/IAppContext';
import HomePage from '../HomePage/HomePage';

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
        <HomePage />
    </AppContext.Provider>
  );
}

export default App;
