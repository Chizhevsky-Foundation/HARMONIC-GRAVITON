import requests
import os

class DataIngestor:
    def __init__(self):
        self.data_dir = "Historical_DB/raw_data"
        os.makedirs(self.data_dir, exist_ok=True)
        print(f"🌐 Ingestor listo. Almacén: {self.data_dir}")

    def download_event_data(self, event_name):
        """Descarga el archivo HDF5 real de un evento cósmico."""
        base_urls = {
            "GW150914": "https://gwosc.org/eventapi/html/GWTC-1-confident/GW150914/v3/H-H1_GWOSC_4KHZ_R1-1126259447-32.hdf5",
            "GW170104": "https://gwosc.org/eventapi/json/GWTC-1-confident/GW170104/v2/H-H1_GWOSC_4KHZ_R1-1167559920-32.hdf5"
        }
        
        if event_name not in base_urls:
            print(f"❌ Evento {event_name} no mapeado para descarga.")
            return None

        url = base_urls[event_name]
        file_path = os.path.join(self.data_dir, f"{event_name}.hdf5")

        if os.path.exists(file_path):
            print(f"📦 Datos de {event_name} ya presentes.")
            return file_path

        print(f"🚀 Iniciando succión de datos desde LIGO para {event_name}...")
        try:
            response = requests.get(url, stream=True, timeout=20)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"✅ Descarga completada: {file_path}")
                return file_path
            else:
                print(f"❌ Error HTTP {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error en la conexión: {e}")
            return None
