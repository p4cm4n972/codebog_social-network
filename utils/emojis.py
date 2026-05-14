"""
Gestion des emojis embarqués pour les posts Codebog.
"""
import base64
import io
from PIL import Image
from config import EMOJI_B64


def emoji_img(name, size=80):
    """
    Retourne un emoji PIL Image depuis le b64 embarqué.

    Args:
        name: Nom de l'emoji ('heart', 'astonished', 'joy', 'fire')
        size: Taille en pixels (défaut: 80)

    Returns:
        PIL.Image en mode RGBA
    """
    data = base64.b64decode(EMOJI_B64[name])
    img  = Image.open(io.BytesIO(data)).convert("RGBA")
    return img.resize((size, size), Image.LANCZOS)
