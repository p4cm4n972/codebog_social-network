"""
Génération du calendrier des 365 posts Codebog.
"""
from datetime import timedelta
from config import START_DATE, END_DATE, EMOJI_ORDER
from .quizzes_js import JS_CHALLENGES
from .quizzes_algo import ALGO_CHALLENGES


def build_schedule():
    """Construit le calendrier complet des posts (max 365 jours)."""
    schedule = []
    current = START_DATE
    day = 1
    js_idx = 0
    algo_idx = 0

    while current <= END_DATE and day <= 365:
        if day % 2 == 1:  # impair → JS
            topic = JS_CHALLENGES[js_idx % len(JS_CHALLENGES)]
            js_idx += 1
        else:              # pair → ALGO
            topic = ALGO_CHALLENGES[algo_idx % len(ALGO_CHALLENGES)]
            algo_idx += 1

        # Phases : 1-90, 91-180, 181-270, 271-365
        if day <= 90:
            phase = 1
        elif day <= 180:
            phase = 2
        elif day <= 270:
            phase = 3
        else:
            phase = 4

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
