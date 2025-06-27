from gemini_client import gemini_generate

def generate_summary(transcript):
    """Generate a multi-sentence summary from the transcript using Gemini."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Summarize the following YouTube transcript in a detailed, multi-sentence paragraph. "
        "Capture the main ideas and important details, not just one sentence.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def extract_chapters(transcript):
    """Extract chapters from the transcript using Gemini."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "Divide the following YouTube transcript into logical chapters or sections. "
        "Return a list of chapter titles with timestamps if possible.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt)

def extract_key_takeaways(transcript):
    """Extract key takeaways from the transcript using Gemini."""
    text = '\n'.join([entry['text'] for entry in transcript])
    prompt = (
        "List the key takeaways or main points from the following YouTube transcript. "
        "Return as a bullet list.\n\nTranscript:\n" + text
    )
    return gemini_generate(prompt) 