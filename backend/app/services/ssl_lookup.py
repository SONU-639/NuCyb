import socket
import ssl
from datetime import datetime


def ssl_information(domain):
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:
                cert = secure_sock.getpeercert()

        issuer = dict(x[0] for x in cert["issuer"])
        subject = dict(x[0] for x in cert["subject"])

        valid_from = datetime.strptime(
            cert["notBefore"], "%b %d %H:%M:%S %Y %Z"
        )

        valid_until = datetime.strptime(
            cert["notAfter"], "%b %d %H:%M:%S %Y %Z"
        )

        days_remaining = (valid_until - datetime.utcnow()).days

        return {
            "status": "Valid",
            "issuer": issuer.get("organizationName"),
            "common_name": subject.get("commonName"),
            "valid_from": str(valid_from),
            "valid_until": str(valid_until),
            "days_remaining": days_remaining,
        }

    except Exception as e:
        return {
            "status": "Invalid",
            "error": str(e)
        }