from fastapi import APIRouter,HTTPException,Query
from models.items import item as it
from models.item_response import item_response
from uuid import UUID
router = APIRouter(prefix= '/Items',tags=['Items'])

    
item_db = {
    1: {"id": 1, "name": "Gaming Laptop", "age": 1, "Description": "High-end laptop", "price": 1200.50, "tags": ["tech", "gaming"]},
    2: {"id": 2, "name": "Smartphone", "age": 2, "Description": "Latest model", "price": 800.00, "tags": ["mobile", "electronics"]}
}
async def getItem(ID):
        if ID in item_db.keys():
            return item_db[ID]
        return {}

async def GetItems(item_db) -> list:
    l = []
    for x in item_db.values():
        l.append(x)
    return l


ID = 3

@router.get('/GetItemByID',response_model=item_response,status_code=201)
async def get(ID:int =Query(...,gt=0) ):
    
    try:
        item = await getItem(ID)
        if item == {}:
            raise HTTPException(status_code= 404 , detail= 'Nayal Is Awesome')
        return item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code= 500 , detail=str(e))
    
@router.get('/GetItemByIDRoute/{ID}',response_model=item_response,status_code=201)
async def getbyID(ID:int):
    
    try:
        item = await getItem(ID)
        if item == {}:
            raise HTTPException(status_code= 404 , detail= 'Nayal Is Awesome')
        return item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code= 500 , detail=str(e))





@router.post("/addItem", response_model=item_response, status_code=201)
async def add_item(item: it):
    global ID
    try:
        item_id = ID
        ID += 1
        item_data = item.model_dump()
        item_data["id"] = item_id

        item_db[item_id] = item_data

        return item_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


  
@router.get('/',response_model= list[item_response])
async def get_items():
    try:
        result = await GetItems(item_db)
        if result == []:
            raise HTTPException(status_code=404,detail='No items Present')
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
     