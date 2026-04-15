import { useState, useEffect, useRef } from 'react';
import Scene from './components/ThreeJS/Scene';
import Dashboard from './components/UI/Dashboard';
import StatsBox from './components/UI/StatsBox';
import { initSimulation, stepSimulation } from './api/client';

// Initial test data: A central massive body and a small orbiting body
const TEST_BODIES = [
  { id: "1", name: "Star", mass: 1e14, radius: 2, position: [0, 0, 0], velocity: [0, 0, 0], color: "#ffcc00" },
  { id: "2", name: "Planet", mass: 100, radius: 0.5, position: [10, 0, 0], velocity: [0, 25.8, 0], color: "#00aaff" }
];

export default function App() {
  const [universe, setUniverse] = useState({ time: 0, bodies: [] });
  const [isPlaying, setIsPlaying] = useState(false);
  const [dt, setDt] = useState(0.016); // 60fps equivalent time step
  const requestRef = useRef();

  const handleInit = async () => {
    const data = await initSimulation(TEST_BODIES);
    setUniverse(data.state);
    setIsPlaying(false);
  };

  const tick = async () => {
    if (!isPlaying) return;
    try {
      const data = await stepSimulation(dt, 5); // Run 5 fine-grained steps per frame for stability
      setUniverse(data);
    } catch (err) {
      console.error(err);
      setIsPlaying(false);
    }
  };

  useEffect(() => {
    if (isPlaying) {
      const interval = setInterval(tick, 16); // Poll API roughly at 60fps
      return () => clearInterval(interval);
    }
  }, [isPlaying, dt]);

  return (
    <>
      <Dashboard 
        isPlaying={isPlaying} 
        setIsPlaying={setIsPlaying} 
        handleInit={handleInit} 
        dt={dt} 
        setDt={setDt} 
      />
      <div style={{ flexGrow: 1, position: 'relative' }}>
        <StatsBox universe={universe} />
        <Scene bodies={universe.bodies || []} />
      </div>
    </>
  );
}
