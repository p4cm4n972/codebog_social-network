#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de validation des quizzes Codebog.
Détecte les anomalies potentielles.
"""
import sys

# Forcer l'encodage UTF-8 pour Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from data.quizzes_js import JS_CHALLENGES
from data.quizzes_algo import ALGO_CHALLENGES

print("=" * 70)
print(" VALIDATION DES QUIZZES CODEBOG")
print("=" * 70)

anomalies = []

def validate_quiz(quiz, index, quiz_type):
    """Valide un quiz et retourne les anomalies trouvées."""
    errors = []

    # 1. Vérifier le nombre d'éléments
    if len(quiz) != 9:
        errors.append(f"❌ {quiz_type} #{index+1}: {len(quiz)} éléments au lieu de 9")
        return errors  # Skip other checks si structure invalide

    type_label, topic, hook, code, options, correct_idx, answer, explanation, tip = quiz

    # 2. Vérifier le type
    if type_label != quiz_type:
        errors.append(f"❌ {quiz_type} #{index+1}: Type '{type_label}' incorrect (devrait être '{quiz_type}')")

    # 3. Vérifier topic non vide
    if not topic or not topic.strip():
        errors.append(f"❌ {quiz_type} #{index+1}: Topic vide")

    # 4. Vérifier hook non vide
    if not hook or not hook.strip():
        errors.append(f"❌ {quiz_type} #{index+1} ({topic}): Hook vide")

    # 5. Vérifier code non vide
    if not code or not code.strip():
        errors.append(f"❌ {quiz_type} #{index+1} ({topic}): Code vide")

    # 6. Vérifier options
    if not isinstance(options, (list, tuple)) or len(options) != 4:
        errors.append(f"❌ {quiz_type} #{index+1} ({topic}): {len(options)} options au lieu de 4")
    else:
        for i, opt in enumerate(options):
            if not opt or (isinstance(opt, str) and not opt.strip()):
                errors.append(f"❌ {quiz_type} #{index+1} ({topic}): Option {i+1} vide")

    # 7. Vérifier index correct
    if not isinstance(correct_idx, int) or correct_idx < 0 or correct_idx > 3:
        errors.append(f"❌ {quiz_type} #{index+1} ({topic}): Index '{correct_idx}' invalide (doit être 0-3)")

    # 8. Vérifier answer non vide
    if not answer or not answer.strip():
        errors.append(f"❌ {quiz_type} #{index+1} ({topic}): Answer vide")

    # 9. Vérifier explanation non vide
    if not explanation or not explanation.strip():
        errors.append(f"❌ {quiz_type} #{index+1} ({topic}): Explanation vide")

    # 10. Vérifier tip non vide
    if not tip or not tip.strip():
        errors.append(f"❌ {quiz_type} #{index+1} ({topic}): Tip vide")

    # 11. Vérifier longueurs raisonnables
    if len(topic) > 100:
        errors.append(f"⚠️  {quiz_type} #{index+1}: Topic très long ({len(topic)} chars)")

    if len(hook) > 200:
        errors.append(f"⚠️  {quiz_type} #{index+1} ({topic}): Hook très long ({len(hook)} chars)")

    if len(code) > 500:
        errors.append(f"⚠️  {quiz_type} #{index+1} ({topic}): Code très long ({len(code)} chars)")

    if len(explanation) > 500:
        errors.append(f"⚠️  {quiz_type} #{index+1} ({topic}): Explanation très longue ({len(explanation)} chars)")

    if len(tip) > 200:
        errors.append(f"⚠️  {quiz_type} #{index+1} ({topic}): Tip très long ({len(tip)} chars)")

    return errors

# Valider JS
print(f"\n🔍 Validation de {len(JS_CHALLENGES)} quizzes JavaScript...")
for i, quiz in enumerate(JS_CHALLENGES):
    errors = validate_quiz(quiz, i, 'JS')
    anomalies.extend(errors)

# Valider ALGO
print(f"🔍 Validation de {len(ALGO_CHALLENGES)} quizzes Algorithmiques...")
for i, quiz in enumerate(ALGO_CHALLENGES):
    errors = validate_quiz(quiz, i, 'ALGO')
    anomalies.extend(errors)

# Afficher les résultats
print(f"\n{'='*70}")
if anomalies:
    print(f"⚠️  {len(anomalies)} anomalie(s) détectée(s) :\n")
    for anomaly in anomalies:
        print(f"   {anomaly}")
else:
    print(f"✅ AUCUNE ANOMALIE DÉTECTÉE !")
    print(f"\n📊 Tous les {len(JS_CHALLENGES) + len(ALGO_CHALLENGES)} quizzes sont valides:")
    print(f"   • {len(JS_CHALLENGES)} quizzes JavaScript")
    print(f"   • {len(ALGO_CHALLENGES)} quizzes Algorithmiques")

print(f"{'='*70}\n")
