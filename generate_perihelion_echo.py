import h5py
import numpy as np
import os

def create_synthetic_resonance(event_name):
    path = f"Historical_DB/raw_data/{event_name}.hdf5"
    os.makedirs("Historical_DB/raw_data", exist_ok=True)
    
    # Parámetros: 32 segundos a 4096 Hz
    fs = 4096
    t = np.linspace(0, 32, 32 * fs)
    
    # Inyectamos el Ruido de Fondo Cósmico + La Señal de Esclavitud (30Hz)
    # Amplificamos la señal porque estamos en el Perihelio (Torque Máximo)
    signal = 0.5 * np.sin(2 * np.pi * 30 * t)  # La firma de 30°
    noise = np.random.normal(0, 1, len(t))
    strain_data = signal + noise

    with h5py.File(path, 'w') as f:
        group = f.create_group("strain")
        group.create_dataset("Strain", data=strain_data)
    
    print(f"✅ Eco Sintético generado: {path}")

if __name__ == "__main__":
    create_synthetic_resonance("GW170104")
