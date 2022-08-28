import React from "react";
import "./Message.css";
import IMessageProps from "./IMessageProps";

function Message(props: IMessageProps, ref: any) {
  const message = props.message;

  const messageContentSection = !(props?.isTyping)
      ? getMessageContent(message)
      : <div className="typing">Typing...</div>;


  return (
    <article ref={ref} className={`message message_${message.modifier}`}>
      <section className="message-name">{message.userName}: </section>
      <section>
        {messageContentSection}
      </section>
    </article>
  );
}

function getMessagePartElement(messagePart: any) {
  switch (messagePart.type) {
    case "text":
      return messagePart.content;
    case "image":
      return <img className="message__image" src={messagePart.content} alt="" />;
    case "link":
      return <a href={messagePart.link} target='blank'>{messagePart.text}</a>;
    default:
      return null;
  }
};

function getMessageContent(message: any) {
  return message.content.map((messagePart: any) => getMessagePartElement(messagePart));
}

export default React.forwardRef(Message);
