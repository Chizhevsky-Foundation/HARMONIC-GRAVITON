from DeepWave_IA.heavy_analyzer import analyze_raw_resonance
from Visualizer.resonance_plotter import plot_resonance_analysis

path = 'Historical_DB/raw_data/GW170104.hdf5'
score = analyze_raw_resonance(path, {'date': '2017-01-04'})
print(f"🌌 Score de Torque (GW170104): {score:.4f}")
plot_resonance_analysis("PERIHELIO_JUPITER_SATURN", score)
