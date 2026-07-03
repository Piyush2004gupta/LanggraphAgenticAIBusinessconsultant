import { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    { sender: 'system', text: 'Hello! I am your AI Business Consultant. How can I help you analyze your business ideas today? (e.g. "Online food delivery startup in India")' }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const chatHistoryRef = useRef(null);

  useEffect(() => {
    if (chatHistoryRef.current) {
      chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
    }
  }, [messages, isLoading]);

  const fetchAgentResponse = async (query) => {
    const res = await fetch('/api/analyze', {
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
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const query = inputValue.trim();
    if (!query) return;

    setMessages((prev) => [...prev, { sender: 'user', text: query }]);
    setInputValue('');
    setIsLoading(true);

    try {
      const response = await fetchAgentResponse(query);
      setMessages((prev) => [...prev, { sender: 'system', text: response }]);
    } catch (error) {
      console.error('Agent Error:', error);
      setMessages((prev) => [...prev, { sender: 'system', text: 'Sorry, I encountered an error connecting to the agent backend.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <div className="background-animation"></div>
      
      <div className="container">
        <header>
          <h1>AI Business Consultant</h1>
          <p>Your intelligent partner for strategic analysis and growth</p>
        </header>

        <main>
          <div className="chat-container">
            <div className="chat-history" ref={chatHistoryRef}>
              {messages.map((msg, index) => (
                <div key={index} className={`message ${msg.sender}`}>
                  <div className="avatar">{msg.sender === 'user' ? 'U' : 'AI'}</div>
                  <div className="bubble">
                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                  </div>
                </div>
              ))}
              
              {isLoading && (
                <div className="message system">
                  <div className="avatar">AI</div>
                  <div className="bubble" id="loading-bubble">
                    <div className="loading-dots">
                      <span></span><span></span><span></span>
                    </div>
                  </div>
                </div>
              )}
            </div>

            <div className="input-area">
              <form id="chat-form" onSubmit={handleSubmit}>
                <input 
                  type="text" 
                  id="user-input" 
                  placeholder="Enter your business query..." 
                  required 
                  autoComplete="off"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  disabled={isLoading}
                />
                <button type="submit" id="send-btn" disabled={isLoading}>
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                </button>
              </form>
            </div>
          </div>
        </main>
      </div>
    </>
  );
}

export default App;
