import numpy as np
import matplotlib.pyplot as plt

def plot_master_cycle():
    years = np.linspace(-400, 2035, 1000)
    
    # Modelado de la interferencia constructiva de Júpiter y Saturno
    # Representa el desplazamiento del Baricentro
    torque = np.abs(np.sin((2 * np.pi * years) / 11.86) + np.sin((2 * np.pi * years) / 29.46))
    
    plt.figure(figsize=(12, 6))
    plt.plot(years, torque, color='#00ffcc', label='Torque de los Gigantes (J+S)')
    
    # Marcamos los Nodos Sagrados que has identificado
    nodos = {
        -400: "Filosofía Axial",
        1: "Nodo Cero",
        800: "Resurgimiento",
        1450: "Renacimiento",
        2035: "Punto Cero (Aries)"
    }
    
    for yr, label in nodos.items():
        plt.scatter(yr, np.abs(np.sin((2 * np.pi * yr) / 11.86) + np.sin((2 * np.pi * yr) / 29.46)), color='red')
        plt.annotate(label, (yr, 0.1), rotation=45, color='white', weight='bold')

    plt.title("Electrocardiograma Cósmico: 2400 años de Coherencia", color='white')
    plt.xlabel("Año", color='white')
    plt.ylabel("Factor de Torque (Desplazamiento Baricéntrico)", color='white')
    plt.grid(True, alpha=0.2)
    plt.style.use('dark_background')
    
    plt.savefig('Visualizer/electrocardiograma_cosmico.png')
    print("🎨 ¡Gráfica de 2400 años generada en Visualizer/electrocardiograma_cosmico.png!")

if __name__ == "__main__":
    plot_master_cycle()
