import requests
response=requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
latitude=data["iss_position"]["latitude"]
longitude=data["iss_position"]["longitude"]
iss_location = (longitude,latitude)
print(iss_location)