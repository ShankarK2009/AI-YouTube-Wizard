import argparse
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from understanding import generate_summary, extract_chapters, extract_key_takeaways
from learning import generate_quiz, explain_like_five, extract_vocabulary
from repurposing import to_blog_post, to_tweet_thread, to_linkedin_post, to_slide_deck, to_instagram_caption
from analysis import sentiment_analysis, emotion_detection, comments_analysis
from engagement import generate_qa_questions

def extract_video_id(url_or_id: str) -> str:
    # Accepts full URL or just video ID
    match = re.search(r"(?:v=|youtu.be/)([\w-]{11})", url_or_id)
    if match:
        return match.group(1)
    if len(url_or_id) == 11:
        return url_or_id
    raise ValueError("Could not extract video ID from input.")
FEATURES = {
    'summary': generate_summary,
    'chapters': extract_chapters,
    'key_takeaways': extract_key_takeaways,
    'quiz': generate_quiz,
    'explain_like_five': explain_like_five,
    'vocabulary': extract_vocabulary,
    'blog_post': to_blog_post,
    'tweet_thread': to_tweet_thread,
    'linkedin_post': to_linkedin_post,
    'slide_deck': to_slide_deck,
    'instagram_caption': to_instagram_caption,
    'sentiment_analysis': sentiment_analysis,
    'emotion_detection': emotion_detection,
    'comments_analysis': comments_analysis,
    'qa_questions': generate_qa_questions,
}

def main():
    parser = argparse.ArgumentParser(description="YouTube Transcript Feature CLI")
    parser.add_argument("video", help="YouTube video URL or ID")
    parser.add_argument("--feature", required=True, choices=FEATURES.keys(), help="Feature to run")
    parser.add_argument("--lang", nargs="*", default=["en"], help="Preferred transcript language(s)")
    args = parser.parse_args()

    try:
        video_id = extract_video_id(args.video)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=args.lang)
        result = FEATURES[args.feature](transcript)
        print(f"\nResult for {args.feature} on video {video_id}:\n")
        if isinstance(result, list):
            for item in result:
                print(item)
        else:
            print(result)
    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("No transcript found for this video in the requested language(s). Try another language or video.")
    except VideoUnavailable:
        print("Video unavailable.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 