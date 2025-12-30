from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

class auth(BaseHTTPMiddleware):
    async def dispatch(self,request: Request , call_next):
        if request.url.path in ['/','/docs','/openapi.json']:
            response  = await call_next(request)
            return response
        api_key = request.headers.get('X-API-KEY')
        if api_key != "NAYALISAWESOME":
            return JSONResponse(status_code=404 , content='ACCESS FORBIDIN')
        response  = await call_next(request)
        return response