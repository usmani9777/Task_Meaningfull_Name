from pydantic import BaseModel,Field
from typing import Optional

# class item(BaseModel):
#     name: str = Field(...,min_length= 3 , max_digits= 100)
#     age: int = Field(...,ge= 1)
#     Description: Optional[str] = Field(default="Nayal IS AWESOME" , min_length=10 , max_digits= 1000)    
#     price: float = Field(...,ge= 3.0)
#     tags: list[str] = Field(default=[])
class user(BaseModel):
    prompt: str = Field(..., max_length=100000)