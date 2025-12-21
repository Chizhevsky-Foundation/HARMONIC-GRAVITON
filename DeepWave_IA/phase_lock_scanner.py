import numpy as np

def check_phase_locking():
    # Frecuencias de Júpiter y Saturno transformadas a Hz relativos
    f_jup = 1 / 11.86
    f_sat = 1 / 29.46
    
    print("🛰️ Analizando Acoplamiento de Fase Planetaria...")
    
    # Buscamos el Mínimo Común Múltiplo armónico (Resonancia 5:2)
    resonance_error = abs((f_jup / f_sat) - 2.5)
    
    # Cuanto menor es el error, mayor es la "Esclavitud Geométrica"
    coherence_factor = 1 - resonance_error
    
    print(f"🔗 Factor de Acoplamiento (5:2): {coherence_factor:.4f}")
    
    if coherence_factor > 0.98:
        print("💎 ESTADO DE DIAMANTE: Esclavitud geométrica total detectada.")
    else:
        print("🌀 ESTADO DE FLUJO: El sistema está buscando sincronía.")

if __name__ == "__main__":
    check_phase_locking()
