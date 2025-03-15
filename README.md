# Lumi - AI Chatbot 🤖

A modern, interactive AI chatbot powered by Google's Gemini AI. Built with Streamlit and Python, Lumi provides engaging conversations with a beautiful, user-friendly interface.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Site-blue)](your-deployment-url-here)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io/)

![Lumi Chat Interface](screenshot-url-here) <!-- Add your screenshot URL here -->

## 🌟 Features

- 💬 Real-time chat interface
- ⚡ Streaming responses with typing animation
- 🧠 Context-aware conversations
- 🎨 Clean and modern UI
- 📱 Mobile-responsive design
- 🔄 Persistent chat history
- 🛡️ Error handling and recovery

## 🚀 Live Demo

Try out Lumi here: [Live Demo](your-deployment-url-here)

## 📋 Prerequisites

- Python 3.9 or higher
- Google API Key (Gemini AI)
- Git (optional)

## 🛠️ Installation

1. **Clone the repository** (or download the ZIP)
   ```bash
   git clone https://github.com/yourusername/lumi-chatbot.git
   cd lumi-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## 🎮 Usage

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Access the chat interface**
   - Open your browser and go to `http://localhost:8501`
   - Start chatting with Lumi!

## 🔑 Getting API Keys

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to your `.env` file

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Create a [Streamlit Cloud](https://streamlit.io/cloud) account
2. Connect your GitHub repository
3. Add your `GOOGLE_API_KEY` to Streamlit Cloud secrets
4. Deploy your app

### Alternative Deployment Options

- **Heroku**: Follow [Heroku's Python deployment guide](https://devcenter.heroku.com/articles/getting-started-with-python)
- **Railway**: Use [Railway's automated deployment](https://railway.app/)
- **DigitalOcean**: Deploy using [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dhruv**
- AI/ML Software Developer
- [GitHub Profile](https://github.com/yourusername)
- [LinkedIn](https://linkedin.com/in/yourusername)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/lumi-chatbot/issues).

## 💖 Support

Give a ⭐️ if this project helped you!