import requests

url = input('please enter url link:')
response = requests.get(url)
print(response.status_code)
print(response.text)
try:
    raw_socket_response = requests.get(url, stream=True)
except requests.exceptions.RequestException as error:
    print("An error occured: ", error)
else:
    print(raw_socket_response.raw)
    print(raw_socket_response.raw.read(15))
