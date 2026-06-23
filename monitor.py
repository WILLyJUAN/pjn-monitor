import requests

r = requests.get(
    "https://portalpjn.pjn.gov.ar/inicio",
    timeout=30
)

print("STATUS:", r.status_code)
print("URL:", r.url)
print("LENGTH:", len(r.text))
