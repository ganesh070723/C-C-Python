import requests
name = "Ganesh"

response = requests.get(f"https://api.agify.io?name={name}")
text=response.json()
print(text["name"])
