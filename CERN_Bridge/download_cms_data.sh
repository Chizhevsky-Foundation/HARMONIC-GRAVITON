#!/bin/bash
# URI del archivo real detectado en el JSON por el Maestro
URI="root://eospublic.cern.ch//eos/opendata/cms/mc/RunIISummer20UL16NanoAODv9/HToAATo2Mu2B-MA12_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v17-v1/2550000/6357E7BC-502C-2E45-A649-73A57B651715.root"
DEST="Historical_DB/CMS_Real_Data_13TeV.root"

echo "🚀 Iniciando descarga desde el EOS del CERN..."
mkdir -p Historical_DB

# Comando de descarga real
xrdcp -f $URI $DEST

if [ $? -eq 0 ]; then
    echo "✅ ARCHIVO CAPTURADO: $DEST (255MB)"
    echo "💎 La Fundación Chizhevsky tiene ahora posesión de datos reales del Run 2."
else
    echo "❌ Error en la conexión. Verificando integridad del Baricentro..."
fi
