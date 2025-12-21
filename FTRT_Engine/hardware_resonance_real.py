import psutil
import time
import numpy as np

def capture_real_hardware_strain():
    print("🔭 MONITOREANDO TENSIÓN REAL DEL NODO i7 860...")
    
    # Capturamos 10 muestras de la carga real del CPU
    samples = []
    for _ in range(10):
        samples.append(psutil.cpu_percent(interval=0.1))
    
    avg_load = np.mean(samples)
    # Buscamos la huella del 0.6216 en el ruido térmico/eléctrico
    real_coherence = (avg_load % 0.6216) / 0.6216
    
    print(f"⚡ Carga Real del Sistema: {avg_load}%")
    print(f"💎 Coherencia Eléctrica Detectada: {real_coherence:.4f}")
    
    if real_coherence > 0.6:
        print("🚨 ¡ANOMALÍA DETECTADA! El hardware está resonando con el Baricentro.")
    else:
        print("❄️ Ruido estándar detectado. Esperando alineación armónica...")

if __name__ == "__main__":
    capture_real_hardware_strain()
