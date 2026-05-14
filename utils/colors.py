"""
Coloration syntaxique pour le code JavaScript.
"""
import re


def colorize_token(draw, x, y, token, font):
    """
    Rend un token JS avec sa couleur syntaxique, retourne le nouveau x.

    Args:
        draw: ImageDraw instance
        x: Position X
        y: Position Y
        token: Token à coloriser
        font: Police à utiliser

    Returns:
        Nouvelle position X après le token
    """
    # Mots-clés JavaScript
    KW  = {'function','return','const','let','var','if','else','for','while','do',
           'true','false','null','undefined','new','class','extends','super','this',
           'async','await','typeof','instanceof','throw','try','catch','finally',
           'yield','static','of','in','switch','case','break','continue','from',
           'import','export','default','get','set','delete','void'}

    # Classes built-in
    CLS = {'console','Math','Object','Array','Promise','JSON','Number','String',
           'Boolean','Symbol','Map','Set','WeakMap','WeakSet','Error','Date'}

    t = token.strip()
    if not t:
        x += draw.textbbox((0,0), token, font=font)[2]
        return x

    # Déterminer la couleur
    if t.startswith('//'):
        color = (106, 153, 85)  # Commentaires verts
    elif t.startswith('"') or t.startswith("'") or t.startswith('`'):
        color = (206, 145, 120)  # Strings orange
    elif t in KW:
        color = (197, 134, 192)  # Mots-clés violets
    elif t in CLS:
        color = (78, 201, 176)   # Classes teal
    elif t.lstrip('-').replace('.','').isdigit():
        color = (181, 206, 168)  # Nombres verts clairs
    else:
        color = (212, 212, 220)  # Défaut blanc cassé

    draw.text((x, y), token, font=font, fill=color)
    x += draw.textbbox((0,0), token, font=font)[2]
    return x


def draw_code_line(draw, x_start, y, line, font):
    """
    Dessine une ligne de code avec coloration syntaxique.

    Args:
        draw: ImageDraw instance
        x_start: Position X de départ
        y: Position Y
        line: Ligne de code à dessiner
        font: Police à utiliser
    """
    # Pattern pour tokeniser le code
    pat = r'(//[^\n]*|"[^"]*"|\'[^\']*\'|`[^`]*`|\b\w+\b|[^\w\s]|\s+)'
    for tok in re.findall(pat, line):
        x_start = colorize_token(draw, x_start, y, tok, font)
