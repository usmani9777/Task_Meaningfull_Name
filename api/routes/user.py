from fastapi import APIRouter,HTTPException,Query

router = APIRouter(prefix= '/User',tags=['User'])



@router.get('/GetByID',status_code=201)
async def get(Name:str , ID:int =Query(...,gt=0) ):
    try:
        if len(Name) < 2:
            raise HTTPException(status_code= 404 , detail= 'Nayal Is Awesome')
        return {'Name':Name , 'ID':ID}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code= 500 , detail=str(e))
@router.get('/')
async def get():
    return {'Message':'Hello World'}

     