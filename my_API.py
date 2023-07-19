from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint.

    Returns:
        dict: A dictionary containing the status message.
    """
    return {
        "message": "API is online!",
        "function": "Calculator"
    }

# Request body model
class Resp(BaseModel):
    """
    Request body model for the calculator endpoint.
    """
    value1: int
    value2: int
    operation: str

# Calculator endpoint
@app.post("/calculator")
async def calculator(resp: Resp):
    """
    Calculator endpoint.
    Performs arithmetic calculations based on the provided operation and values.

    Args:
        resp (Resp): Request body containing value1, value2, and operation.

    Returns:
        dict: A dictionary containing the result of the calculation.
            If an error occurs, an error message is returned instead.
    """
    # Extract values from the request body
    value1 = resp.value1
    value2 = resp.value2
    operation = resp.operation

    result = None
    if operation == "+":
        # Addition operation
        result = str(value1 + value2)
    elif operation == "-":
        # Subtraction operation
        result = str(value1 - value2)
    elif operation == "/":
        if value2 != 0:
            # Division operation
            result = str(value1 / value2)
        else:
            # Error: Division by zero
            return {"Error": "Division by zero cannot be done, please try again with a non-zero number!"}
    elif operation == "*":
        # Multiplication operation
        result = str(value1 * value2)
    else:
        # Error: Invalid operation
        return {"Error": "Operation not recognized. Please try again!"}

    # Return the result
    return {"Result": result}

