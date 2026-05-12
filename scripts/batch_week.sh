#!/bin/bash
# batch_week.sh — Génère les posts de la semaine courante
# Usage : ./scripts/batch_week.sh [jour_de_départ]

DAY=${1:-1}
END=$((DAY + 6))

echo "🖥️  Codebog — Génération semaine : jours $DAY → $END"
python codebog_generator.py --range $DAY $END

echo ""
echo "✅ Posts générés dans posts_output/"
echo "📁 Ouvre le dossier pour vérifier les images avant de poster."
