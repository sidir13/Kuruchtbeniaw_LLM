document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    
    // Display user message
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div><b>Vous:</b> ${userInput}</div>`;
    
    // Clear the text field after sending
    document.getElementById('user-input').value = '';

    // Api call to get model message
    fetch('http://127.0.0.1:5555/predict', {  
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: userInput  // Input from user
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display model messages
        const botResponse = data.response;  // Get respond
        chatBox.innerHTML += `<div><b>Bot:</b> ${botResponse}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;  // scroll down
    })
    .catch(error => {
        console.error('Erreur:', error);
    });
});
