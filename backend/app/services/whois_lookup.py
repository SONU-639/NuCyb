import whois
from datetime import datetime


def format_date(date_value):
    if isinstance(date_value, list):
        date_value = date_value[0]

    if isinstance(date_value, datetime):
        return date_value.strftime("%Y-%m-%d")

    return None


def whois_information(domain):
    try:
        data = whois.whois(domain)

        return {
            "registrar": data.registrar,
            "creation_date": format_date(data.creation_date),
            "expiration_date": format_date(data.expiration_date),
            "country": data.country
        }

    except Exception as e:
        return {
            "error": str(e)
        }