# Initializing the Libraries 

import streamlit as st
from utils.youtube_utils import get_video_id, get_transcript
from utils.summarize import summarize_text
from config.openai_config import setup_openai

# Initialize OpenAI API
setup_openai()

# Streamlit Web App
html_temp="""

    <div style="background-color:#FF0000;padding:10xp">
    <h2 style="color:white;text-align:center;">🍁 YOUTUBE VIDEO SUMMARIZER 🍁</h2>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html=True)
st.write("\n\n")
st.write("**Enter YouTube URL to get summary of the video.**")

url = st.text_input("YouTube Video URL")

if st.button("Summarize",type="primary"):
    if not url:
        st.error("Please enter a valid Youtube URL.")
    else:
        st.info("Fetching transcript...")
        video_id = get_video_id(url)
        if video_id:
            transcript = get_transcript(video_id)
            if transcript:
                st.info("Generating summary...")
                summary = summarize_text(transcript)
                st.subheader("Summary")
                st.write(summary)
            else:
                st.error("Failed to fetch transcript.")
        else:
            st.error("Invalid Youtube URL.")