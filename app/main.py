from app.api.v1.routes import players
from app.api.v1.routes import clubs
from app.database import Base, engine
from app.models import message
from app.models import user
from app.database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import contact
from app.api.v1.routes import auth
from app.api.v1.routes import admin

app = FastAPI(
    title="Ultimate Manager API",
    description="Backend system for Ultimate Manager Telegram Mini App",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://cyberdercy-portfolio.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clubs.router)
app.include_router(players.router)
app.include_router(contact.router)
app.include_router(auth.router)
app.include_router(admin.router)

@app.get("/")
def home():
    return {
        "game": "Ultimate Manager",
        "status": "Running",
        "message": "Welcome to the football management world"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/database-test")
def database_test():
    try:
        engine.connect()
        return {
            "database": "connected"
        }
    except Exception as e:
        return {
            "database": "failed",
            "error": str(e)
        }    
