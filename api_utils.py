import requests

def get_current_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("ip", "Unknown IP")
    except Exception as e:
        return f"Error: {str(e)}"

def get_random_joke():
    try:
        url = "https://v2.jokeapi.dev/joke/Any"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if data["type"] == "single":
            return data["joke"]
        else:
            return f"{data['setup']}\n{data['delivery']}"
    except Exception as e:
        return f"Error fetching joke: {str(e)}"


