import requests

def fetch(base="USD", currencies="XAU"):
    url = "https://api.metalpriceapi.com/v1/latest"
    params = {
        "api_key": "bb27d86f6b0a23832f62c5ad3393c8aa",
        "base": base,
        "currencies": currencies,
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            return data  # Return the dictionary
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
# data = fetch(base="USD", currencies="XAU")
# print(data)
