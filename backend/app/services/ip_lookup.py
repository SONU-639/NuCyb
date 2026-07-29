from ipwhois import IPWhois


def ip_information(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap()

        return {
            "country": result.get("asn_country_code"),
            "organization": result.get("asn_description"),
            "asn": result.get("asn")
        }

    except Exception as e:
        return {
            "error": str(e)
        }