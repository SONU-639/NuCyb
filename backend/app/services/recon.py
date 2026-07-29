import dns.resolver


def dns_lookup(domain):
    result = {}

    try:
        answers = dns.resolver.resolve(domain, "A")

        result["ip"] = []

        for answer in answers:
            result["ip"].append(str(answer))

    except Exception:
        result["ip"] = "Not found"

    return result