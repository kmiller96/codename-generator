from typing import Annotated

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=".")


def _render_html_template(request: Request):
    """Renders the HTML template with optional status and message."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/")
async def index(request: Request):
    """Returns the HTML file."""
    return _render_html_template(request=request)


@app.post("/")
async def process_submission(input_text: Annotated[str, Form()], request: Request):
    """Handles form submission."""
    return _render_html_template(request=request)
