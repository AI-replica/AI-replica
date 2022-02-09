const sendMessageButton = document.getElementById("sendMessageButton");
sendMessageButton.addEventListener("click", onSendMessageButtonClicked);

const messages = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");

async function onSendMessageButtonClicked(event) {
  const userMessage = messageInput.value;
  messageInput.value = "";

  const addedMessage = addMessage(messages, userMessage, "You", "user-message");
  addedMessage.scrollIntoView(false);

  const requestData = { message: userMessage };
  const response = await fetch("/getResponse", {
    method: 'POST', 
    body: JSON.stringify(requestData),
  });
  const botResponse = await response.json();
  const botMessages = botResponse.messages || [];
  botMessages.forEach((message) => {
    const addedMessage = addMessage(messages, message, "Bot", "bot-message");
    addedMessage.scrollIntoView(false);
  });
}

function addMessage(messagesElement, messageText, userName, modifier) {
  const messageElement = document.createElement("article");
  messageElement.className = `message message_${modifier}`;
  messageElement.innerHTML = `
    <section class="message-name">${userName}: </section>
    <section>${messageText}</section>
  `;

  messagesElement.appendChild(messageElement);

  return messageElement;
}
