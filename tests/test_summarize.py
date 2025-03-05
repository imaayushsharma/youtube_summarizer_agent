import pytest
import sys
sys.path.append("../utils")
from utils.summarize import summarize_text
def test_summarize_text():
    text = "There is possibilty of existence of multiverse in this universe."
    summary = summarize_text(text)
    assert isinstance(summary, str)
    assert len(summary) > 0    
    
    