from hashlib import sha256
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR))

################
## Load Words ##
################


def _load_words(filename: str) -> list[str]:
    with (BASE_DIR / filename).open() as word_file:
        return [line.strip() for line in word_file if line.strip()]


ADJECTIVES = _load_words("adjectives.txt")
NOUNS = _load_words("nouns.txt")

#############
## Helpers ##
#############


def _generate_codename(input_text: str) -> str:
    normalized_text = input_text.strip().lower()
    digest = sha256(normalized_text.encode("utf-8")).digest()
    adjective_index = int.from_bytes(digest[:8], "big") % len(ADJECTIVES)
    noun_index = int.from_bytes(digest[8:16], "big") % len(NOUNS)

    adjective = ADJECTIVES[adjective_index].title()
    noun = NOUNS[noun_index].title()
    return f"{adjective} {noun}"


def _render_html_template(
    request: Request,
    input_text: str = "",
    codename: str | None = None,
):
    """Renders the HTML template with the current form state."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "input_text": input_text,
            "codename": codename,
        },
    )


##############
## Handlers ##
##############


@app.get("/")
async def index(request: Request):
    """Returns the HTML file."""
    return _render_html_template(request=request)


@app.post("/")
async def process_submission(input_text: Annotated[str, Form()], request: Request):
    """Handles form submission and returns a deterministic codename."""
    normalized_input = input_text.strip().lower()

    return _render_html_template(
        request=request,
        input_text=normalized_input,
        codename=_generate_codename(normalized_input),
    )
