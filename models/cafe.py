from decimal import Decimal
from sqlmodel import Field, SQLModel
# from pydantic import BaseModel, Field

# La documentación oficial de SQLModel recomienda estructurar tu archivo models/cafe.py dividiendo el modelo en tres partes utilizando la herencia de la siguiente manera:

# 1. MODELO BASE: Campos comunes que comparte todo el mundo
class CafeBase(SQLModel):
    name: str
    description: str
    price: Decimal = Field(..., max_digits=10, decimal_places=2, ge=0)
    available: bool = True

# 2. MODELO DE ENTRADA (Para el POST): No tiene ID porque aún no se genera
class CafeCreate(CafeBase):
    pass  # Hereda todo lo de CafeBase tal cual

# 3. MODELO DE TABLA (Base de Datos): Tiene el ID y controla la persistencia
class Cafe(CafeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


















""" class Cafe(BaseModel):
    id:int 
    name:str
    description:str
    price:Decimal = Field(max_digits=10, decimal_places=2) 
    is_enabled: bool = True
     """
    
    
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