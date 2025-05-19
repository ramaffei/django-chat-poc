function send(socket, type, message, username) {
    console.log("enviando mensaje")
    socket.send(JSON.stringify({ type, message, username }));
}

const username = localStorage.getItem('username');
if (!username) {
    window.location.href = '/';
}

const messagesDiv = document.getElementById('messages');
const input = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');

const socket = new WebSocket(`ws://${location.host}/ws/chat/${roomId}/`);

socket.onopen = (event) => {
    console.log(this)
    send(socket, "init", "iniciando", username)
};

console.log(socket)
socket.onmessage = (event) => {
    console.log(event)
    const data = JSON.parse(event.data);
    const msgEl = document.createElement('div');
    msgEl.classList.add('message');
    msgEl.classList.add(data.username === username ? 'sent' : 'received');
    msgEl.innerHTML = `<strong>${data.username}</strong>: ${data.message}`;
    messagesDiv.appendChild(msgEl);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
};

sendBtn.addEventListener('click', () => {
    const message = input.value.trim();
    send(socket, 'chat_message', message, username)
});
input.addEventListener('keydown', e => { if (e.key === 'Enter') {
    const message = input.value.trim(); 
    send(socket, 'chat_message', message, username);
} 
});
