import requests

r = requests.get(
    "https://portalpjn.pjn.gov.ar",
    allow_redirects=True,
    timeout=30
)

print("FINAL URL:", r.url)
print(r.text[:2000])
