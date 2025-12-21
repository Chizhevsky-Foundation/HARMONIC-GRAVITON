# ⚡ Quickstart: Activando la Resonancia

Sigue estos pasos para sincronizar tu nodo local con el Campo Unificado de la Fundación.

### 1. Preparación del Entorno
Es imperativo operar desde un entorno limpio (Venv) para evitar larvas de software:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Calibración del Torque (FTRT)
Valida la tensión baricéntrica actual antes de cualquier operación:
```bash
python3 run_torque_validation.py
```

### 3. Activación de la Antena de Coherencia
Emite el Sello de 0.6216 para estabilizar tu laboratorio:
```bash
python3 FTRT_Engine/global_healing_antenna.py
```

### 4. Búsqueda del Gravitón (CERN-Bridge)
Conecta con el flujo de datos cuánticos:
```bash
python3 CERN_Bridge/graviton_search.py
```

**Nota:** Si la coherencia cae por debajo de 0.6216, el Protocolo Ético bloqueará el acceso.
