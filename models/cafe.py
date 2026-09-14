from decimal import Decimal
from faulthandler import is_enabled

from pydantic import BaseModel, Field


class Cafe(BaseModel):
    id:int 
    name:str
    description:str
    price:Decimal = Field(max_digits=10, decimal_places=2) 
    is_enabled: bool = True
    
    