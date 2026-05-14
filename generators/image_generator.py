"""
Génération d'images pour les posts Codebog.

NOTE: Cette version utilise temporairement l'ancienne fonction.
TODO: Migrer complètement generate_image() ici avec les nouveaux imports.
"""
from PIL import Image, ImageDraw
from config import *
from utils.fonts import load_font
from utils.colors import draw_code_line
from utils.emojis import emoji_img
from utils.drawing import draw_hook_two_color, draw_down_arrow


def generate_image(post, output_path):
    """
    Génère l'image 1080x1080 du post avec le nouveau layout.

    Pour maintenant, wrapper vers l'ancienne implémentation.
    """
    # Import temporaire de l'ancienne fonction
    import codebog_generator
    return codebog_generator.generate_image(post, output_path)


# TODO: Copier la vraie implémentation de generate_image() ici
# en utilisant les imports ci-dessus au lieu des fonctions locales
