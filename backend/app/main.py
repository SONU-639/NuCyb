from fastapi import FastAPI
from app.services.recon import dns_lookup
from app.services.ip_lookup import ip_information
from app.services.whois_lookup import whois_information
from app.services.ssl_lookup import ssl_information
from app.services.header_lookup import security_headers
from app.services.risk_engine import calculate_risk
from app.services.technology_lookup import technology_information
app = FastAPI(
    title="NuCyb",
    description="Cyber Intelligence Platform built with FastAPI",
    version="1.0.0",
    contact={
        "name": "Sonu P Koshy",
        "url": "https://github.com/SONU-639/NuCyb"
    },
    license_info={
        "name": "MIT License"
    }
)

@app.get("/")
def home():
    return {
        "project": "NuCyb",
        "status": "online",
        "message": "Cyber Intelligence Platform running"
    }
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "NuCyb Backend"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }
@app.get("/recon/{domain}")
def recon(domain: str):

    dns_data = dns_lookup(domain)

    ip = dns_data["ip"][0]

    report = {
        "domain": domain,
        "dns": dns_data,
        "ip_information": ip_information(ip),
        "whois_information": whois_information(domain),
        "ssl_information": ssl_information(domain),
        "security_headers": security_headers(domain),
        "technology_information": technology_information(domain)
    }

    report["risk_assessment"] = calculate_risk(report)

    return report

  

    