"""
Générateurs d'images et de texte pour les posts Codebog.
"""
from .image_generator import generate_image
from .text_generator import generate_post_text

__all__ = ['generate_image', 'generate_post_text']
