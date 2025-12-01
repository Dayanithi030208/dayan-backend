from fastapi import FastAPI
from app.routers import auth, activity, dashboard
from app.database import Base, engine
from app.models.activity_model import Activity

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DAYAN Backend",
    description="AI Powered Focus & Emotional Intelligence Engine",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "DAYAN API is running 🚀"}

# Register Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(activity.router, prefix="/api/activity", tags=["Activity"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
