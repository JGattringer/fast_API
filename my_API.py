from fastapi import FastAPI
from pydantic import BaseModel
from requests import post

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "API is online!",
        "function": "Calculator"
    }


class Resp(BaseModel):
    value1: int
    value2: int
    operation: str


@app.post("/calculator")
async def calculator(resp: Resp):
    value1 = resp.value1
    value2 = resp.value2
    operation = resp.operation

    result = None
    if operation == "+":
        result = str(value1 + value2)
    elif operation == "-":
        result = str(value1 - value2)
    elif operation == "/":
        if value2 != 0:
            result = str(value1 / value2)
        else:
            return {"Error": "Division by zero cannot be done, please try again with a non-zero number!"}
    elif operation == "*":
        result = str(value1 * value2)
    else:
        return {"Error": "Operation not recognized. Please try again!"}

    return {"Result": result}


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


