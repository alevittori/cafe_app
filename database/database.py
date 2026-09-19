# ¿Qué responsabilidad tendría database.py?

# Todo lo relacionado con la configuración de SQLite y el engine (motor).

from sqlalchemy import create_engine
from sqlmodel import SQLModel
from models.cafe import Cafe

sqlite_file_name="database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# motor
engine = create_engine(sqlite_url)

# SQLModel.metadata.create_all(engine)