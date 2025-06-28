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

# Understanding
with st.sidebar.expander("Understanding", expanded=True):
    summary = st.checkbox("Summary", value=True)
    chapters = st.checkbox("Chapters")
    key_takeaways = st.checkbox("Key Takeaways", value=True)

# Learning
with st.sidebar.expander("Learning"):
    quiz = st.checkbox("Quiz")
    explain5 = st.checkbox("Explain Like Five")
    vocab = st.checkbox("Vocabulary")

# Content Repurposing
with st.sidebar.expander("Content Repurposing"):
    blog = st.checkbox("Blog Post")
    tweet = st.checkbox("Tweet Thread")
    linkedin = st.checkbox("Linkedin Post")
    slides = st.checkbox("Slide Deck")
    insta = st.checkbox("Instagram Caption")

# Analysis
with st.sidebar.expander("Analysis"):
    sentiment = st.checkbox("Sentiment Analysis")
    emotion = st.checkbox("Emotion Detection")
    comments = st.checkbox("Comments Analysis")

# Engagement
with st.sidebar.expander("Engagement"):
    qa = st.checkbox("Qa Questions")

st.sidebar.markdown("## Export Options")
st.sidebar.selectbox("Export format", options=["md"], index=0, disabled=True)

if st.sidebar.button("Run Analysis"):
    if not video_url:
        st.error("Please enter a YouTube URL.")
        st.stop()
    try:
        video_id = extract_video_id(video_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video.")
        st.stop()
    except NoTranscriptFound:
        st.error("No transcript found for this video in the requested language(s).")
        st.stop()
    except VideoUnavailable:
        st.error("Video unavailable.")
        st.stop()
    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()

    st.header("Results")
    if summary:
        st.subheader("Summary")
        st.write(generate_summary(transcript))
    if chapters:
        st.subheader("Chapters")
        st.write(extract_chapters(transcript))
    if key_takeaways:
        st.subheader("Key Takeaways")
        st.write(extract_key_takeaways(transcript))
    if quiz:
        st.subheader("Quiz")
        st.write(generate_quiz(transcript))
    if explain5:
        st.subheader("Explain Like Five")
        st.write(explain_like_five(transcript))
    if vocab:
        st.subheader("Vocabulary")
        st.write(extract_vocabulary(transcript))
    if blog:
        st.subheader("Blog Post")
        st.write(to_blog_post(transcript))
    if tweet:
        st.subheader("Tweet Thread")
        st.write(to_tweet_thread(transcript))
    if linkedin:
        st.subheader("Linkedin Post")
        st.write(to_linkedin_post(transcript))
    if slides:
        st.subheader("Slide Deck")
        st.write(to_slide_deck(transcript))
    if insta:
        st.subheader("Instagram Caption")
        st.write(to_instagram_caption(transcript))
    if sentiment:
        st.subheader("Sentiment Analysis")
        st.write(sentiment_analysis(transcript))
    if emotion:
        st.subheader("Emotion Detection")
        st.write(emotion_detection(transcript))
    if comments:
        st.subheader("Comments Analysis")
        st.write(comments_analysis(transcript))
    if qa:
        st.subheader("QA Questions")
        st.write(generate_qa_questions(transcript))