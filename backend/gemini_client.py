from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=GEMINI_API_KEY)

def gemini_generate(prompt, model="gemini-1.5-flash", max_tokens=1024):
    model = genai.GenerativeModel(model)
    response = model.generate_content(prompt, generation_config={"max_output_tokens": max_tokens})
    return response.text 