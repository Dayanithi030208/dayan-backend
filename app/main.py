from fastapi import FastAPI
from app.routers import auth, activity, dashboard
from app.database import Base, engine
from app.models.activity_model import Activity
from app.database import Base, engine
from app.models import user, activity_model, mood
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DAYAN Backend",
    description="AI Powered Focus & Emotional Intelligence Engine",
    version="1.0.0"
)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "DAYAN API is running 🚀"}

# Register Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(activity.router, prefix="/api/activity", tags=["Activity"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
