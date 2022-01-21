const sendMessageButton = document.getElementById("sendMessageButton");
sendMessageButton.addEventListener("click", onSendMessageButtonClicked);

const messages = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");

async function onSendMessageButtonClicked(event) {
  const userMessage = messageInput.value;
  messageInput.value = "";

  addMessage(messages, userMessage, "You", "user-message");

  const requestData = { message: userMessage };
  const response = await fetch("/getResponse", {
    method: 'POST', 
    body: JSON.stringify(requestData),
  });
  const botMessage = await response.json();
  addMessage(messages, botMessage.message, "Bot", "bot-message");
}

function addMessage(messagesElement, messageText, userName, modifier) {
  const botMessageElement = document.createElement("article");
  botMessageElement.className = `message message_${modifier}`;
  botMessageElement.innerHTML = `
    <section class="message-name">${userName}: </section>
    <section>${messageText}</section>
  `;

  messagesElement.appendChild(botMessageElement);
}
