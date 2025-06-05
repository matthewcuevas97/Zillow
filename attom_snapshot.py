import http.client
import json
import urllib.parse

# Replace with your Attom API key
API_KEY = "d72597eea0ed245a73b9bea2a69f7bc0"

HOST = "api.gateway.attomdata.com"
PATH = "/propertyapi/v1.0.0/property/snapshot"

params = {
    "postalcode": "93611",
    "propertytype": "SFR",  # Single Family Residential
}

query = urllib.parse.urlencode(params)
conn = http.client.HTTPSConnection(HOST)
headers = {
    "accept": "application/json",
    "apikey": API_KEY,
}

conn.request("GET", f"{PATH}?{query}", headers=headers)
res = conn.getresponse()
raw_data = res.read().decode("utf-8")

try:
    data = json.loads(raw_data)
    print(json.dumps(data, indent=2))
except json.JSONDecodeError:
    print(raw_data)
