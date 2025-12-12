# tests/test_ethics.py
import pytest
from src.ethics_charters import SacredEthicsCharter
from src.alignment_mirrors import AlignmentMirror

def test_charter_prefix():
    charter = SacredEthicsCharter()
    prefix = charter.generate_prefix("Test context")
    assert "Sacred Charter:" in prefix
    assert "Response must align:" in prefix

def test_validate_output():
    charter = SacredEthicsCharter()
    valid, _ = charter.validate_output("Harmless response.")
    assert valid
    invalid, suggestions = charter.validate_output("This is harmful and deceptive.")
    assert not invalid
    assert len(suggestions) > 0

def test_mirror_extraction():
    mirror = AlignmentMirror()
    response = "AI Response: ...\nSelf-Mirror: This aligns."
    insights = mirror.extract_insights(response)
    assert insights["aligned"] is True
