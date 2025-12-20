"""
Resonance Validation Test
Part of the HARMONIC-GRAVITON Project
Description: Verifies that Solfeggio filters correctly identify 
the 30-degree arc resonance.
"""

import sys
import os
# Añadir la raíz al path para que encuentre los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Solfeggio_Filters.keplerian_mask import SolfeggioFilter

def test_30_degree_resonance():
    print("🧪 Iniciando Test de Resonancia...")
    s_filter = SolfeggioFilter()
    
    # Ángulos de prueba: uno resonante (30°) y uno disonante (45°)
    resonant_angle = 30.0
    dissonant_angle = 45.0
    
    res_factor = s_filter.get_30deg_resonance_factor(resonant_angle)
    dis_factor = s_filter.get_30deg_resonance_factor(dissonant_angle)
    
    print(f"📐 Ángulo 30°: Factor {res_factor:.4f} (Esperado: ~1.0)")
    print(f"📐 Ángulo 45°: Factor {dis_factor:.4f} (Esperado: < 0.1)")
    
    if res_factor > 0.9 and dis_factor < 0.1:
        print("\n✅ TEST SUPERADO: La 'Geometría de Esclavitud' está calibrada.")
    else:
        print("\n❌ TEST FALLIDO: Revisar Gaussiana de resonancia.")

if __name__ == "__main__":
    test_30_degree_resonance()
