import streamlit as st
import sys
import os

# Add backend to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import re

from understanding import generate_summary, extract_chapters, extract_key_takeaways
from learning import generate_quiz, explain_like_five, extract_vocabulary
from repurposing import to_blog_post, to_tweet_thread, to_linkedin_post, to_slide_deck, to_instagram_caption
from analysis import sentiment_analysis, emotion_detection, comments_analysis
from engagement import generate_qa_questions

def extract_video_id(url_or_id: str) -> str:
    match = re.search(r"(?:v=|youtu.be/)([\w-]{11})", url_or_id)
    if match:
        return match.group(1)
    if len(url_or_id) == 11:
        return url_or_id
    raise ValueError("Could not extract video ID from input.")

st.set_page_config(page_title="AI YouTube Wizard", layout="wide")
st.sidebar.title("YouTube Video Input")
video_url = st.sidebar.text_input("Paste YouTube URL here:")