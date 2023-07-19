import pytest
from fastapi.testclient import TestClient
from my_API import app

client = TestClient(app)


@pytest.mark.parametrize("value1, value2, operation, expected_result", [
    (10, 5, "+", "15"),  # Addition operation test case
    (10, 5, "-", "5"),   # Subtraction operation test case
    (10, 5, "*", "50"),  # Multiplication operation test case
    (10, 5, "/", "2"),   # Division operation test case
    (10, 0, "/", None) # Division by zero test case
])
def test_calculator(value1, value2, operation, expected_result):
    """
    Test case for the calculator endpoint.
    """
    response = client.post(
        "/calculator",
        json={"value1": value1, "value2": value2, "operation": operation}
    )
    assert response.status_code == 200
    result = response.json().get("Result")
    if expected_result is None:
        assert result is None  # Check if the result is None
    else:
        expected_result = int(expected_result)
        assert round(float(result)) == expected_result

def test_invalid_operation():
    """
    Test case for an invalid operation.
    """
    response = client.post(
        "/calculator",
        json={"value1": 10, "value2": 5, "operation": "%"}
    )
    assert response.status_code == 200
    error_message = response.json().get("Error")
    assert error_message == "Operation not recognized. Please try again!"


def test_division_by_zero():
    """
    Test case for division by zero.
    """
    response = client.post(
        "/calculator",
        json={"value1": 10, "value2": 0, "operation": "/"}
    )
    assert response.status_code == 200
    error_message = response.json().get("Error")
    assert error_message == "Division by zero cannot be done, please try again with a non-zero number!"

    response = client.post(
        "/calculator",
        json={"value1": 10, "value2": 0, "operation": "/"}
    )
    assert response.status_code == 200
    result = response.json().get("Result")
    if result is not None:
        result = round(result)  # Apply rounding to the result if it's not None
    assert result is None  # Use the 'is' operator to compare with None






if __name__ == "__main__":
    pytest.main()
