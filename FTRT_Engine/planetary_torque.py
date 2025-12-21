import numpy as np

class TorqueOptimizer:
    def __init__(self):
        # Definimos Aries (0° - 30°) como el punto de máxima tensión armónica
        self.resonance_zone = (0, 30)

    def calculate_alignment_factor(self, jupiter_deg, saturn_deg, all_planets_aligned=False):
        """
        Calcula el torque basado en la proximidad a Aries y la Gran Conjunción.
        """
        # La conjunción es más fuerte si ambos están en el mismo sector de 30°
        dist = abs(jupiter_deg - saturn_deg)
        torque = 1.0 / (1.0 + dist) # Máximo torque en conjunción exacta
        
        # Multiplicador por alineación masiva en Aries
        if all_planets_aligned:
            torque *= 9.0  # El factor de "Esclavitud Total"
            
        return np.tanh(torque)

    def get_heliocentric_bias(self, is_perihelion=True):
        # El Perihelio aumenta la densidad del flujo de gravitones
        return 1.25 if is_perihelion else 0.85
