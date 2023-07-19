# API Project README

This is a simple API project that provides a calculator functionality. The API is built using the FastAPI framework and utilizes the Pydantic library for request body validation.

## Prerequisites

Before running the API, make sure you have the following dependencies installed:

- Python 3.7+
- FastAPI
- Pydantic
- Requests
- Pytest

## Installation

1. Clone the repository:

```bash
git clone <(https://github.com/JGattringer/fast_API.git)>

2. Install the required dependencies using pip:

pip install fastapi pydantic requests pytest

# Usage

## Running the API
To run the API, execute the following command:

uvicorn my_API:app --reload

The API will be accessible at http://localhost:8000.

# Root Endpoint

. GET /: Returns the status message of the API.

Example response:

{
  "message": "API is online!",
  "function": "Calculator"
}

## Calculator Endpoint

. POST /calculator: Performs arithmetic calculations based on the provided operation and values.

##Request body model:

class Resp(BaseModel):
    value1: int
    value2: int
    operation: str
Supported operations: +, -, *, /

Example request:

{
  "value1": 10,
  "value2": 5,
  "operation": "+"
}
Example response:

{
  "Result": "15"
}
If an error occurs, an error message is returned instead.

# Testing

This project includes a set of test cases to ensure the correctness of the calculator endpoint. The tests are implemented using the Pytest framework and the FastAPI test client.

## To run the tests, execute the following command:

pytest

## The tests cover the following scenarios:

. Addition operation test case
. Subtraction operation test case
. Multiplication operation test case
. Division operation test case
. Division by zero test case
. Invalid operation test case
The test results will be displayed in the console.

## Additional Notes

Make sure the API is running before executing the test cases.
The API logs will be displayed in the console while the API is running.
Feel free to explore and enhance this simple API project according to your requirements.

