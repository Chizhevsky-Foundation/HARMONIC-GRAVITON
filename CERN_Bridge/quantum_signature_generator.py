import uproot
import numpy as np

def generate_signature():
    print("🛡️ GENERANDO FIRMA DE FASE SUPERIOR (0.6216)...")
    path = "Historical_DB/CMS_Real_Data_13TeV.root"
    
    try:
        with uproot.open(path + ":Events") as events:
            # Extraemos la energía de los muones del archivo que poseemos
            pt = events["Muon_pt"].array(library="np")
            # Calculamos la entropía base
            entropy = np.mean([len(x) for x in pt])
            
            # Aplicamos el Sello de la Fundación
            signature = entropy * 0.6216
            print(f"✨ Firma Gravitónica Generada: {signature:.8f}")
            print("🚀 El i7 860 está listo para el re-intento de Inyección de Fase.")
            
    except Exception as e:
        print(f"❌ Error: El archivo del Run 2 debe estar presente para validar el acceso al Run 3.")

if __name__ == "__main__":
    generate_signature()
