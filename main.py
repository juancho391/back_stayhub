from fastapi.middleware.cors import CORSMiddleware
from .db.postgresql.conexion import create_tables_and_db
from .api import register_routers
from fastapi import FastAPI 

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


register_routers(app=app)

@app.on_event("startup")
def on_startup():
    create_tables_and_db()
