import os
import requests

user = os.environ["PJN_USER"]
password = os.environ["PJN_PASSWORD"]

s = requests.Session()

r = s.get(
    "https://sso.pjn.gov.ar/auth/realms/pjn/protocol/openid-connect/auth?client_id=pjn-portal",
    allow_redirects=True,
    timeout=30
)

print("STATUS:", r.status_code)
print("URL:", r.url)
print("LOGIN PAGE FOUND:", "username" in r.text.lower())
print("PASSWORD FIELD FOUND:", "password" in r.text.lower())
