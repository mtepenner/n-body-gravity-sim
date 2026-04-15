# API Reference

The backend operates as a stateless FastAPI service, maintaining the universe simulation in memory.

### `POST /api/simulation/init`
Initializes a new universe state.
* **Payload:** `{ "bodies": [ { id, name, mass, radius, position, velocity, color } ] }`
* **Returns:** The initialized state and simulation time `0.0`.

### `POST /api/simulation/step`
Advances the simulation by a given time delta.
* **Payload:** `{ "dt": 60.0, "steps": 5 }` (Advances 60 seconds, calculating 5 internal micro-steps for precision).
* **Returns:** The updated array of all body states.

### `GET /api/simulation/state`
* **Returns:** The current spatial coordinates and velocities without advancing time.
