import requests

parameters = {
    "amount": 20,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
quiz_data = response.json()
question_data = quiz_data["results"]

