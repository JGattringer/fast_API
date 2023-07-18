from fastapi import FastAPI
from pydantic import BaseModel


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




