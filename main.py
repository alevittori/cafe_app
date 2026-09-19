

from fastapi import Depends, FastAPI, HTTPException, status
from httpx import get
from sqlmodel import SQLModel, Session,select
from database.database import engine
from models.cafe import Cafe, CafeCreate


app = FastAPI()

# Crear las tablas al iniciar la aplicacion si no existe
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    
# Dependencias para obtener la sesion de la base de datos
def get_session():
    with Session(engine) as session:
        yield session
        
# Obtener la lista completa de cafe, haicendo una consulta SELEC
@app.get("/menu_cafe")
def get_menu_cafe(session: Session = Depends(get_session)):
    try:
        # Buscamos todos los registros de la talblaCafe
        cafes = session.exec(select(Cafe)).all()
        return cafes
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocurrio un error al cargar el servidor:{e!s}",
        )
        
# Obtener un cafe especifico
# Usamos session.get(Cafe,id) que  busca directamente por llave primaria
@app.get("/menu_cafe/{id}")
def get_cafe(id:int , session: Session= Depends(get_session)): 
    cafe = session.get(Cafe,id)
    
    if not cafe:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"Cafe con id {id} no fue encontrado en el menu"
        )
        
    return {"cafe": cafe}

# POST para agregar un cafe
#  Agregamos el objeto a la sesion, hacemos commit para guardar en la base de datos y refresh para actualiar el objeto con los datos dinales de la BD, como el id
@app.post("/menu_cafe")
def create_cafe(cafe_in: CafeCreate, session: Session = Depends(get_session)): 
    # Convertimos los datos limpios de entrada en un modelo de base de datos real
    db_cafe = Cafe.model_validate(cafe_in)
    
    session.add(db_cafe) 
    session.commit() 
    session.refresh(db_cafe) 
    
    return {"message": f"Cafe '{db_cafe.name}' agregado con éxito con el ID {db_cafe.id}"}

