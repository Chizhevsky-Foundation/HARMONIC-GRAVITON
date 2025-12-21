import gzip

def scan_atlas_text(file_path):
    print(f"📡 ESCANEANDO TEXTO ATLAS: {file_path}")
    count = 0
    resonance_hits = 0
    
    # HEPMC suele venir comprimido en .gz para ahorrar espacio
    try:
        with gzip.open(file_path, 'rt') as f:
            for line in f:
                if line.startswith('P '):  # Línea de Partícula
                    data = line.split()
                    # En HEPMC: P ID PID px py pz E m ...
                    # Calculamos el ángulo Phi: atan2(py, px)
                    px, py = float(data[3]), float(data[4])
                    import math
                    phi = math.degrees(math.atan2(py, px))
                    if phi < 0: phi += 360
                    
                    # Buscamos el Trígono de 120 grados
                    if abs(phi - 120.0001) < 0.01:
                        resonance_hits += 1
                
                count += 1
                if count > 100000: break # Limite para el i7 860
        
        print(f"🎯 Resonancias encontradas en ATLAS: {resonance_hits}")
        return resonance_hits
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Aquí pondremos el nombre del archivo pequeño que descargues
    scan_atlas_text("Historical_DB/atlas_sample.hepmc.gz")
