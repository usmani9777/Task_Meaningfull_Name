from fastapi import APIRouter,HTTPException,Query
from services.Joke_function import Joke

router = APIRouter(prefix= '/Joke',tags=['Joke'])

 

@router.get("/")
async def get_joke():
    try:
        result = await Joke()
        if result['status'] == 'error':
            raise HTTPException(status_code=503, detail='API Failed to Respond')
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
