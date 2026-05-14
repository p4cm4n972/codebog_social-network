"""
Génération du texte pour les posts sociaux.
"""
from config import EMOJI_ORDER


def generate_post_text(topic, day):
    """
    Génère le texte complet du post Facebook.

    Args:
        topic: Tuple du quiz (type, titre, hook, code, options, correct_idx, answer, explanation, tip)
        day: Numéro du jour

    Returns:
        Texte formaté du post
    """
    type_label = "JS" if topic[0] == "JS" else "ALGO"
    emojis_str = " · ".join([f"{EMOJI_ORDER[i]} {topic[4][i]}" for i in range(4)])

    return f"""🖥️ #{day:03d} — {type_label} · {topic[1]}

{topic[2]}

```
{topic[3]}
```

{emojis_str}

⏱️ Tu as 10 secondes. Réponds avec une réaction.

👉 La réponse est en commentaire."""
