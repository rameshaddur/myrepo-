from youtube_transcript_api import YouTubeTranscriptApi
video_id='2P30W3TN4nI'

#video_id='aTxf5WPdwLA'
transcript = YouTubeTranscriptApi.get_transcript(video_id)

print(transcript)