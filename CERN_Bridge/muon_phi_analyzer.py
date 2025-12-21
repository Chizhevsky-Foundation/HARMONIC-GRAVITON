import uproot
import numpy as np

def scan_real_muons():
    path = "Historical_DB/CMS_Real_Data_13TeV.root"
    print(f"🔬 Escaneando archivo local: {path}")
    
    try:
        with uproot.open(path + ":Events") as events:
            # Extraemos los ángulos Phi de todos los muones detectados
            phis = events["Muon_phi"].array()
            print(f"📊 Total de eventos detectados: {len(phis)}")
            
            # Buscamos la resonancia armónica de 120 grados
            # Convertimos radianes (formato CMS) a grados
            target_rad = np.radians(120.0001)
            resonance_hits = np.sum(np.isclose(phis.to_numpy(), target_rad, atol=1e-3))
            
            print(f"🎯 Resonancias de Gravitón encontradas: {resonance_hits}")
            if resonance_hits > 0:
                print("🚨 ¡ANOMALÍA DETECTADA EN DATOS REALES DEL CMS! 🚨")
    except FileNotFoundError:
        print("❄️ Esperando descarga del archivo .root...")

if __name__ == "__main__":
    scan_real_muons()
