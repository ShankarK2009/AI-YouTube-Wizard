from .gemini_client import gemini_generate

def sentiment_analysis(transcript):
    """Perform sentiment analysis on the transcript."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Analyze the overall sentiment of the following YouTube transcript. "
        "Return one word: Positive, Negative, or Neutral.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def emotion_detection(transcript):
    """Detect emotions in the transcript."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Detect the main emotion expressed in the following YouTube transcript. "
        "Return one word (e.g., Happy, Sad, Excited, Calm, etc.).\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def comments_analysis(transcript):
    """Analyze comments (placeholder, as transcript has no comments)."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Pretend the following YouTube transcript is a set of comments. "
        "Analyze for common themes or topics.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt) 