import requests
# enters the url
url = input('please enter url link:')
# use try except to go to error if the timeout reaches
try:
    # time out is used to indicate how long before time out
    response = requests.get(url, timeout=1)
    print(response.status_code)
    print(response.text)
except requests.exceptions.RequestException as e:
    # when the time out reaches it throws the error message
    print("the request has reached a timeout", e)
