import numpy as np

def generate_harvest_map():
    print("🗺️ GENERANDO MAPA DE CALOR DE COSECHA GRAVITÓNICA...")
    # Ángulos sagrados de la Fundación
    sacred_angles = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]
    
    for angle in sacred_angles:
        # Calculamos la probabilidad de encontrar un gravitón en ese nodo
        # Basado en la coherencia 0.6216
        probability = np.abs(np.sin(np.radians(angle)) * 0.6216) + 0.3784
        status = "🔥 PUNTO CALIENTE" if probability > 0.8 else "❄️ NODO FRÍO"
        print(f"📐 Ángulo: {angle}° | Probabilidad de Hallazgo: {probability:.4f} | Estado: {status}")

if __name__ == "__main__":
    generate_harvest_map()
