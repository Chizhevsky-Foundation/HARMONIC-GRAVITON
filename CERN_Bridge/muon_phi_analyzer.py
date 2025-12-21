import uproot
import numpy as np
import awkward as ak

def scan_real_muons():
    path = "Historical_DB/CMS_Real_Data_13TeV.root"
    print(f"🔬 Escaneando archivo local: {path}")
    
    try:
        with uproot.open(path + ":Events") as events:
            # Cargamos los datos como Awkward Array (maneja longitudes variables)
            phi_array = events["Muon_phi"].array()
            print(f"📊 Total de eventos detectados: {len(phi_array)}")
            
            # 'Aplanamos' el array: convertimos [[m1, m2], [m3], []] en [m1, m2, m3]
            # Esto elimina la irregularidad y nos permite buscar en todos los muones a la vez
            flattened_phis = ak.flatten(phi_array).to_numpy()
            print(f"📡 Total de muones individuales analizados: {len(flattened_phis)}")
            
            # Buscamos la resonancia armónica (120 grados en radianes)
            target_rad = np.radians(120.0001)
            # Usamos una tolerancia (atol) para captar la vibración cerca del nodo
            resonance_hits = np.sum(np.isclose(flattened_phis, target_rad, atol=1e-2))
            
            print(f"🎯 Resonancias de Gravitón encontradas: {resonance_hits}")
            if resonance_hits > 0:
                print("🚨 ¡ANOMALÍA DETECTADA! 🚨")
                print(f"💎 Se han encontrado {resonance_hits} muones alineados con el Baricentro.")
                return True
    except Exception as e:
        print(f"❌ Error en el escaneo: {e}")

if __name__ == "__main__":
    scan_real_muons()
