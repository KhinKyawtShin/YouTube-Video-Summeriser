from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    query = parse_qs(urlparse(url).query)
    return query["v"][0]

video_url = input("Enter YouTube video URL: ")
video_id = extract_video_id(video_url)

transcript = YouTubeTranscriptApi.get_transcript(video_id)
text = " ".join([line["text"] for line in transcript])
print(text)
