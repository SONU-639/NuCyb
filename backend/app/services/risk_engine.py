def calculate_risk(report):
    score = 100

    positive = []
    warnings = []
    critical = []

    # SSL Check
    ssl_info = report.get("ssl_information", {})

    if ssl_info.get("status") == "Valid":
        positive.append("SSL certificate is valid")
    else:
        score -= 40
        critical.append("SSL certificate is invalid")

    # WHOIS Check
    whois = report.get("whois_information", {})

    if whois.get("registrar"):
        positive.append("WHOIS information available")
    else:
        score -= 20
        warnings.append("WHOIS information unavailable")

    # Security Headers Check
    headers = report.get("security_headers", {})

    important_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    for header in important_headers:
        if headers.get(header) == "Missing":
            score -= 5
            warnings.append(f"Missing {header}")

    # Keep score within range
    score = max(0, min(score, 100))

    if score >= 80:
        level = "Low"
    elif score >= 50:
        level = "Medium"
    else:
        level = "High"

    return {
        "score": score,
        "level": level,
        "positive": positive,
        "warnings": warnings,
        "critical": critical
    }