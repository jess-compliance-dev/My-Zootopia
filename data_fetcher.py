import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """Fetches animal data from API for the given animal name"""
    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error occurred:", response.status_code, response.text)
        return []  # avoids TypeError