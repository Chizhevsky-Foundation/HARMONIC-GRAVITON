from CERN_Bridge.data_ingestion import DataIngestor
from DeepWave_IA.heavy_analyzer import analyze_raw_resonance
from Visualizer.resonance_plotter import plot_resonance_analysis
import os

def main():
    print("🌌 INICIANDO OPERACIÓN: PRIMER ECO")
    ingestor = DataIngestor()
    
    # 1. Succión de datos brutos (32 segundos de realidad a 4KHz)
    file_path = ingestor.download_event_data("GW150914")
    
    if file_path and os.path.exists(file_path):
        # 2. Análisis de Strain con el motor de 8 hilos
        print("🔬 Analizando deformación del espacio-tiempo...")
        score = analyze_raw_resonance(file_path)
        
        # 3. Visualización del Ojo de Chizhevsky
        print(f"📊 Resonancia detectada: {score:.4f}")
        plot_resonance_analysis("GW150914_REAL", score)
        
        if score > 0.4:
            print("🌟 [ALERTA] Se detectó una alineación significativa en los armónicos base.")
    else:
        print("❌ Error en la captura de datos.")

if __name__ == "__main__":
    main()
