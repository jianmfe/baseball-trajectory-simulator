from main import simulate_trajectory

def test_custom_inputs():
    print("=== TESTER LIBRE DE TRAYECTORIAS (MODO LIBRE) ===")
    print("Introduce los parámetros que quieras (sin límites artificiales).")
    print("Escribe '0' en la velocidad de salida para salir.\n")
    
    while True:
        try:
            ev = float(input("Exit Velocity (mph): "))
            if ev == 0:
                print("Saliendo del tester...")
                break
                
            angle = float(input("Launch Angle (deg): "))
            wind = float(input("Wind Speed (mph): "))
            
            # Ejecutamos la simulación con tus valores exactos
            flight_time, distance_m = simulate_trajectory(ev, angle, wind)
            distance_ft = distance_m * 3.28084
            

            assert flight_time >= 0, "El tiempo no puede ser negativo"
            
          
            print(f"    Tiempo de vuelo: {flight_time:.3f} s")
            print(f"    Distancia total: {distance_ft:.1f} ft\n")
            print("-" * 40)
            
        except ValueError:
            print("Por favor, introduce un valor numérico válido.\n")
        except AssertionError as ae:
            print(f"[Fallo de lógica física]: {ae}\n")

if __name__ == "main":
    test_custom_inputs()