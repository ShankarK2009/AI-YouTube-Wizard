from gemini_client import gemini_generate

def generate_quiz(transcript):
    """Generate a quiz from the transcript."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Create a short quiz (3-5 questions) based on the following YouTube transcript. "
        "Return questions only, no answers.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def explain_like_five(transcript):
    """Explain the content like you're five years old."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Explain the main ideas of the following YouTube transcript as if you are talking to a five-year-old. "
        "Use simple language.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def extract_vocabulary(transcript):
    """Extract vocabulary words from the transcript."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Extract a list of important vocabulary words from the following YouTube transcript. "
        "Return as a bullet list.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt) 