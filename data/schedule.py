"""
Génération du calendrier des 365 posts Codebog.
"""
from datetime import timedelta
from config import START_DATE, END_DATE, EMOJI_ORDER
from .quizzes_js import JS_CHALLENGES
from .quizzes_algo import ALGO_CHALLENGES


def build_schedule(ignore_end_date=False):
    """Construit le calendrier complet des posts (365 jours + bonus).

    Args:
        ignore_end_date: Si True, génère tous les quiz disponibles sans limite de date
    """
    schedule = []
    current = START_DATE
    day = 1
    js_idx = 0
    algo_idx = 0

    # Calculer le maximum de jours possibles basé sur les quiz disponibles
    # Jours impairs = JS, pairs = ALGO pour les 365 premiers jours
    # Jours 366+ = quiz extras disponibles (bonus)
    max_js_days = len(JS_CHALLENGES)  # 184 JS
    max_algo_days = len(ALGO_CHALLENGES)  # 182 ALGO
    # Pour 365 jours: besoin de 183 JS (impairs) + 182 ALGO (pairs)
    # Extras: 184 - 183 = 1 JS extra → 1 jour bonus possible
    js_extras = max(0, max_js_days - 183)
    algo_extras = max(0, max_algo_days - 182)
    max_days = 365 + js_extras + algo_extras

    while day <= max_days and (ignore_end_date or current <= END_DATE):
        # Pour les jours > 365 (bonus), on utilise les quiz extras disponibles
        if day > 365:
            # Vérifier quel type de quiz on a encore en extra
            if js_idx < len(JS_CHALLENGES):
                topic = JS_CHALLENGES[js_idx]
                js_idx += 1
                topic_type = 'JS'
            elif algo_idx < len(ALGO_CHALLENGES):
                topic = ALGO_CHALLENGES[algo_idx]
                algo_idx += 1
                topic_type = 'ALGO'
            else:
                break  # Plus de quiz disponibles
        else:
            # Alternance normale pour les jours 1-365
            if day % 2 == 1:  # impair → JS
                topic = JS_CHALLENGES[js_idx % len(JS_CHALLENGES)]
                js_idx += 1
            else:              # pair → ALGO
                topic = ALGO_CHALLENGES[algo_idx % len(ALGO_CHALLENGES)]
                algo_idx += 1

        # Phases : 1-90, 91-180, 181-270, 271-365, 366+ (bonus)
        if day <= 90:
            phase = 1
        elif day <= 180:
            phase = 2
        elif day <= 270:
            phase = 3
        elif day <= 365:
            phase = 4
        else:
            phase = 5  # Phase bonus

        schedule.append({
            "day": day,
            "date": current.strftime("%Y-%m-%d"),
            "day_name": ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"][current.weekday()],
            "type": topic[0],
            "phase": phase,
            "topic": topic[1],
            "hook": topic[2],
            "code": topic[3],
            "options": {EMOJI_ORDER[i]: topic[4][i] for i in range(4)},
            "correct_emoji": EMOJI_ORDER[topic[5]],
            "answer": topic[6],
            "explanation": topic[7],
            "tip": topic[8],
        })

        current += timedelta(days=1)
        day += 1

    return schedule
