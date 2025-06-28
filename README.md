# 🧙‍♂️ AI YouTube Wizard

> **Transform YouTube videos into actionable insights and repurposed content with AI-powered analysis**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)](https://streamlit.io)
[![Gemini AI](https://img.shields.io/badge/Gemini%20AI-Powered-green.svg)](https://ai.google.dev/gemini)

## 🚀 Try It Live

**[AI YouTube Wizard - Live Demo](https://ai-youtube-wizard.streamlit.app)**

## 📖 What is AI YouTube Wizard?

AI YouTube Wizard is an intelligent tool that extracts transcripts from YouTube videos and uses Google's Gemini AI to transform them into various useful formats. Whether you're a content creator, educator, researcher, or just someone who wants to get more value from YouTube content, this tool helps you understand, learn from, and repurpose video content efficiently.

## ✨ Key Features

### 🧠 **Understanding**

- **📝 Smart Summaries** - Generate detailed, multi-sentence summaries
- **📚 Chapter Extraction** - Automatically identify and organize content sections
- **🎯 Key Takeaways** - Extract main points and insights as bullet points

### 🎓 **Learning Tools**

- **❓ Quiz Generation** - Create educational quizzes from video content
- **👶 Explain Like Five** - Simplify complex topics for easy understanding
- **📖 Vocabulary Lists** - Extract important terms and concepts

### 🔄 **Content Repurposing**

- **📝 Blog Posts** - Convert videos into well-structured articles
- **🐦 Tweet Threads** - Create engaging Twitter/X content threads
- **💼 LinkedIn Posts** - Generate professional social media content
- **📊 Slide Decks** - Transform content into presentation format
- **📸 Instagram Captions** - Create catchy social media captions

### 📊 **Analysis & Insights**

- **😊 Sentiment Analysis** - Understand the emotional tone of content
- **🎭 Emotion Detection** - Identify specific emotions expressed
- **💬 Comments Analysis** - Analyze discussion themes and topics

### 🤝 **Engagement**

- **❓ Q&A Questions** - Generate thoughtful discussion questions

## 🛠️ Technology Stack

- **Backend**: Python 3.8+
- **AI Engine**: Google Gemini AI
- **Web Interface**: Streamlit
- **YouTube Integration**: YouTube Transcript API
- **Environment**: Python-dotenv for configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- YouTube video with available transcripts

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/ShankarK2009/AI-YouTube-Wizard.git
   cd ai-youtube-wizard
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**

   ```bash
   # Create a .env file in the project root
   echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
   ```

4. **Run the web application**
   ```bash
   cd frontend
   streamlit run app.py
   ```

### Command Line Usage

You can also use the tool via command line:

```bash
# Generate a summary
python backend/cli.py "https://youtube.com/watch?v=VIDEO_ID" --feature summary

# Create a blog post
python backend/cli.py "https://youtube.com/watch?v=VIDEO_ID" --feature blog_post

# Generate a quiz
python backend/cli.py "https://youtube.com/watch?v=VIDEO_ID" --feature quiz
```

## 🎯 Use Cases

### For Content Creators

- **Repurpose long-form content** into multiple social media formats
- **Generate blog posts** from video content
- **Create engaging captions** for different platforms

### For Educators

- **Create quizzes** from educational videos
- **Simplify complex topics** for different age groups
- **Extract key learning points** for lesson planning

### For Researchers

- **Analyze sentiment** of video content
- **Extract main themes** and topics
- **Generate discussion questions** for research

### For Students

- **Create study materials** from educational videos
- **Understand complex topics** through simplified explanations
- **Build vocabulary** from subject-specific content

## 🔧 Configuration

The tool uses environment variables for configuration:

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

## 📁 Project Structure

```
AI-YouTube-Wizard/
├── backend/                 # Core AI processing modules
│   ├── analysis.py         # Sentiment and emotion analysis
│   ├── cli.py             # Command-line interface
│   ├── engagement.py      # Q&A generation
│   ├── gemini_client.py   # Gemini AI integration
│   ├── learning.py        # Educational tools
│   ├── repurposing.py     # Content transformation
│   └── understanding.py   # Summary and insights
├── frontend/              # Streamlit web interface
│   └── app.py            # Main web application
├── exports/              # Generated content storage
└── requirements.txt      # Python dependencies
```

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the AI capabilities
- **YouTube Transcript API** for video transcript extraction
- **Streamlit** for the beautiful web interface
- **Open Source Community** for inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/ShankarK2009/AI-YouTube-Wizard/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

---

**Made with ❤️ by Shankar and Lakshan**

_Transform your YouTube experience with AI-powered insights!_
