import requests
import json
# save the request from the url
response = requests.get('https://randomuser.me/api/')
# from importing json can use .json() to convert response to json
print(response.json())
# this also converts the response into json
data = json.loads(response.text)
print(data)
# Print the type of data variable
print("Type:", type(data))

