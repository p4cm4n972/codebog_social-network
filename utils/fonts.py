"""
Gestion du chargement des polices avec fallbacks multi-plateformes.
"""
from PIL import ImageFont


def load_font(name, size):
    """
    Charge une font avec priorité :
    1. Dossier courant (si DejaVu téléchargées)
    2. Fonts Windows système (toujours disponibles)
    3. Fonts Linux

    Args:
        name: Nom du fichier de police (ex: "DejaVuSans.ttf")
        size: Taille en pixels

    Returns:
        ImageFont instance
    """
    W = "C:/Windows/Fonts/"
    WIN_MAP = {
        "DejaVuSansMono.ttf":      [W+"consola.ttf",  W+"lucon.ttf",   W+"cour.ttf"],
        "DejaVuSansMono-Bold.ttf": [W+"consolab.ttf", W+"courbd.ttf"],
        "DejaVuSans.ttf":          [W+"segoeui.ttf",  W+"arial.ttf",   W+"calibri.ttf"],
        "DejaVuSans-Bold.ttf":     [W+"segoeuib.ttf", W+"arialbd.ttf", W+"calibrib.ttf"],
        "seguiemj.ttf":            [W+"seguiemj.ttf"],
    }
    LIN = "/usr/share/fonts/truetype/dejavu/"
    LIN_MAP = {
        "DejaVuSansMono.ttf":      [LIN+"DejaVuSansMono.ttf"],
        "DejaVuSansMono-Bold.ttf": [LIN+"DejaVuSansMono-Bold.ttf"],
        "DejaVuSans.ttf":          [LIN+"DejaVuSans.ttf"],
        "DejaVuSans-Bold.ttf":     [LIN+"DejaVuSans-Bold.ttf"],
        "seguiemj.ttf":            [LIN+"DejaVuSans.ttf"],
    }
    candidates = [name] + WIN_MAP.get(name, []) + LIN_MAP.get(name, [])
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            pass
    return ImageFont.load_default()
