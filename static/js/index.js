window.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('userForm');
    const roomList = document.getElementById('roomList');

    form.addEventListener('submit', event => {
        event.preventDefault();
        const username = document.getElementById('username').value.trim();
        if (!username) return;
        localStorage.setItem('username', username);
        form.classList.add('hidden');
        roomList.classList.remove('hidden');
    });

    document.querySelectorAll('.room-link').forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault();
            const roomId = link.getAttribute('data-room-id');
            window.location.href = `/chat/${roomId}/`;
        });
    });
});