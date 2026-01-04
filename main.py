from fastapi import FastAPI
import uvicorn
from api.routes.user import router as user_route
from api.routes.items  import router as items_route
from api.routes.joke import router as joke_route
from middleware.auth import auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(auth)
# app.add_middleware(CORSMiddleware,allow_methods = ['*'],allow_origins = ["*"],allow_headers = ["*"],allow_credentials = True)
app.include_router(user_route)
app.include_router(items_route)
app.include_router(joke_route)
   
if __name__ == "__main__":
    uvicorn.run(app = 'main:app',host = '0.0.0.0' , port = 8000 , reload =True )