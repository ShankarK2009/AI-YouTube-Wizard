from .gemini_client import gemini_generate

def to_blog_post(transcript):
    """Convert transcript to a blog post."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Rewrite the following YouTube transcript as a well-structured blog post. "
        "Use paragraphs, headings, and make it engaging.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)
def to_tweet_thread(transcript):
    """Convert transcript to a tweet thread."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Rewrite the following YouTube transcript as a Twitter/X thread. "
        "Break it into 5-10 concise tweets.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def to_linkedin_post(transcript):
    """Convert transcript to a LinkedIn post."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Rewrite the following YouTube transcript as a LinkedIn post. "
        "Make it professional and engaging.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def to_slide_deck(transcript):
    """Convert transcript to a slide deck."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Rewrite the following YouTube transcript as a slide deck. "
        "List slide titles and bullet points for each slide.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def to_instagram_caption(transcript):
    """Convert transcript to an Instagram caption."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Rewrite the following YouTube transcript as a catchy Instagram caption. "
        "Keep it short and engaging.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt) 