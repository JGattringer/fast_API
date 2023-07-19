from my_api import app
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html



# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    """
    Root endpoint.

    Returns:
        HTMLResponse: The HTML content of the documentation page.
    """
    with open("static/index.html") as f:
        content = f.read()
    return HTMLResponse(content=content, status_code=200)


def custom_openapi():
    """
    Custom function to generate the OpenAPI schema.

    Returns:
        dict: The generated OpenAPI schema.
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your API Title",
        version="1.0.0",
        description="Your API description",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    """
    Endpoint to serve the Swagger UI HTML page.

    Returns:
        HTMLResponse: The Swagger UI HTML page.
    """
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Documentation")


@app.get("/openapi.json", include_in_schema=False)
async def openapi_endpoint():
    """
    Endpoint to return the OpenAPI schema.

    Returns:
        dict: The OpenAPI schema.
    """
    return custom_openapi()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
