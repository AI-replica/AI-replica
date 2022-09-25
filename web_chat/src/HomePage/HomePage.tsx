import Chat from "../Chat/Chat";
import SideSection from "../SideSection/SideSection";

import './HomePage.css';

function HomePage() {
    return (
        <div className="HomePage">
            <main id="chat">
                <Chat />
            </main>
            <section id="side">
                <SideSection />
            </section>
        </div>
    )
}

export default HomePage;
