document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('question-form');
    const chatbox = document.querySelector('.chatbox');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const responseInput = document.getElementById('response');
        const response = responseInput.value.trim(); // Get user response

        if (response !== '') {
            // Create a new chat message element for the user's response
            const userMessage = document.createElement('li');
            userMessage.classList.add('chat-outgoing', 'chat');
            userMessage.innerHTML = `<p>${response}</p>`;
            chatbox.appendChild(userMessage);

            // Clear the response input field
            responseInput.value = '';

            // Submit the form asynchronously
            const formData = new FormData(form);
            fetch('/result', {
                method: 'POST',
                body: formData
            })
            .then(response => response.text())
            .then(data => {
                // Update the chat interface with the next question or MBTI result
                chatbox.innerHTML += data;
                // Scroll to the bottom of the chatbox
                chatbox.scrollTop = chatbox.scrollHeight;
            })
            .catch(error => console.error('Error:', error));
        }
    });
});
