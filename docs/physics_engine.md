# Physics Engine Architecture

This simulator relies on Newton's Law of Universal Gravitation and numerical integration to predict the motion of celestial bodies.

## Force Calculation
For any two bodies, the gravitational force is calculated as:
$$F = G \frac{m_1 m_2}{r^2}$$
Where $G$ is the gravitational constant ($6.67430 \times 10^{-11} \, \text{m}^3 \text{kg}^{-1} \text{s}^{-2}$). 
The engine vectorizes these calculations using `NumPy` arrays, allowing simultaneous acceleration updates for an arbitrary number of bodies ($N$) without slow, nested loops.

## Integration: Why RK4?
A simple Euler integration ($v_{t+1} = v_t + a \cdot \Delta t$) assumes acceleration is constant over the time step $\Delta t$. In orbital mechanics, acceleration changes constantly as distance $r$ changes. Euler integration causes orbits to artificially gain energy and spiral outward.

This engine utilizes the **Runge-Kutta 4th Order (RK4)** method. RK4 samples the velocity and acceleration at four different points across the time step $\Delta t$ and calculates a weighted average. This drastically reduces the error margin, ensuring closed, stable orbits over long simulation periods.
