"""Unit tests for the compute_risk helper."""
from risk import compute_risk


def test_high_risk_when_email_and_ip_are_low():
    transaction = {"emailAgeDays": 5, "ipTrustScore": 40}
    assert compute_risk(transaction) == "high"


def test_medium_risk_when_only_email_is_low():
    transaction = {"emailAgeDays": 5, "ipTrustScore": 70}
    assert compute_risk(transaction) == "medium"


def test_medium_risk_when_only_ip_is_low():
    transaction = {"emailAgeDays": 15, "ipTrustScore": 55}
    assert compute_risk(transaction) == "medium"


def test_low_risk_when_signals_are_strong():
    transaction = {"emailAgeDays": 30, "ipTrustScore": 80}
    assert compute_risk(transaction) == "low"
