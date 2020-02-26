from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from pydantic import BaseModel
from pythonrobofriends.robots import robots

templates = Jinja2Templates(directory="pythonrobofriends/templates")


class RobotsList(BaseModel):
    id: int
    name: str
    username: str
    email: str


app = FastAPI()

app.mount("/static", StaticFiles(directory="pythonrobofriends/static"), name="static")


@app.get("/")
async def get_robots(request: Request):
    item_list = []

    for robot in robots:
        item = RobotsList(
            id=robot['id'],
            name=robot['name'],
            username=robot['username'],
            email=robot['email']
        )
        item_list.append(item)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "robots": item_list}
    )
