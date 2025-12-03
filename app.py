"""Simple Flask API for mock fraud signal decoding.

This module provides two endpoints:
- `/transaction` returns a mock transaction payload.
- `/transaction_with_risk` returns the same payload with a computed risk level.

Run with `python app.py` after installing dependencies.
"""
from flask import Flask, jsonify

from risk import compute_risk

app = Flask(__name__)


def get_mock_transaction() -> dict:
    """Return a static mock transaction payload.

    The fields are deliberately simplified to practice working with JSON
    and HTTP responses.
    """
    return {
        "transactionId": "txn_123456",
        "amount": 125.50,
        "currency": "USD",
        "deviceType": "mobile",
        "country": "US",
        "emailAgeDays": 7,
        "ipTrustScore": 45,
        "accountAgeDays": 120,
        "channel": "web",
    }


@app.get("/transaction")
def transaction() -> tuple:
    """Return the mock transaction as a JSON response."""
    return jsonify(get_mock_transaction()), 200


@app.get("/transaction_with_risk")
def transaction_with_risk() -> tuple:
    """Return the mock transaction plus a computed risk level."""
    payload = get_mock_transaction()
    payload["computedRiskLevel"] = compute_risk(payload)
    return jsonify(payload), 200


if __name__ == "__main__":
    # Running in development mode with debug enabled for faster iteration.
    app.run(host="0.0.0.0", port=5000, debug=True)
