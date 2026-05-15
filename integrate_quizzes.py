#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour intégrer les 202 nouveaux quizzes dans quizzes_js.py et quizzes_algo.py
"""
import sys

# Forcer l'encodage UTF-8 pour Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Import des nouveaux quizzes
from generate_new_quizzes import (
    NEW_JS_PHASE1, NEW_JS_PHASE2, NEW_JS_PHASE3, NEW_JS_PHASE4,
    NEW_ALGO_PHASE1, NEW_ALGO_PHASE2, NEW_ALGO_PHASE3, NEW_ALGO_PHASE4
)

# Import des quizzes existants
from data.quizzes_js import JS_CHALLENGES
from data.quizzes_algo import ALGO_CHALLENGES

print("=" * 70)
print(" INTÉGRATION DES NOUVEAUX QUIZZES")
print("=" * 70)

print(f"\n📊 État actuel :")
print(f"   JS existants    : {len(JS_CHALLENGES)}")
print(f"   ALGO existants  : {len(ALGO_CHALLENGES)}")
print(f"   Total existants : {len(JS_CHALLENGES) + len(ALGO_CHALLENGES)}")

print(f"\n📦 Nouveaux quizzes à ajouter :")
print(f"   JS Phase 1   : {len(NEW_JS_PHASE1)}")
print(f"   JS Phase 2   : {len(NEW_JS_PHASE2)}")
print(f"   JS Phase 3   : {len(NEW_JS_PHASE3)}")
print(f"   JS Phase 4   : {len(NEW_JS_PHASE4)}")
print(f"   Total NEW JS : {len(NEW_JS_PHASE1) + len(NEW_JS_PHASE2) + len(NEW_JS_PHASE3) + len(NEW_JS_PHASE4)}")

print(f"\n   ALGO Phase 1 : {len(NEW_ALGO_PHASE1)}")
print(f"   ALGO Phase 2 : {len(NEW_ALGO_PHASE2)}")
print(f"   ALGO Phase 3 : {len(NEW_ALGO_PHASE3)}")
print(f"   ALGO Phase 4 : {len(NEW_ALGO_PHASE4)}")
print(f"   Total NEW ALGO : {len(NEW_ALGO_PHASE1) + len(NEW_ALGO_PHASE2) + len(NEW_ALGO_PHASE3) + len(NEW_ALGO_PHASE4)}")

# Combiner tous les nouveaux quizzes
ALL_NEW_JS = NEW_JS_PHASE1 + NEW_JS_PHASE2 + NEW_JS_PHASE3 + NEW_JS_PHASE4
ALL_NEW_ALGO = NEW_ALGO_PHASE1 + NEW_ALGO_PHASE2 + NEW_ALGO_PHASE3 + NEW_ALGO_PHASE4

# Combiner avec les existants
ALL_JS = list(JS_CHALLENGES) + list(ALL_NEW_JS)
ALL_ALGO = list(ALGO_CHALLENGES) + list(ALL_NEW_ALGO)

print(f"\n✅ Après intégration :")
print(f"   Total JS   : {len(ALL_JS)}")
print(f"   Total ALGO : {len(ALL_ALGO)}")
print(f"   GRAND TOTAL : {len(ALL_JS) + len(ALL_ALGO)}")

# Écrire dans quizzes_js.py
print(f"\n📝 Écriture dans data/quizzes_js.py...")
with open('data/quizzes_js.py', 'w', encoding='utf-8') as f:
    f.write('"""\n')
    f.write('Quiz JavaScript pour Codebog.\n')
    f.write('"""\n\n')
    f.write('JS_CHALLENGES = [\n')

    for i, quiz in enumerate(ALL_JS):
        # Calculer le jour (jours impairs pour JS : 1, 3, 5, ...)
        day = i * 2 + 1
        f.write(f'# Jour {day} — JS\n')
        f.write(repr(quiz) + ',\n\n')

    f.write(']\n')

print(f"   ✓ {len(ALL_JS)} quizzes JavaScript écrits")

# Écrire dans quizzes_algo.py
print(f"\n📝 Écriture dans data/quizzes_algo.py...")
with open('data/quizzes_algo.py', 'w', encoding='utf-8') as f:
    f.write('"""\n')
    f.write('Quiz Algorithmique pour Codebog.\n')
    f.write('"""\n\n')
    f.write('ALGO_CHALLENGES = [\n')

    for i, quiz in enumerate(ALL_ALGO):
        # Calculer le jour (jours pairs pour ALGO : 2, 4, 6, ...)
        day = (i + 1) * 2
        f.write(f'# Jour {day} — ALGO\n')
        f.write(repr(quiz) + ',\n\n')

    f.write(']\n')

print(f"   ✓ {len(ALL_ALGO)} quizzes Algorithmiques écrits")

print(f"\n{'='*70}")
print(f"🎉 INTÉGRATION TERMINÉE !")
print(f"{'='*70}")
print(f"\n📊 Récapitulatif final :")
print(f"   JS   : {len(ALL_JS)} quizzes (jours impairs)")
print(f"   ALGO : {len(ALL_ALGO)} quizzes (jours pairs)")
print(f"   TOTAL: {len(ALL_JS) + len(ALL_ALGO)} quizzes")
print(f"\n💡 Prochaine étape : python codebog.py --day 1 --preview")
print(f"{'='*70}\n")
