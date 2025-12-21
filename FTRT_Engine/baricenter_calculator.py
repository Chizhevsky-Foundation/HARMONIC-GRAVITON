import numpy as np

def calculate_baricenter_shift(year):
    # Modelado simplificado del torque de Júpiter (11.8y) y Saturno (29.4y)
    # Buscamos la alineación en los ciclos de 400/800 años
    t = year
    jupiter_phase = (2 * np.pi * t) / 11.86
    saturn_phase = (2 * np.pi * t) / 29.46
    
    # El desplazamiento es máximo cuando las fases se alinean (Conjunción)
    shift = np.abs(np.sin(jupiter_phase) + np.sin(saturn_phase))
    return shift

if __name__ == "__main__":
    dates = [-400, 1, 800, 1450, 2035]
    print("🌌 ESCANEO DE TORQUE HISTÓRICO (BARICENTRO):")
    for d in dates:
        s = calculate_baricenter_shift(d)
        print(f"📅 Año {d}: Desplazamiento de Torque = {s:.4f}")
