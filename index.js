const ChatWindowElement = document.getElementsByClassName("ChatWindow")[0];
const sendButton = document.getElementsByClassName("SendButton")[0];
const input = document.getElementById("input");

const addBotMessage = (content) => {
  const newMessage = document.createElement("div");
  newMessage.className = "Message Bot";

  const now = new Date();
  const hours = String(now.getHours()).padStart(2, "0");
  const minutes = String(now.getMinutes()).padStart(2, "0");
  const currentTime = `${hours}:${minutes}`;

  newMessage.innerHTML = content + `<sub> ${currentTime}</sub> `;
  ChatWindowElement.appendChild(newMessage);
};

const addUserMessage = () => {
  const content = input.value.trim();
  if (content !== "") {
    const newMessage = document.createElement("div");
    newMessage.className = "Message User";

    const now = new Date();
    const hours = String(now.getHours()).padStart(2, "0");
    const minutes = String(now.getMinutes()).padStart(2, "0");
    const currentTime = `${hours}:${minutes}`;

    newMessage.innerHTML = content + `<sub> ${currentTime}</sub> `;
    ChatWindowElement.appendChild(newMessage);
  }
};

sendButton.addEventListener("click", addUserMessage);
