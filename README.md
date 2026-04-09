🤖 Gemini AI Chatbot
A simple and interactive web-based AI chatbot powered by Google's Gemini 2.5 Flash model. Chat with AI directly from your browser using a lightweight Flask backend.

✨ Features
•	🌙 Clean and modern dark-themed UI
•	⚡ Fast real-time AI responses
•	🧠 Powered by Gemini 2.5 Flash
•	🔗 LangChain integration for easy model usage
•	🖥 Runs locally with minimal setup


📱 Demo
+---------------------------+
| Gemini AI Bot             |
|                           |
| > Ask something... [Ask]  |
|                           |
| AI Reply: ...             |
+---------------------------+

🛠 Prerequisites
Make sure you have:
•	Python 3.8 or higher
•	Google AI API Key (free tier available)

🚀 Quick Start
1. Clone the Repository
git clone https://github.com/yourusername/GENAI.git
cd GENAI
2. Install Dependencies
pip install -r requirements.txt
3. Setup Environment Variables
Create a .env file in the root directory:
GOOGLE_API_KEY=your_api_key_here
Get your API key from:
👉 https://aistudio.google.com/app/apikey
4. Run the Application
python app.py
5. Open in Browser
http://127.0.0.1:5000

🏗 Project Structure
GENAI/
├── app.py              # Flask backend + Gemini integration
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
├── .env                # API keys (not committed)
└── templates/
    └── index.html      # Chat UI


🔧 Customization
Change model in app.py:
model = "gemini-2.5-flash"
Modify UI in:
templates/index.html
Add chat history:
Extend backend using sessions or database

⚠️ Important Notes
Keep your .env file private (do not upload to GitHub)
API usage is subject to Google rate limits
Designed for learning and lightweight applications

