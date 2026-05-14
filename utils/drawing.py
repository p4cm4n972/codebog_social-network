"""
Fonctions de dessin pour les éléments graphiques des posts.
"""


def draw_down_arrow(draw, cx, cy, r, color):
    """
    Dessine une flèche bas premium dans un cercle.

    Args:
        draw: ImageDraw instance
        cx: Centre X
        cy: Centre Y
        r: Rayon du cercle
        color: Couleur RGB tuple
    """
    # Cercle
    draw.ellipse(
        [cx-r, cy-r, cx+r, cy+r],
        outline=color,
        width=3
    )

    # Tige verticale
    draw.line(
        [(cx, cy-r//3), (cx, cy+r//6)],
        fill=color,
        width=4
    )

    # Pointe gauche
    draw.line(
        [(cx-10, cy+2), (cx, cy+r//3)],
        fill=color,
        width=4
    )

    # Pointe droite
    draw.line(
        [(cx+10, cy+2), (cx, cy+r//3)],
        fill=color,
        width=4
    )


def draw_hook_two_color(draw, hook, x, y_start, font_w, font_g, accent, base, max_w):
    """
    Rend le hook sur plusieurs lignes avec 2 couleurs :
    - Ligne 1        : couleur base (blanc)
    - Début ligne 2  : couleur accent (vert/bleu)
    - Suite ligne 2+ : couleur base

    Args:
        draw: ImageDraw instance
        hook: Texte du hook
        x: Position X de départ
        y_start: Position Y de départ
        font_w: Police normale (blanc)
        font_g: Police accentuée (bold)
        accent: Couleur d'accent RGB tuple
        base: Couleur de base RGB tuple
        max_w: Largeur max avant retour à la ligne

    Returns:
        Position Y après le hook
    """
    words  = hook.split()
    n      = len(words)
    # Zone accent : du tiers au deux-tiers
    acc_s  = max(1, n // 3)
    acc_e  = max(acc_s + 1, (2 * n) // 3)

    # Construction des lignes avec wrapping manuel
    lines, current = [], []
    for i, w in enumerate(words):
        current.append((i, w))
        test = ' '.join(wd for _, wd in current)
        if draw.textbbox((0,0), test, font=font_w)[2] > max_w and len(current) > 1:
            lines.append(current[:-1])
            current = [(i, w)]
    if current:
        lines.append(current)

    # Calculer la ligne de base de référence (la plus grande police)
    baseline_offset = draw.textbbox((0,0), 'Ag', font=font_g)[3]

    y = y_start
    for li, line in enumerate(lines):
        cx = x
        # Position de la baseline pour cette ligne
        baseline_y = y + baseline_offset

        for wi_abs, (word_idx, word) in enumerate(line):
            in_accent = (acc_s <= word_idx < acc_e)
            font  = font_g if in_accent else font_w
            color = accent if in_accent else base

            # Aligner sur la baseline en utilisant anchor="ls" (left-baseline)
            draw.text((cx, baseline_y), word, font=font, fill=color, anchor="ls")
            space = word + ' '
            cx += draw.textbbox((0,0), space, font=font)[2]

        # Hauteur de ligne = max des deux fonts
        lh = max(
            draw.textbbox((0,0), 'Ag', font=font_w)[3],
            draw.textbbox((0,0), 'Ag', font=font_g)[3]
        )
        y += int(lh * 1.12)
    return y   # y après le hook
