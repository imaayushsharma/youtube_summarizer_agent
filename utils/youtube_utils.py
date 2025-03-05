#Initialize Library

from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extracting video ID from Yt URL

    Args:
        url ( str ): contains video url string 
    """
    
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    return None

def get_transcript(video_id):
    """ Fetch the transcript of YouTube video.

    Args:
        video_id ( str ): contains url video id
    """
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])
        return text
    except Exception as e:
        return str(e)