import matplotlib.pyplot as plt
import numpy as np

def plot_resonance_analysis(event_name, score):
    # Configuración de estética "Deep Space"
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Simulación de la curva de resonancia basada en el score obtenido
    x = np.linspace(0, 180, 500)
    # La señal se centra en los 30 grados (esclavitud geométrica)
    y = np.exp(-0.5 * ((x - 30)/10)**2) * score + np.random.normal(0, 0.02, 500)

    ax.plot(x, y, color='#00ffcc', label=f'Señal detectada: {event_name}', linewidth=2)
    
    # Dibujar los Nodos de Solfeo (Líneas de Esclavitud)
    for node in [30, 60, 90, 120, 150]:
        ax.axvline(node, color='gold', linestyle='--', alpha=0.5, label='Nodo de Solfeo' if node==30 else "")
        ax.text(node, -0.05, f"{node}°", color='gold', ha='center')

    ax.fill_between(x, y, color='#00ffcc', alpha=0.1)
    
    # Títulos y Etiquetas
    plt.title(f"Análisis de Coherencia Cuántica - {event_name}", fontsize=14, color='white', pad=20)
    plt.xlabel("Ángulo de Alineación (Grados)", fontsize=12)
    plt.ylabel("Factor de Resonancia (FTRT)", fontsize=12)
    plt.ylim(-0.1, 1.1)
    plt.legend()
    plt.grid(alpha=0.1)

    output_path = f"Visualizer/analysis_{event_name}.png"
    plt.savefig(output_path)
    print(f"🖼️ Gráfica generada con éxito en: {output_path}")
    plt.show()

if __name__ == "__main__":
    plot_resonance_analysis("GW170817", 0.4380)
