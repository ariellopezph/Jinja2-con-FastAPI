# import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def post_form(request: Request, username: str = Form(...), password: str = Form(...)):
    print(f'username: {username}')
    print(f'password: {password}')
    if username == 'aaa' and password == 'aaa':
        return templates.TemplateResponse("user.html", {"request": request})
    else:
        return "Verifique el usuario y contrasena"



# if __name__ == '__main__':
#     uvicorn.run(app)