"""
Module de données pour les quiz Codebog.
"""
from .quizzes_js import JS_CHALLENGES
from .quizzes_algo import ALGO_CHALLENGES
from .schedule import build_schedule

__all__ = ['JS_CHALLENGES', 'ALGO_CHALLENGES', 'build_schedule']
