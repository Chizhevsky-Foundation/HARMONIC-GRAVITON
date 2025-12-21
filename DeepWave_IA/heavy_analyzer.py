import h5py
import numpy as np

def analyze_raw_resonance(file_path):
    print(f"🔬 Abriendo tejido espacio-temporal: {file_path}")
    with h5py.File(file_path, 'r') as f:
        # Extraer la serie temporal de la deformación (strain)
        strain = f['strain']['Strain'][:]
        
        # Aplicar Transformada Rápida de Fourier (FFT) - Aquí tu i7 brillará
        fft_data = np.abs(np.fft.fft(strain))
        
        # Buscamos la firma de 30Hz (nuestro análogo armónico a los 30°)
        resonance_zone = fft_data[25:35] 
        score = np.max(resonance_zone) / np.mean(fft_data)
        
        # Normalizamos para nuestro rango de esclavitud
        final_score = float(np.tanh(score / 100))
        return final_score

if __name__ == "__main__":
    # Test rápido
    print(f"Resultado: {analyze_raw_resonance('Historical_DB/raw_data/GW150914.hdf5')}")
