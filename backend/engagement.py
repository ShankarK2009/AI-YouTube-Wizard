from .gemini_client import gemini_generate

def generate_qa_questions(transcript):
    """Generate QA questions from the transcript."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Generate 3-5 thoughtful QA questions based on the following YouTube transcript. "
        "Return as a bullet list.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)