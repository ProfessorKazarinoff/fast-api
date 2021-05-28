# main.py

from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
async def index():
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<div>"
        "Try it <a href='/api/calculate?x=7&y=2'>/api/calculate?x=7&y=2</a>"
        "</div>"
        "</body>"
        "</html"
    )
    return fastapi.responses.HTMLResponse(content=body)


@api.get("/api/calculate")
async def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "Error: Z can not be zero"}, status_code=400
        )

    value = x + y
    if z is not None:
        value = value / z

    return {"x": x, "y": y, "z": z, "value": value}
