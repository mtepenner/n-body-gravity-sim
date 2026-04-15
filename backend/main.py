from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes import router as simulation_router

app = FastAPI(
    title="N-Body Gravity Simulator API",
    description="Physics backend for simulating n-body gravitational systems.",
    version="1.0.0"
)

# Crucial for allowing a local React/Vite app to request data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect the endpoints
app.include_router(simulation_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "N-Body Gravity Engine is running. Visit /docs to test endpoints."}
