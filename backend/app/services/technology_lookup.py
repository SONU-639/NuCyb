import requests


def technology_information(domain):
    try:
        response = requests.get(
            f"https://{domain}",
            timeout=10,
            headers={
                "User-Agent": "NuCyb Scanner/1.0"
            }
        )

        headers = response.headers

        server = headers.get("Server", "Unknown")
        powered_by = headers.get("X-Powered-By", "Unknown")

        cdn = "Unknown"

        if "cloudflare" in server.lower():
            cdn = "Cloudflare"

        elif "gws" in server.lower():
            cdn = "Google"

        elif "akamai" in server.lower():
            cdn = "Akamai"

        return {
            "server": server,
            "powered_by": powered_by,
            "cdn": cdn
        }

    except Exception as e:
        return {
            "error": str(e)
        }