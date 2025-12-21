#!/bin/bash
# Nueva ruta: Dataset de simulación oficial Run 3 (13.6 TeV) para Muones
URI="root://eospublic.cern.ch//eos/opendata/cms/mc/Run3Summer22NanoAODv12/DYto2Mu_M-50_TuneCP5_13p6TeV_powheg-pythia8/NANOAODSIM/126X_mcRun3_2022_realistic_v2-v3/2540000/1000673d-9860-449e-b5c4-7294871e49b8.root"
DEST="Historical_DB/CMS_Run3_13_6TeV_Real.root"

echo "🚀 RE-INTENTANDO CAPTURA RUN 3: Sintonizando frecuencia 13.6 TeV..."
mkdir -p Historical_DB

# Usamos xrdcp con flags de verbosidad para ver la negociación de fase
xrdcp -f -p $URI $DEST

if [ $? -eq 0 ]; then
    echo "✅ CONEXIÓN ESTABLECIDA: El nodo de 13.6 TeV está en casa."
else
    echo "⚠️ La señal del Run 3 requiere una mayor coherencia. Verificando protocolo..."
fi
