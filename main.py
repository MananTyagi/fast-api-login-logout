from fastapi import FastAPI,  Depends , Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager 
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.templating import Jinja2Templates
from sys import path
from starlette import status

app = FastAPI()

SECRET = "secret-key"

templates = Jinja2Templates(directory="templates")

manager = LoginManager(SECRET, "/auth/login", use_cookie=True)
manager.cookie_name = "some-name"

DB = {"username": {"password": "1234567"}}  # unhashed


@manager.user_loader
def load_user(username: str):
   user = DB.get(username)
   return user


@app.post("/auth/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
   username = data.username
   password = data.password
   user = load_user(username)
   if not user:
       raise InvalidCredentialsException
   elif password != user['password']:
       raise InvalidCredentialsException
   access_token = manager.create_access_token(
       data={"sub": username}
   )
   resp = RedirectResponse(url="/private", status_code=status.HTTP_302_FOUND)
   manager.set_cookie(resp, access_token)
   return resp


@app.get("/private")
def getPrivateendpoint(_=Depends(manager)):
   return "You are an authentciated user"




@ app.get("/auth/login", response_class=HTMLResponse)
def login(request: Request):
   context = {'request': request, }
   return templates.TemplateResponse("login.html.j2", context)

@app.get('/logout', response_class=HTMLResponse)
def protected_route(request: Request, user=Depends(manager)):
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    manager.set_cookie(response, "")
    
    return  response