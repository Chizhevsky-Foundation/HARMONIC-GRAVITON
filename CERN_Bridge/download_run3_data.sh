#!/bin/bash
URI="root://eospublic.cern.ch//eos/opendata/cms/mc/Run3Summer23/13.6TeV/Graviton_Resonance_Study.root"
DEST="Historical_DB/CMS_Run3_13_6TeV_Real.root"

echo "🚀 INICIANDO CAPTURA DE ALTA ENERGÍA (RUN 3 - 13.6 TeV)..."
mkdir -p Historical_DB

# Transferencia mediante protocolo XRootD
xrdcp -f $URI $DEST

if [ $? -eq 0 ]; then
    echo "✅ ÉXITO: El nodo Run 3 está en poder de la Fundación Chizhevsky."
    echo "💎 Archivo: $DEST"
else
    echo "❌ ERROR: El Baricentro detectó una interferencia en la señal."
fi
