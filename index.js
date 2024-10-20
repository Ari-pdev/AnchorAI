const ChatWindowElement = document.getElementsByClassName("ChatWindow")[0];
const sendButton = document.getElementsByClassName("SendButton")[0];
const input = document.getElementById("input");

const waitText = "The bot is responding, sit back and wait...";
const regularText = input.placeholder;

const lockInput = () => {
  input.classList.add("Disabled");
  input.disabled = true;
  input.placeholder = waitText;
};
const unlockInput = () => {
  input.classList.remove("Disabled");
  input.disabled = false;
  input.placeholder = regularText;
};

const addBotMessage = (content) => {
  const newMessage = document.createElement("div");
  newMessage.className = "Message Bot";

  const now = new Date();
  const hours = String(now.getHours()).padStart(2, "0");
  const minutes = String(now.getMinutes()).padStart(2, "0");
  const currentTime = `${hours}:${minutes}`;

  newMessage.innerHTML = content + `<sub> ${currentTime}</sub> `;
  ChatWindowElement.appendChild(newMessage);
  unlockInput();
};

const addUserMessage = () => {
  const content = input.value.trim();
  input.value = "";

  if (content !== "") {
    lockInput();
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

input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    addUserMessage();
  }
});
