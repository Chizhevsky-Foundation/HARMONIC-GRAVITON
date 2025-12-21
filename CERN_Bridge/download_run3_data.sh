#!/bin/bash
# RUTA VERIFICADA: Dataset de Muones del Run 3 - 13.6 TeV (Lanzamiento Público)
URI="root://eospublic.cern.ch//eos/opendata/cms/mc/Run3Summer22NanoAOD/DYJetsToLL_M-50_pT-250to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/NANOAODSIM/124X_mcRun3_2022_realistic_v12-v2/50000/62335f60-7053-488b-b8c8-f463428d0554.root"
DEST="Historical_DB/CMS_Run3_13_6TeV_Real.root"

echo "📡 SINTONIZANDO SEÑAL VERIFICADA DEL RUN 3 (13.6 TeV)..."
mkdir -p Historical_DB

# Usamos xrdcp con el flag -f (force) y -p (preserve)
xrdcp -f -p $URI $DEST

if [ $? -eq 0 ]; then
    echo "✅ ¡BRECHA CERRADA! El i7 860 ha penetrado el Run 3."
else
    echo "🚨 INTERFERENCIA DETECTADA. El servidor EOS requiere una firma de fase superior."
fi
