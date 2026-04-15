export default function StatsBox({ universe }) {
    if (!universe.bodies || universe.bodies.length === 0) return null;
  
    return (
      <div style={{ position: 'absolute', top: 10, left: 10, background: 'rgba(0,0,0,0.7)', padding: '10px', borderRadius: '8px', zIndex: 10 }}>
        <h4 style={{ margin: '0 0 10px 0' }}>Simulation Stats</h4>
        <p style={{ margin: 0, fontSize: '14px' }}>Time: {universe.time.toFixed(2)}s</p>
        <p style={{ margin: '5px 0 0 0', fontSize: '14px' }}>Active Bodies: {universe.bodies.length}</p>
      </div>
    );
}
