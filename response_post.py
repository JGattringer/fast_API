from requests import post

response = post("http://localhost:8000/calculator", json={"value1": 23, "value2": 2, "operation": "+"})
if response.status_code == 200:
    result = response.json()
    if result is not None:
        print(f"Result: {result}")
    else:
       print("Operation not recognized, please try again!")
else:
    print(f"Error processing the request. Status code: {response.status_code}")
    print("Error Response:", response.text)


