"""
Response Post

This module demonstrates sending a POST request to the calculator endpoint of the API
and handling the response.
It uses the requests library to make the HTTP request.
"""

from requests import post

# Send a POST request to the calculator endpoint with a timeout of 5 seconds
response = post("http://localhost:8000/calculator", json={"value1": 23, "value2": 0, "operation": "/"}, timeout=5)

if response.status_code == 200:
    # If the request is successful (status code 200)
    result = response.json()
    if result is not None:
        # If the result is not None, print it
        print(f"Result: {result}")
    else:
        # If the result is None, print an error message
        print("Operation not recognized, please try again!")
else:
    # If there is an error processing the request, print the error details
    print(f"Error processing the request. Status code: {response.status_code}")
    print("Error Response:", response.text)
