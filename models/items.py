from pydantic import BaseModel,Field
from typing import Optional

# class item(BaseModel):
#     name: str = Field(...,min_length= 3 , max_digits= 100)
#     age: int = Field(...,ge= 1)
#     Description: Optional[str] = Field(default="Nayal IS AWESOME" , min_length=10 , max_digits= 1000)    
#     price: float = Field(...,ge= 3.0)
#     tags: list[str] = Field(default=[])
class item(BaseModel):
    name: Optional[str] = Field(default="Nayal",min_length=1)
    age : int = Field(...,gt= 0)
    Description: str = Field(...,min_length=2 , max_length=100)
    price : float = Field(default=0)
    tags : Optional[list[str]]=  Field(default_factory=list)
    