const botInfo = document.getElementById("botInfo");

// TODO: Provide a user possibility to choose a bot with whom to talk.
let currentBot;

const onWindowLoad =  async (event) => {
  const userAndBotInfoResponse = await fetch("/getUserAndBotInfo", {method: "GET"})
    .then((resp) => resp.json());
  const userId = userAndBotInfoResponse.user.id;
  currentBot = userAndBotInfoResponse.bot;
  const botId = userAndBotInfoResponse.bot.id;
  
  const response = await fetch("/getConversationHistory?$top=1000", {
    method: 'GET', 
  })
    .then((resp) => resp.json());
  
  let lastAddedMessage;
  response.forEach((utterance) => {
    if (utterance.user_id === userId) {
      const userMessage = [{"type": "text", "content": utterance.text}];
          
      lastAddedMessage = addMessage(messages, userMessage, "You", "user-message");
    } else if (utterance.user_id === botId) {
      const botResponse = JSON.parse(utterance.text);
      const botMessages = botResponse.messages || [];
      botMessages.forEach((message) => {
        lastAddedMessage = addMessage(messages, message, currentBot.name, "bot-message");
      });
    }
    if (lastAddedMessage) {
      lastAddedMessage.scrollIntoView(false);
    }    
  });
  renderBotInfo();
};

const renderBotInfo = () => {
  botInfo.innerHTML = `Hello, I am ${currentBot.name}.`;
}

window.addEventListener('load', onWindowLoad);

const sendMessageButton = document.getElementById("sendMessageButton");
sendMessageButton.addEventListener("click", onSendMessageButtonClicked);

const messages = document.getElementById("messages");

const messageInput = document.getElementById("messageInput");

async function onSendMessageButtonClicked(event) {
  const userMessage = [{"type": "text", "content": messageInput.value}];
  messageInput.value = "";

  const addedMessage = addMessage(messages, userMessage, "You", "user-message");
  addedMessage.scrollIntoView(false);

  // TODO: for now, send only text messages to the server
  // Think how to add images and links to be processed by the server/bot.
  const requestData = { message: userMessage[0].content };
  const response = await fetch("/getResponse", {
    method: 'POST', 
    body: JSON.stringify(requestData),
  });
  const botResponse = await response.json();
  const botMessages = botResponse.messages || [];
  botMessages.forEach((message) => {
    const addedMessage = addMessage(messages, message, currentBot.name, "bot-message");
    addedMessage.scrollIntoView(false);
  });
}

function addMessage(messagesElement, messageParts, userName, modifier) {
  const messageElement = document.createElement("article");
  messageElement.className = `message message_${modifier}`;
  let messageHtml = `<section class="message-name">${userName}: </section>`;
  messageHtml += '<section>';
  messageParts.forEach((messagePart) => {
    switch (messagePart.type) {
      case "text":
        messageHtml += messagePart.content;
        break;
      case "image":
        messageHtml += `<img class="message__image" src='${messagePart.content}' />`;
        break;
      case "link":
        messageHtml += `<a href='${messagePart.link}' target='blank'>${messagePart.text}</a>`;
        break;
    }
  });

  messageHtml += '</section>';
  messageElement.innerHTML = messageHtml;
  messagesElement.appendChild(messageElement);

  return messageElement;
}
