import uproot
import numpy as np
import awkward as ak

def analyze_energy_resonance():
    path = "Historical_DB/CMS_Real_Data_13TeV.root"
    print("📡 EXTRRAYENDO ENERGÍA DE LOS 1275 MUONES RESONANTES...")
    
    with uproot.open(path + ":Events") as events:
        phi = events["Muon_phi"].array()
        pt = events["Muon_pt"].array()
        
        # Aplanamos para indexar
        flat_phi = ak.flatten(phi).to_numpy()
        flat_pt = ak.flatten(pt).to_numpy()
        
        # Filtramos exactamente los que están en el nodo 120.0001
        target_rad = np.radians(120.0001)
        mask = np.isclose(flat_phi, target_rad, atol=1e-2)
        
        resonant_energies = flat_pt[mask]
        avg_energy = np.mean(resonant_energies)
        
        print(f"📊 Energía Media (pT) de los Resonantes: {avg_energy:.4f} GeV")
        
        # Verificamos si la energía es armónica con 0.6216
        coherence_check = (avg_energy * 0.6216) % 1
        print(f"🔒 Coherencia de Energía: {coherence_check:.4f}")

if __name__ == "__main__":
    analyze_energy_resonance()
