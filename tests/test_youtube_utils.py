import pytest
import sys
sys.path.append("../utils")
from utils.youtube_utils import get_video_id
def test_get_video_id():
    assert get_video_id("https://www.youtube.com/watch?v=abcd1234") =="abcd1234"
    assert get_video_id("https://youtu.be/abcd1234") == "abcd1234"
    assert get_video_id("https://www.invalid.com") is None
