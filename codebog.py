#!/usr/bin/env python3
"""
Codebog Post Generator v4 - Architecture Modulaire

Génère des posts quotidiens JavaScript et Algorithmique pour les réseaux sociaux.
Refactorisé pour supporter 365 jours de contenu de manière maintenable.

Usage:
    python codebog.py              # Génère le post du jour
    python codebog.py --day 42     # Génère le post du jour 42
    python codebog.py --all        # Génère tous les posts (1-365)
"""
import argparse
import os
from datetime import date, timedelta

# Imports locaux (nouvelle architecture)
from config import OUTPUT_DIR
from data import build_schedule
from generators import generate_image, generate_post_text


def main():
    """Point d'entrée principal."""
    parser = argparse.ArgumentParser(description='Génère des posts Codebog')
    parser.add_argument('--day', type=int, help='Jour spécifique (1-365)')
    parser.add_argument('--all', action='store_true', help='Générer tous les posts')
    parser.add_argument('--output', default=OUTPUT_DIR, help='Dossier de sortie')
    args = parser.parse_args()

    # Créer le dossier de sortie
    os.makedirs(args.output, exist_ok=True)

    # Construire le calendrier
    schedule = build_schedule()

    if args.all:
        print(f"Génération de {len(schedule)} posts...")
        for post in schedule:
            generate_post(post, args.output)
        print(f"✓ {len(schedule)} posts générés dans {args.output}/")

    elif args.day:
        if args.day < 1 or args.day > len(schedule):
            print(f"Erreur : le jour doit être entre 1 et {len(schedule)}")
            return
        post = schedule[args.day - 1]
        generate_post(post, args.output)
        print(f"✓ Post jour #{args.day} généré")

    else:
        # Par défaut : post du jour
        today = date.today()
        for post in schedule:
            if post['date'] == today.strftime("%Y-%m-%d"):
                generate_post(post, args.output)
                print(f"✓ Post du jour (#{post['day']}) généré")
                return

        print(f"Aucun post prévu pour aujourd'hui ({today})")
        print("Utilise --day N pour générer un post spécifique")


def generate_post(post, output_dir):
    """
    Génère l'image et le texte pour un post.

    Args:
        post: Dictionnaire avec les données du post
        output_dir: Dossier de sortie
    """
    day = post['day']
    type_label = post['type'].lower()

    # Nom des fichiers
    img_path = os.path.join(output_dir, f"day_{day:03d}_{type_label}.png")
    txt_path = os.path.join(output_dir, f"day_{day:03d}_{type_label}.txt")

    # Générer l'image
    generate_image(post, img_path)

    # Générer le texte
    text = generate_post_text(
        (post['type'], post['topic'], post['hook'], post['code'],
         list(post['options'].values()), list(post['options'].keys()).index(post['correct_emoji']),
         post['answer'], post['explanation'], post['tip']),
        day
    )

    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"  [{day:03d}] {post['type']} · {post['topic']}")


def show_stats():
    """Affiche les statistiques du calendrier."""
    schedule = build_schedule()
    js_count = sum(1 for p in schedule if p['type'] == 'JS')
    algo_count = sum(1 for p in schedule if p['type'] == 'ALGO')

    print(f"📊 Statistiques Codebog")
    print(f"   Total posts    : {len(schedule)}")
    print(f"   Posts JS       : {js_count}")
    print(f"   Posts ALGO     : {algo_count}")
    print(f"   Phases         : 4 (90 jours chacune)")
    print(f"   Date début     : {schedule[0]['date']}")
    print(f"   Date fin       : {schedule[-1]['date']}")


if __name__ == "__main__":
    main()
