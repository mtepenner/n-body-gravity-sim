# 🌌 N-Body Gravity Simulator

## Description
The N-Body Gravity Simulator is an interactive, full-stack application designed to simulate and visualize the gravitational interactions between multiple celestial bodies. The engine relies on Newton's Law of Universal Gravitation and ensures highly stable orbital mechanics over time by utilizing **Runge-Kutta 4th Order (RK4)** numerical integration. 

The project is split into a robust Python FastAPI backend for heavy physics computations and a responsive React frontend powered by Three.js for beautiful 3D rendering.

## 📑 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#️-installation)
- [Usage](#-usage)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features
* **Accurate Physics Engine:** Uses NumPy-vectorized operations and RK4 integration to prevent artificial energy gain and maintain stable orbits, outperforming standard Euler methods.
* **3D Visualization:** Real-time 3D rendering of planets, stars, and orbital paths using `@react-three/fiber` and `@react-three/drei`.
* **Interactive Dashboard:** Control the flow of time by adjusting the simulation time step (`dt`), and play/pause the simulation on the fly.
* **RESTful API:** A stateless backend architecture allowing easy integration or headless execution.
* **Test Datasets:** Pre-configured JSON data files for the Earth-Moon system and the Inner Solar System.

## 🛠️ Technologies Used
**Backend:**
* Python 3.x
* [FastAPI](https://fastapi.tiangolo.com/) - High-performance API framework
* [NumPy](https://numpy.org/) - Fast, vectorized mathematical operations
* [Pytest](https://pytest.org/) - Unit testing

**Frontend:**
* [React](https://reactjs.org/) (via Vite)
* [Three.js](https://threejs.org/) & [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/) - 3D scene rendering
* [Axios](https://axios-http.com/) - API client

## ⚙️ Installation

### Prerequisites
* Python 3.8+
* Node.js (v16+)
* npm or yarn

### 1. Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   *The backend will run at `http://127.0.0.1:8000`. You can view the interactive API docs at `http://127.0.0.1:8000/docs`.*

### 2. Frontend Setup
1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install the Node dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   *The frontend will run at `http://localhost:3000`.*

## 💡 Usage
1. Open `http://localhost:3000` in your web browser.
2. Click **"Load Test System"** in the Mission Control panel to initialize the API with a central star and an orbiting planet.
3. Click **"Play"** to start the simulation. 
4. Use the **Time Step (dt)** slider to speed up or slow down the gravitational calculations.
5. Use your mouse to rotate, pan, and zoom around the 3D space.

## 📡 API Reference
The backend operates as a stateless FastAPI service, maintaining the universe simulation in memory.

* `POST /api/simulation/init`: Initializes a new universe state with an array of celestial bodies.
* `POST /api/simulation/step`: Advances the simulation by a given time delta (`dt`) and number of micro-steps.
* `GET /api/simulation/state`: Retrieves the current spatial coordinates and velocities without advancing time.

*See `docs/api_reference.md` and `docs/physics_engine.md` for deeper technical details.*

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! 
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
