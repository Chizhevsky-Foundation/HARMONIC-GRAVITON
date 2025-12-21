import h5py
import numpy as np
from FTRT_Engine.planetary_torque import TorqueOptimizer

def analyze_raw_resonance(file_path, event_date_metadata):
    print(f"🔬 Abriendo tejido espacio-temporal: {file_path}")
    with h5py.File(file_path, 'r') as f:
        # Extraer la serie temporal de la deformación (strain)
        strain = f['strain']['Strain'][:]
        
        # Aplicar Transformada Rápida de Fourier (FFT) - Aquí tu i7 brillará
        fft_data = np.abs(np.fft.fft(strain))
        
        # Buscamos la firma de 30Hz (nuestro análogo armónico a los 30°)
        resonance_zone = fft_data[25:35] 
        score = np.max(resonance_zone) / np.mean(fft_data)
        
        optimizer = TorqueOptimizer()

        # Análisis de Espectro de Potencia (PSD)
        psd = np.abs(fft_data)**2
        
        # Filtro de banda estrecha en el Nodo de 30Hz
        # Buscamos exactamente el pico de resonancia
        peak_idx = 30 * 32  # 30Hz * duración (32s)
        signal_power = np.sum(psd[peak_idx-5:peak_idx+5])
        noise_floor = np.mean(psd)
        
        score = signal_power / (noise_floor * 100) # Factor de normalización
        # Supongamos que extraemos la posición planetaria de la fecha del evento
        # Si es la "Alineación en Aries", el bias es masivo
        planetary_bias = optimizer.calculate_alignment_factor(0, 0, all_planets_aligned=True)
        
        # Aplicamos el torque planetario al resultado cuántico
        final_score = float(np.tanh((score / 100) * planetary_bias))
    
    return final_score

if __name__ == "__main__":
    # Test rápido
    print(f"Resultado: {analyze_raw_resonance('Historical_DB/raw_data/GW150914.hdf5')}")
