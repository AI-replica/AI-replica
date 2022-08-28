import { useContext, useEffect, useRef, useState } from 'react';
import AppContext from "../utils/AppContext";
import { BASE_API_URL } from '../utils/constants';
import Message from '../Message/Message';

import './Chat.css'

function Chat() {
  const appContext = useContext(AppContext)
  const bot = appContext.bot;
  const user = appContext.user;
  const [messages, setMessages] = useState<any[]>([]);
  const [userMessageText, setUserMessageText] = useState("");
  const [botIsTyping, setBotIsTyping] = useState(false);
  const messagesElementRef = useRef<HTMLElement|undefined>();
  const audioElementRef = useRef<HTMLAudioElement|null>(null);
  
  useEffect(() => {
    if (!bot || !user) {
      return
    }

    fetch(`${BASE_API_URL}/getConversationHistory?$top=1000`, {
      method: 'GET', 
    })
      .then((resp) => resp.json())
      .then((response) => {
        const conversationMessages = response.reduce((acc: any[], utterance: any) => {
          if (utterance.user_id === user?.id) {
            const userMessage = {
              userName: user?.id, 
              modifier:  "user-message",
              content: [{"type": "text", "content": utterance.text}]
            };
            return [...acc, userMessage];
          } else if (utterance.user_id === bot?.id) {
            const botResponse = JSON.parse(utterance.text);
            const botMessages = (botResponse.messages || []).map((message: any) => {
              return {
                userName: bot?.name,
                modifier: "bot-message",
                content: message,
              };
            })
            return [...acc, ...botMessages];
          }

          return acc;
        }, []);
        setMessages(conversationMessages);
        scrollToTheLatestMessage();
      })
  }, [bot, user]);
  const handleSendClick = (event: any) => {
    const userMessage = {
      userName: user?.id,
      modifier: "user-message",
      content: [{"type": "text", "content": userMessageText}]
    };
    setUserMessageText("");
    setMessages([...messages, userMessage]);
    scrollToTheLatestMessage();

    // for now, let's assume that bot always replies to a user right after user asks something
    // later, it can be that the bot will provide the answer later.
    // later, we can detect when the bot starts actual message processing and display notification that time only
    // so display Typing notifictaion right after the request is sent.
    setBotIsTyping(true);
    // TODO: for now, send only text messages to the server
    // Think how to add images and links to be processed by the server/bot.
    const requestData = { message: userMessage.content[0].content };
    fetch(`${BASE_API_URL}/getResponse`, {
      method: 'POST', 
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json())
      .then(async (botResponse) => {
        const botMessages = (botResponse.messages || []).map((message: any) => {
          return {
            userName: bot?.name,
            modifier: "bot-message",
            content: message
          }
        }) as any[];
        // emulate bot typing, i.e. emulate that the bot i styoing message
        // await emulateBotTyping();
        setMessages((prevMessages: any[]) => [...prevMessages, ...botMessages])
        scrollToTheLatestMessage();
        playVoiceMessage(botResponse.guid);
      })
      .catch((error) => {
        console.log("Error occured while getting response", error);
      })
      .finally(() => {
        setBotIsTyping(false);
      })
  };

  const handleMessageInputChange = (event: any) => {
    setUserMessageText(event.target.value);
  };

  const scrollToTheLatestMessage = () => {
    // TODO: find a better way to detect that inserted messages are rendered and scroll only after all the messages are rendered.
    // For now, we assume that the rendering happens within 20ms.
    setTimeout(() => {
      if(!messagesElementRef.current) {
        return;
      }

      messagesElementRef.current.scrollIntoView(false)
    }, 50);
  };

  // emulates the behavior when bot is typing message
  async function emulateBotTyping() {
    return new Promise((resolve, reject) => {
      setBotIsTyping(true);
      scrollToTheLatestMessage();
      setTimeout(() => {
        setBotIsTyping(false);
        resolve(undefined);
      }, 5000)
    });
  }

  function playVoiceMessage(guid: string) {
    if (audioElementRef.current) {
      audioElementRef.current.src = `${BASE_API_URL}/generated/${guid}.mp3`;
      audioElementRef.current.play();
    }
  }

  return (
    <div className="Chat">
      <section id="messages">
        {messages.map((message, index) => (
          <Message
            message={message}
            key={index} 
            ref={messagesElementRef}
          />
        ))}
        {botIsTyping && 
        <Message
          message={{content: [], userName: bot?.name, modifier: "bot-message"}}
          isTyping={true}
          ref={messagesElementRef}
        />}
      </section>
      <section id="input">
        <textarea 
          id="messageInput" 
          className="input" 
          placeholder="Type a message..." 
          value={userMessageText}
          onChange={handleMessageInputChange}         
        ></textarea>
        <button 
          id="sendMessageButton"
          onClick={handleSendClick}
        >
          Send
        </button>
      </section>
      <audio ref={audioElementRef} id="chat_player">
        <source type="audio/mpeg" />
      </audio>
    </div>
  );
}

export default Chat;
