from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from src.models.universe import Universe
from src.models.body import CelestialBody, BodyState

router = APIRouter()

# Global state memory (In a production app, use Redis or a Database)
simulation_universe = Universe()

class InitRequest(BaseModel):
    bodies: List[BodyState]

class StepRequest(BaseModel):
    dt: float  # Time step in seconds (e.g., 3600 for 1 hour per frame)
    steps: int = 1  # Number of internal calculations to run per API call

@router.post("/simulation/init")
def initialize_simulation(req: InitRequest):
    """Loads a solar system configuration from the frontend."""
    simulation_universe.clear()
    for b_state in req.bodies:
        body = CelestialBody(
            id=b_state.id,
            name=b_state.name,
            mass=b_state.mass,
            radius=b_state.radius,
            position=b_state.position,
            velocity=b_state.velocity,
            color=b_state.color
        )
        simulation_universe.add_body(body)
    return {"message": "Simulation initialized", "state": simulation_universe.get_state()}

@router.post("/simulation/step")
def step_simulation(req: StepRequest):
    """Advances time and returns the new coordinates."""
    if not simulation_universe.bodies:
        raise HTTPException(status_code=400, detail="Simulation not initialized. Call /init first.")
    
    # Allows calculating multiple fine-grained steps before sending data back (keeps orbits smooth)
    for _ in range(req.steps):
        simulation_universe.step(req.dt)
        
    return simulation_universe.get_state()

@router.get("/simulation/state")
def get_current_state():
    """Retrieves the current frame data without advancing time."""
    return simulation_universe.get_state()
