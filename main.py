import requests
import os
from datetime import datetime

# These are the original variables that have become Env Vars
# NUTRITIONIX_APP_ID = "54d8780a"
# NUTRITIONIX_APP_KEY = "2f91880644d0a39f55594cc2595af99b"
# NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# SHEETY_POST_ENDPOINT = "https://api.sheety.co/789e9c01b29d4ce7279876f9f22b5a3e/myWorkouts/workouts"
# SHEETY_TOKEN = "YWxhbmxlZXc6QWNlZzIzMTI="

NUTRITIONIX_APP_ID = os.environ.get("APP_ID")
NUTRITIONIX_APP_KEY = os.environ.get("APP_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POST_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

parameters = {
    "query": input("Tell me which exercises you did: "),
}


response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=parameters)
response.raise_for_status()
json_data = response.json()
# print(json_data)

data = {
    "workout":{
        "date": datetime.today().strftime("%d/%m/%Y"),
        "time": datetime.today().strftime("%X"),
        "exercise": json_data["exercises"][0]["user_input"].title(),
        "duration": json_data["exercises"][0]["duration_min"],
        "calories": json_data["exercises"][0]["nf_calories"]
    }
}
# print(data)

sheety_header = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}

response = requests.post(url=SHEETY_POST_ENDPOINT, json=data, headers=sheety_header)
response.raise_for_status()
print(response.text)