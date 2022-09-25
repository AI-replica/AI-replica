export default interface IMessageProps {
  message: {
    modifier?: string;
    userName: string;
    content: any[];
  }
  isTyping?: boolean;
}
