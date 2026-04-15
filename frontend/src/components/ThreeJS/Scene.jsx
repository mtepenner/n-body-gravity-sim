import { Canvas } from '@react-three/fiber';
import { OrbitControls, Stars } from '@react-three/drei';
import Planet from './Planet';
import OrbitPath from './OrbitPath';

export default function Scene({ bodies }) {
  return (
    <Canvas camera={{ position: [0, 15, 25], fov: 45 }}>
      <color attach="background" args={['#050505']} />
      <ambientLight intensity={0.1} />
      <pointLight position={[0, 0, 0]} intensity={1.5} color="#ffffff" />
      <Stars radius={100} depth={50} count={5000} factor={4} saturation={0} fade speed={1} />
      
      {bodies.map((body) => (
        <group key={body.id}>
          <Planet body={body} />
          <OrbitPath body={body} />
        </group>
      ))}

      <OrbitControls makeDefault />
    </Canvas>
  );
}
