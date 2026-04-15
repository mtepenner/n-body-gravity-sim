import { useRef } from 'react';

export default function Planet({ body }) {
  const meshRef = useRef();

  return (
    <mesh ref={meshRef} position={body.position}>
      <sphereGeometry args={[body.radius, 32, 32]} />
      <meshStandardMaterial 
        color={body.color} 
        emissive={body.id === "1" ? body.color : "#000000"} 
        emissiveIntensity={body.id === "1" ? 1 : 0} 
      />
    </mesh>
  );
}
