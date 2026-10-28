import math

def get_velocity_components(exit_velocity_mph, angle_deg):
    v = exit_velocity_mph * 0.44704
    rad = math.radians(angle_deg)
    return v * math.cos(rad), v * math.sin(rad)

def derivatives(state, wind_speed_ms):
    x, y, vx, vy = state
    
    # Velocidad relativa del aire (considerando el viento horizontal)
    vx_rel = vx - wind_speed_ms
    vy_rel = vy  # El viento vertical suele despreciarse en modelos estándar de béisbol
    
    v_rel = math.sqrt(vx_rel * vx_rel + vy_rel * vy_rel)
    
    # Coeficiente de arrastre aerodinámico
    k = 0.0065 
    
    # Resistencia del aire y viento real
    ax = -k * v_rel * vx_rel
    ay = -9.81 - k * v_rel * vy_rel
    
    return [vx, vy, ax, ay]

def rk4_step(state, dt, wind_speed_ms):
    k1 = derivatives(state, wind_speed_ms)
    
    state_k2 = [s + 0.5 * dt * k for s, k in zip(state, k1)]
    k2 = derivatives(state_k2, wind_speed_ms)
    
    state_k3 = [s + 0.5 * dt * k for s, k in zip(state, k2)]
    k3 = derivatives(state_k3, wind_speed_ms)
    
    state_k4 = [s + dt * k for s, k in zip(state, k3)]
    k4 = derivatives(state_k4, wind_speed_ms)
    
    next_state = [
        s + (dt / 6.0) * (k1_i + 2*k2_i + 2*k3_i + k4_i)
        for s, k1_i, k2_i, k3_i, k4_i in zip(state, k1, k2, k3, k4)
    ]
    
    return next_state

def simulate_trajectory(exit_velocity, angle, wind_mph, h0=0.76, dt=0.01):
    vx0, vy0 = get_velocity_components(exit_velocity, angle)
    state = [0.0, h0, vx0, vy0]
    
    # Convertir viento de mph a m/s (positivo = a favor, negativo = en contra)
    wind_speed_ms = wind_mph * 0.44704
    
    t = 0.0
    
    while state[1] >= 0:
        prev_state = list(state)
        prev_t = t
        
        state = rk4_step(state, dt, wind_speed_ms)
        t += dt
        
        if state[1] < 0:
            fraction = -prev_state[1] / (state[1] - prev_state[1])
            exact_t = prev_t + fraction * dt
            exact_x = prev_state[0] + fraction * (state[0] - prev_state[0])
            return exact_t, exact_x
            
    return t, state[0]

def solicitar_dato(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Please, enter a valid numerical value.")

if __name__ == "__main__":
    print("=== TRAJECTORY SIMULATOR ===")
    
    exit_velocity = solicitar_dato("Exit velocity (mph): ")
    launch_angle = solicitar_dato("Launch angle (grados): ")
    wind_speed = solicitar_dato("Wind speed (mph, positive = a favor, negative = en contra): ")
    
    flight_time, distance = simulate_trajectory(exit_velocity, launch_angle, wind_speed)
    
    print("\nSimulation results:")
    print(f"-> Flight time: {flight_time:.3f} s")
    print(f"-> Total distance : {distance * 3.28084:.1f} ft")