from decimal import Decimal
from sqlmodel import Field, SQLModel
# from pydantic import BaseModel, Field


""" class Cafe(BaseModel):
    id:int 
    name:str
    description:str
    price:Decimal = Field(max_digits=10, decimal_places=2) 
    is_enabled: bool = True
     """
    
class Cafe(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key = True)
    name:  str 
    description:str 
    price: Decimal = Field(..., max_digits=10, decimal_places=2, ge=0)
    available: bool= True
    
""" Tutorial
REcurso
https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#primary-key-id



class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

Veamos ahora con más detalle 
estas declaraciones de campos/columnas.

NoneCampos, columnas que admiten valores nulos¶
Comencemos con age, observe que tiene un tipo de int | None.

Esa es la forma estándar de declarar que algo "podría ser un into un None" en Python.

Y también establecimos el valor predeterminado agede None 


"""