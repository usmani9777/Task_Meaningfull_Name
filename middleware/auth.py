from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class auth(BaseHTTPMiddleware):
    async def dispatch(self,request: Request , call_next):
        if request.url.path in ['/','/docs','/openapi.json']:
            response  = await call_next(request)
            return response    
        try:
            api_key = request.headers.get('X-API-KEY')
            if api_key != "NAYALISAWESOME":
                return JSONResponse(status_code=403 , content='ACCESS FORBIDIN')
            response  = await call_next(request)
            return response
        except: raise JSONResponse(status_code= 422 , content= 'Invalid Header doesnt consist API Key')