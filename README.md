NERVbot

MAGI Access Terminal — an Evangelion-inspired AI chatbot powered by the Groq API.

Features
Terminal-based chatbot
NERV-themed interface
Powered by Groq's Llama 3.3 70B model
Environment variable support through .env
Basic input filtering
Installation

Clone the repository:

git clone https://github.com/floresephraimjoshua-debug/NERVbot.git
cd NERVbot

Install dependencies:

pip install requests python-dotenv
Setup

Create a .env file:

GROQ_API_KEY=your_api_key
SYSTEM_SETTINGS=your_custom_system_prompt
Run
python NERVbot.py