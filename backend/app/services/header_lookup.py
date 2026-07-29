import requests


def security_headers(domain):
    try:
        response = requests.get(
            f"https://{domain}",
            timeout=10,
            allow_redirects=True,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/140.0.0.0 Safari/537.36"
                )
            }
        )

        print("========== RESPONSE HEADERS ==========")
        print(response.headers)
        print("======================================")

        headers = response.headers

        security = {
            "Strict-Transport-Security": headers.get(
                "Strict-Transport-Security",
                "Missing"
            ),
            "Content-Security-Policy": headers.get(
                "Content-Security-Policy",
                "Missing"
            ),
            "X-Frame-Options": headers.get(
                "X-Frame-Options",
                "Missing"
            ),
            "X-Content-Type-Options": headers.get(
                "X-Content-Type-Options",
                "Missing"
            ),
            "Referrer-Policy": headers.get(
                "Referrer-Policy",
                "Missing"
            ),
            "Permissions-Policy": headers.get(
                "Permissions-Policy",
                "Missing"
            )
        }

        return security

    except Exception as e:
        return {
            "error": str(e)
        }