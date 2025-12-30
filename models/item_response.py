from pydantic import BaseModel

class item_response(BaseModel):
    id : int 
    name: str
    age: int 
    Description: str        
    price: float
    tags: list[str]
   