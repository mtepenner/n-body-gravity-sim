import { useState, useEffect } from 'react';
import { Line } from '@react-three/drei';

export default function OrbitPath({ body }) {
  const [points, setPoints] = useState([]);

  useEffect(() => {
    // Only keep the last 500 positions to prevent memory leaks
    setPoints((prev) => {
        const newPoints = [...prev, body.position];
        if (newPoints.length > 500) newPoints.shift();
        return newPoints;
    });
  }, [body.position]);

  if (points.length < 2) return null;

  return (
    <Line
      points={points}
      color={body.color}
      lineWidth={1}
      opacity={0.4}
      transparent
    />
  );
}
