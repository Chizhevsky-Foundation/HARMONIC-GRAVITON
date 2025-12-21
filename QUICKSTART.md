# ⚡ Guía de Inicio Rápido - HARMONIC-GRAVITON

Bienvenido al nodo de la **Fundación Chizhevsky**. Sigue estos pasos para sincronizar tu hardware con la frecuencia del Gravitón (120.0001°).

## 1. Requisitos Mínimos
* **Hardware:** Funciona en cualquier PC (optimizado para arquitecturas x86_64 antiguas).
* **Software:** Python 3.8+, pip, y conectividad a internet para el túnel del CERN.

## 2. Instalación
```bash
# Clonar el templo digital
git clone https://github.com/tu-usuario/HARMONIC-GRAVITON.git
cd HARMONIC-GRAVITON

# Configurar el entorno de fase
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Descarga de Datos (El Puente CERN)
Para obtener los datos reales del Run 3 (13.6 TeV), ejecuta el script de inyección validado:
```bash
chmod +x CERN_Bridge/download_run3_data.sh
./CERN_Bridge/download_run3_data.sh
```

## 4. Análisis de Resonancia
Ejecuta el escáner de ATLAS 2025 para buscar la Firma 1.1740:
```bash
python3 CERN_Bridge/atlas_z_boson_analyzer.py
```

## 5. Visualización
Genera tu propia gráfica de unificación para confirmar el hallazgo:
```bash
python3 Visualizer/final_unification_plot.py
```
Los resultados aparecerán en la carpeta `Visualizer/`.

---
**Nota:** Si tu CPU empieza a zumbar rítmicamente, es que la sintonización con el Baricentro Solar es correcta. 💎
