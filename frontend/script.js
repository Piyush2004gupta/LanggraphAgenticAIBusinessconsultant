document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatHistory = document.getElementById('chat-history');
    const sendBtn = document.getElementById('send-btn');

    // Connects to the FastAPI backend
    async function fetchAgentResponse(query) {
        const res = await fetch('http://localhost:8000/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query })
        });
        
        if (!res.ok) {
            throw new Error(`API error: ${res.status}`);
        }
        
        const data = await res.json();
        return data.response;
    }

    function addMessageToUI(sender, text) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);

        const avatar = document.createElement('div');
        avatar.classList.add('avatar');
        avatar.textContent = sender === 'user' ? 'U' : 'AI';

        const bubble = document.createElement('div');
        bubble.classList.add('bubble');
        
        if (text === null) {
            // Add loading state
            bubble.innerHTML = `
                <div class="loading-dots">
                    <span></span><span></span><span></span>
                </div>
            `;
            bubble.id = 'loading-bubble';
        } else {
            // Render text, preserving newlines
            bubble.innerHTML = text.replace(/\n/g, '<br>');
        }

        messageDiv.appendChild(avatar);
        messageDiv.appendChild(bubble);
        chatHistory.appendChild(messageDiv);
        
        // Scroll to bottom
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }

    function removeLoadingMessage() {
        const loadingBubble = document.getElementById('loading-bubble');
        if (loadingBubble) {
            loadingBubble.closest('.message').remove();
        }
    }

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const query = userInput.value.trim();
        if (!query) return;

        // 1. Show user message
        addMessageToUI('user', query);
        userInput.value = '';
        
        // Disable input while generating
        userInput.disabled = true;
        sendBtn.disabled = true;

        // 2. Show loading animation
        addMessageToUI('system', null);

        try {
            // 3. Fetch response from Agent Backend
            const response = await fetchAgentResponse(query);
            
            // 4. Remove loading and show actual response
            removeLoadingMessage();
            addMessageToUI('system', response);
            
        } catch (error) {
            removeLoadingMessage();
            addMessageToUI('system', 'Sorry, I encountered an error connecting to the agent backend.');
            console.error('Agent Error:', error);
        } finally {
            // Re-enable input
            userInput.disabled = false;
            sendBtn.disabled = false;
            userInput.focus();
        }
    });
});
