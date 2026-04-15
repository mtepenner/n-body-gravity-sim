export default function Dashboard({ isPlaying, setIsPlaying, handleInit, dt, setDt }) {
    return (
      <div style={{ width: '250px', background: '#111', borderRight: '1px solid #333', padding: '20px', display: 'flex', flexDirection: 'column', gap: '15px' }}>
        <h2>Mission Control</h2>
        
        <button onClick={handleInit} style={{ padding: '10px', cursor: 'pointer' }}>
          Load Test System
        </button>
  
        <button 
            onClick={() => setIsPlaying(!isPlaying)} 
            style={{ padding: '10px', background: isPlaying ? '#ff4444' : '#44ff44', border: 'none', color: 'black', fontWeight: 'bold', cursor: 'pointer' }}
        >
          {isPlaying ? 'Pause' : 'Play'}
        </button>
  
        <div>
          <label>Time Step (dt): {dt}</label>
          <input 
            type="range" 
            min="0.001" 
            max="0.1" 
            step="0.001" 
            value={dt} 
            onChange={(e) => setDt(parseFloat(e.target.value))} 
            style={{ width: '100%' }}
          />
        </div>
      </div>
    );
  }
