import requests

def get_current_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("ip", "Unknown IP")
    except Exception as e:
        return f"Error: {str(e)}"

