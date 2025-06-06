from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound
from urllib.parse import urlparse, parse_qs
import google.generativeai as genai
import os

def extract_video_id(url):
    query = parse_qs(urlparse(url).query)
    return query["v"][0]

video_url = input("Enter YouTube video URL: ")
video_id = extract_video_id(video_url)

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([line["text"] for line in transcript])
    print(text)
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model=genai.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content(
        "Summarize the following YouTube video transcript: " + text,
        generation_config=genai.types.GenerationConfig(max_output_tokens=200)
    )
    print("Summary of the video:" + response.text)
except NoTranscriptFound:
    print("No transcript found for this video. It may not have subtitles or is unavailable.")
except Exception as e:
    print(f"An error occurred: {e}")