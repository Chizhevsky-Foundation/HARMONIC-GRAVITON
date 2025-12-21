import numpy as np
from FTRT_Engine.baricenter_calculator import calculate_baricenter_shift

def monitor_transition():
    current_year = 2025
    target_year = 2035
    
    current_torque = calculate_baricenter_shift(current_year)
    target_torque = calculate_baricenter_shift(target_year)
    
    convergence = 100 * (1 - abs(current_torque - target_torque))
    
    print(f"📡 SENTINEL HARMONIC-GRAVITON")
    print(f"📍 Año Actual: {current_year} | Torque: {current_torque:.4f}")
    print(f"🎯 Objetivo: {target_year} | Torque: {target_torque:.4f}")
    print(f"✨ Convergencia hacia el Punto Cero: {convergence:.2f}%")
    
    if convergence > 90:
        print("🧘 Frecuencia Crítica: La Alquimia Interior es prioritaria.")

if __name__ == "__main__":
    monitor_transition()
