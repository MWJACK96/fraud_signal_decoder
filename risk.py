"""Risk evaluation helpers for fraud_signal_decoder."""


def compute_risk(transaction: dict) -> str:
    """Compute a simple categorical risk level for the transaction.

    Control flow in plain language:
    1. Check the highest-risk condition first: if the email is brand new
       (under 10 days) *and* the IP address looks untrustworthy (score under 50),
       classify as "high" risk.
    2. Otherwise, check for medium risk: if either the email is brand new OR the
       IP trust score is under 60, label it "medium" risk.
    3. If neither of the above conditions is true, return "low" risk.
    """
    email_age = transaction.get("emailAgeDays", 0)
    ip_score = transaction.get("ipTrustScore", 0)

    if email_age < 10 and ip_score < 50:
        return "high"
    if email_age < 10 or ip_score < 60:
        return "medium"
    return "low"
