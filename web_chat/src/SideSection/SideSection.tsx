import { useContext } from 'react';
import { Link } from 'react-router-dom';
import AppContext from '../utils/AppContext';
import './SideSection.css'

function SideSection() {
  const appContext = useContext(AppContext)
  const bot = appContext.bot;

  return (
    <section className="SideSection">
      <section id="avatar">
        <img src="avatar.gif" alt="Avatar"/>
      </section>
      <div id="botInfo">
        Hello, I am {bot && bot.name}
      </div>
      <div id="testPageLinkWrapper">
        <Link to="/test">Test Page</Link>
      </div>
    </section>
  );
}

export default SideSection;
