import requests
import json

API_KEY = "d72597eea0ed245a73b9bea2a69f7bc0"
ENDPOINT = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/snapshot"

params = {
    "postalcode": "93611",
    "propertytype": "SFR"  # Single Family Residential
}

headers = {
    "accept": "application/json",
    "apikey": API_KEY
}

response = requests.get(ENDPOINT, params=params, headers=headers)

try:
    response.raise_for_status()
    data = response.json()
    print(json.dumps(data, indent=2))
except requests.HTTPError as e:
    print(f"HTTP error: {e}")
    print(response.text)

