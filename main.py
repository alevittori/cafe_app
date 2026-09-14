
from decimal import Decimal

from fastapi import FastAPI, HTTPException, status

from models.cafe import Cafe

app=FastAPI()
# Lista con los 10 cafés para tu menú
menu_cafe = [
    Cafe(
        id=1, 
        name="Espresso", 
        description="Un shot de café concentrado, intenso y con una capa de crema perfecta.", 
        price=Decimal("1200.00")
    ),
    Cafe(
        id=2, 
        name="Americano", 
        description="Café espresso suavizado con agua caliente, ideal para un sabor prolongado.", 
        price=Decimal("1400.00")
    ),
    Cafe(
        id=3, 
        name="Cappuccino", 
        description="Espresso combinado con partes iguales de leche vaporizada y una densa espuma.", 
        price=Decimal("1800.00")
    ),
    Cafe(
        id=4, 
        name="Latte", 
        description="Una base de espresso con abundante leche vaporizada y una fina capa de espuma.", 
        price=Decimal("1700.00")
    ),
    Cafe(
        id=5, 
        name="Macchiato", 
        description="Espresso 'manchado' con una pequeña cucharada de espuma de leche caliente.", 
        price=Decimal("1350.00")
    ),
    Cafe(
        id=6, 
        name="Moka", 
        description="Deliciosa mezcla de espresso, leche vaporizada y jarabe de chocolate dulce.", 
        price=Decimal("2100.00")
    ),
    Cafe(
        id=7, 
        name="Flat White", 
        description="Doble shot de espresso corto combinado con leche vaporizada de textura muy fina.", 
        price=Decimal("1900.00")
    ),
    Cafe(
        id=8, 
        name="Cold Brew", 
        description="Café infusionado en agua fría durante 16 horas, resultando en un sabor suave y refrescante.", 
        price=Decimal("2000.00")
    ),
    Cafe(
        id=9, 
        name="Frappé de Caramelo", 
        description="Café licuado con hielo, leche y salsa de caramelo, cubierto con crema batida.", 
        price=Decimal("2400.00"),
        is_enabled=True
    ),
    Cafe(
        id=10, 
        name="Café Irlandés", 
        description="Café caliente combinado con un toque de whisky irlandés, azúcar y crema batida.", 
        price=Decimal("2800.00"),
        is_enabled=False  # Lo dejamos deshabilitado por si no hay stock o es para un horario especial
    )
]

@app.get("/")
def read_root(): 
    return {"message":"CafeApp funcionando desde FAstApi"}

@app.get("/menu_cafe")
def get_menu_cafe(): 
    try:
        
        return {"menu":menu_cafe}
    except Exception as e:  # noqa: BLE001
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocurrio un error al cargar servidor: {e!s}"
        )

@app.get("/menu_cafe/{id}")
def get_cafe(id:int): 
    
    for cafe in menu_cafe:
        if(cafe.id == id):
            return {"cafe":cafe}
    
   
    # 2. Si el bucle termina y no encontró nada, lanzamos el error de inmediato
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"El café con el ID {id} no fue encontrado en el menú."
    )
    
@app.post("/menu_cafe")
def create_cafe(cafe:Cafe):
    existe = any(c.id == cafe.id for c in menu_cafe)
    if existe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El café con el ID {cafe.id} ya existe en el menú."
        )
        
    menu_cafe.append(cafe)
    return {"message": f"Café '{cafe.name}' agregado con éxito."}

@app.delete("/menu_cafe/{id}", status_code=status.HTTP_200_OK)
def delete_cafe(id: int):
    
    cafe_encontrado = next((cafe for cafe in menu_cafe if cafe.id == id), None)
    
  
    if cafe_encontrado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se puede eliminar: El café con ID {id} no existe."
        )
    
   
    menu_cafe.remove(cafe_encontrado)
    return {"message": f"El café '{cafe_encontrado.name}' fue eliminado correctamente."}


@app.put("/menu_cafe/{id}", status_code=status.HTTP_200_OK)
def update_cafe(id: int, cafe_actualizado: Cafe):
    
    indice_encontrado = None
    for index, cafe in enumerate(menu_cafe):
        if cafe.id == id:
            indice_encontrado = index
            break
            
   
    if indice_encontrado is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se puede actualizar: El café con ID {id} no existe."
        )
        
   
    menu_cafe[indice_encontrado] = cafe_actualizado
    
    return {
        "message": f"Café con ID {id} actualizado con éxito.",
        "cafe": cafe_actualizado
    }
