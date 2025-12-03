# fraud_signal_decoder

A tiny Flask API that returns a mock transaction as JSON and demonstrates how simple risk logic can be layered on top of raw data. It doubles as a hands-on practice project for JSON handling, HTTP APIs, Postman usage, and lightweight automated testing.

## Setup

1. **(Optional but recommended) create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\\Scripts\\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Flask app

Start the server on http://localhost:5000:
```bash
python app.py
```
You should see Flask start in debug mode. The available endpoints are:
- `GET /transaction`
- `GET /transaction_with_risk`

## Postman collection

A ready-to-import Postman collection is included at `Fraud_Signal_Decoder.postman_collection.json`.
1. Open Postman, click **Import**, and choose the file.
2. Send the `GET /transaction` and `GET /transaction_with_risk` requests against `http://localhost:5000`.
3. The `GET /transaction_with_risk` request includes a test script that asserts `computedRiskLevel` is valid and logs the value to the Postman console.

## Tests

Run the automated risk-logic checks with pytest:
```bash
python -m pytest
```

## How the risk logic works

The `compute_risk` helper in `risk.py` inspects two signals: `emailAgeDays` and `ipTrustScore`.
- If the email is younger than 10 days **and** the IP trust score is below 50 → **high** risk.
- Else if either the email is younger than 10 days **or** the IP trust score is below 60 → **medium** risk.
- Otherwise → **low** risk.

This mirrors the sort of heuristic scoring often used in real fraud teams, where multiple weak signals combine to raise concern even if each on its own is only moderately risky.

## Using this project in conversation

This project shows you can:
- Design and build a small Flask API that returns structured JSON.
- Express and explain control flow that maps signals to a clear risk label.
- Validate API behavior with Postman collections and scripts.
- Add quick automated tests to document and protect core business logic.
