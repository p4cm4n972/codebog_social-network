#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║         CODEBOG POST GENERATOR v1.0                  ║
║  241 posts Facebook · 5 mai → 31 décembre 2026       ║
║  121 JS (jours impairs) + 120 Algo (jours pairs)     ║
╚══════════════════════════════════════════════════════╝

Usage:
  python codebog_generator.py               # génère tous les posts
  python codebog_generator.py --day 1       # génère le post #1
  python codebog_generator.py --range 1 7   # génère les posts 1 à 7
  python codebog_generator.py --json        # exporte posts.json
"""

import os
import sys
import json
import textwrap
import argparse
from datetime import date, timedelta
from PIL import Image, ImageDraw, ImageFont

import base64, io as _io

EMOJI_B64 = {
    "heart": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAACyElEQVR4nO2d23HbMBBFbzTuwSnIKcCVpoCkoKQK5SdMNBBBLsB9Qvd8yha4uIdLkJiRBBBCCCGEEEIIIYS48cVq4Pv7x11UwO+fZjVIiK5TdVDpZHp4ychUp8pAVyfUYiUiY52XBtCeUIuWiMx13mbfaD0prWNkr3NKgMekNI5Voc7h1pk60K8fn7uvf/32XTrEaJt7hv/IaJ22k+oF3yIUIZ1cVPgbIxLE/zg0KWnwLQIRZ5OLDn9DKkG0BriEL3zvUS1ZwgfktZwKyDSpjb2aqtTZMn0busuVs19zjEIcCsh4Vm081lalzj10O4AM0xWQ+azauL9/3KvU2fubbgcMPFiZjlGIXQEVzqpq9DLVXwOunMEvdvYDwJvJqFuQylsRK/L0uGxy+VHYjFuFdovCpgNaXjBoKXwOCIYCgqGAYCggmH8rMh++fNnuhm7tC8Sex6xvvT8QG9qMuQYEQwHBPAngZciOvWzZAcFQQDC7AngZ0qeXKTsgmK4AdoEeR1myA4I5FMAuuM5ZhuyAYE4FsAvmkWQn6gBKGEf18wEjA5KxrIbWAEo4ZzSj4UWYEvrMZDN1F0QJz8xmMn0bSgn/uZJFia8CyEr4d0W0vIqIdN+W0rKqCIvLrslWxIrrg9WczPaCVpRggelm3CoSLOdhvhtaXYJ1/dyOPsDj5HERULELvGp264BKEjxrdb0EVZLghfsakF2Cd30hi3BWCRF18S7oL1EnRZiATF0QWUtoB2SSEEX4JShaQvTxwwUAcSFEhw8kEQD4h5EhfCCRAE+yhA8kE+ARTKbwgWQCgHwBWZNOAGD4ey0J5aYUAOiHlTF8ILEAQC+0rOEDyQVokDl8oICA7AFeJb0AYF5CBXklBAATv81SIHygkABAHmqV8IFiAoDzcCuFDxQUcES18IGiAioG3aOkAOBZwkpSSrHqZxEIIYSszx+Tjihez5QCQwAAAABJRU5ErkJggg==",
    "astonished": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAEnUlEQVR4nO1dOVJcMRBtKJcTnHIFJ06nyonxUSalfAdfxKmPYghJnfgKpJCQ4EgzGo2WVqs3/dHLYP6XWu+pW8vXArBgiitrA7B4eYT33nc+ffNfPpcGUsjGwpsoLozBEH5ze9ed7uvzQ/MZa0FMMy8RTyEbi5IoVkKoZ2pBegkexFDLKEe8Bekl5MTQEEJFgJR8T8SnSIWQFkE08ZmIT6ElhJgAMfkzEZ8iFkJCBPYEt0J8CikhrrkSAtgu+QCn5eEcKLIJsGXyAyREYHGlYExK/P7+rfre718fObIfBsXOEJJGw9GwACn5rcKUoC0Gh50cIgwJEJNPLVAKaSG47RwVgSxAIP/Hz6/FZ1pk1sjgFmIkr9a7IyKQBKiRTyUuV0guETjTLqVFFeFDrwGnMf9ozChZ4X2uENHKZ/T91M6b2zt4fX6Al0d47xGhS61Sb2fhiF5PQI8DJL9SbRFYvroHYqv219HLD0qAFXr6EHjCeEFTgEU+DVgRuntBJHz+U//933cVM87gwK5qSz1c+1sFTKElhKJdrV5RUYCh2c3eAqaQEsLArtZ3hGYboE4+VxoSaRLSaPGXFYDc5+ckboNp5XjNhiBS7EcYttvtTv5+enpqpzsajpzYVWoLVHpBaQHT/6MKLAAPdp2FIO7aXyok+pmR8OHIrtK4gPWjfApMISnPjsKTXScCkBpfiR4LRx5e7YJTnrMewDHtQKk5Gl5gaVeOV9EQtNDGEsAYBwHWrKcO0t7Q8gBjiAlAGcRoDHy82TUugMYUMiUPr3YlEA1BPTVHczrCk11XAEwN8MCwv1pIwck4S7vC5JzKZFwoCGnWURAe7OLzAAD+4T9XHHdoV/AA3jaAs+G7hLRAohHmMFCiB+PULpk2IBjqbVWEQ7tkG2FsgbXXBTmyS2dhltXCqxYc2LXmgoyxBDCGTghixCxbX7GYRgDs1qXw3CxCuBeAumdsFiGuAY6rtTBnrGmCY8Oe9KY/CuJVcm49oLo390t+FnP/Nz+Jtr9/c+sJh3WKnr4Jl8gvEX/2fkEILyLEHuBOgOxGaCTxZ2llhPAgQiyAq3EAJ/mld721CQcBrBtibvJraViKkC5Td+UBMTjIl0iLGy4EsKiRXkJRVgDr8YBEjfXgBTleTwSwPsj6UhDzbB6CLEOBhzB0JoB1b0gyVFiGodImPXMPuHRUBbBujLeCGo9ZAVZjLAPSUQXLC8bQ4q8owPICXpT4rHqAdY9odmAO8HPXCyrN5XtPm4qmANJeYDk/L5k39vhKlAesUNSHnrNDu0OQhggSoUIr/PTygxZAsldkEYak82Q/OTdOdDYv0K79PZW1OwRJiZCrkRzEaX2Yp56eTuqGziKCd/IBGG/Q4MRM64LMbtAI0BYBoH9lHIBP8gGEb1Eahed7adzcohQgdY/YqAjc5HPfqMfat5e8zK1XCMlaD8A3LpruLkmrHTJSd0mu21QbmO421RjrPuE21o3aCTZ1o3aMdad8HurffUun81qIUZpK0fwebvrh3UIMD6THcLHyAXNmNUUUzGSh9eoPFwKkkLy1z5rwFK6MqYEiijeyc/gP166ChkA7XfoAAAAASUVORK5CYII=",
    "joy": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAEcUlEQVR4nO2dv24UMRDG5yJECtLyBogGiYoyIFHxFulOPEGegg7RoHR5i1RIkJKWBt0b0IYCmlAEJ16f7Z1/3vF551cll9zu+Ptsr9fr9QA4pmysA8Bycw231O+cnPZfvi4D5IiNpTdTuggGI/iTp6/Jx/3969vs/1gbYnrykvAcsbGUTLEyYvGTWoheogczFjtRTngL0UvkzFjCiEUMSMXvSfiU1IjWJjQ9+CEJn7KUEc0MiMU/JOFTYiNamKB+wFGET2llxJHWgQDGFR9gWh7NG0U1A0YWP9DCBJWmFIIZVfgcoUuSdkfiFrBG8QEeyittCSID1ip+QMMEtgFrFz8gNYFlgIs/RWIC2QAXPw/XBJIBLn4djgloA1o+pRoRrF7kLshrfx2qPigDvOuhQemKZg1w8XlgTVCdjHPoVA3w2i8D0woelf6gOeo5e/+3+vfLz4+1TkViybhuruE2N3FXnMmT1v65wpVobYZFXLWZ02wXJK393EJKv9vy2Bpx5XStXgM4tV8j0BYmWMZV0zHbBXG7n1qApSbM+Q6VHuIqdUN7BmiKTw1U4xgtjqkVV84ElfsArQBz39Hut3uIK2ZigNbQU1JrW46Ceokr1jnbAijdT1oTNAJNj8GpbT3GldPVpyKMKd4JY9juruD4/O7nPx/easRzMByffwEAgO0O4OLZO/Zx7q/G1NHPdne195kkkENCWvZ4NMTqgnIB1D4fCe2y+zXAGDfAGDfAmCMAf/CyNPGDGlYLKF3x1zAK0i47uwtKT7gG8QOaZd8AeBdkQbgX8IuwMW6AMeK5oMCargEAemVnt4D01nsN0xABzbL7XBARnwsaDDfAGDfAGJ+KINJkKiKsU8HssVY64RrED0jLHj8RYz+SdPiIH0k6ergBxrSfinj+VXKKPvj5Zu8j9akI6oXYpyLKv9dIF+j6VAQRn4oYjKwBlPsBB09O18lF+OQUNtgl6ula0MsXr/7/9HL6j58IEfbKx4cyXcDdYtizH98n/xLWimJQf0HD4bNnAGY0tKZpByxzmpTeEVNrAWmTHBnNslYNqLUCq7fbe2ROi5qOWQO4e2GuoRVIyoh+Uz7GW0EdSe0HqBjgrWAf7doPgNi6GPOcIPs+7v19wRjkxMfW/lplVhkFZV9kHqglcMTHMmsAdpZ0VBO44mM390b389hHlqWXlw+tSypVHk3xARgGAPBNAOjfiFqrpYgPoGwAAO3B/ex2YJ0ZMdddYvt8al4B8lCTunqidyO0hAfgJXVgjfW1TYhpbQhlYNBafABBChPOOiL2hnlMU7ijMOoQU5LORJT/pMXWZpZobkWGRZzEx2p7Sy1abUeJpassSkuZoXEXq5VFSS0jXMs8Yj1tAqudUU81leHoydxapDNUfSgfBzXa0pZWuSQ9m+oMB5dNNcbzCc/jGbUThsqoHeM55fMsZkCgtPTRwozSQGEJ4QOLGxBjYUYPoseYGhDALAjmmIIZClsJH+jCgJSWWfusBU/pKpgaHFN6EzvHP858bTstmHbXAAAAAElFTkSuQmCC",
    "fire": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAADSUlEQVR4nO1dW07DQBDbIC6GxBm4Ax+cph/cgTMgcTT4WqlUabPztKcdf0JJHHs8swlLGKPRsOD3Y/yiOVjwhCZgwRS/sgllDbgUvaoJG5qAFCtCb6c611UqAatVXikNZQyQilrFhBIGaMWsYAK9AVYR2U2gHVYRwjEOZ8oERFUtYxroDIgWic0EKgOyxGEygcaAbFFYTIAPJQYhkMMZmgAG8cfA8oAZwCL+BIoPxADXi/16dTsUwoR0A0LEL2xC2vBxv7A90d++XU+RMZxTEpAi/q2vK5GRhnAD0sRf/b4Q0SaEGpAuvvRzBKC5Ez6EVNQigznMAIqlZoEk8CfAKqKTCVEpCFlmuZD1rl6HJWrEspQzARGtw+GYESlwN8BMMrJvE84ErgRkCGQ8h3cKXA0wkcusTqIkcCQAIYjhnJ4pcDNATQpZjQRJwCaAQAAtB68UuBigIsMg/gSQC8cMKAqPFJgNKF/9EyBOnQAjrCkwGcC2s6Ei8hPA2H4mACsitQFd/T7oGeAEbUGqDCh517uKZI6dAEdoClNsQPd+X+QloEL7mUh8UioyoKvfHz0DwMgxoFL7mUji/Cz58HYaG7wN/RxsL3nBmi3duiIyAIIjwY8+DzbkCOKNRuIEaKMsFf4IWiOEG7qkCeAcwt7iRx3TAeIWFDoHokWaxw9qS5qti7EJkLSfzAqVnCt4NcTRghDtgaQlxRqwMsCQQqyc2/kP/y6hMsBtmzZDFTpx0GoS34KCKygUCdxxM4Ch+ieAXHIMqJiCJM6YBDBV/wSIk9oA8dCplILgxw/n4LgPeGCYlpOqRxLvljMm4FP+I52AwjAZwPgi1GxYNegEgNEGgNEGgGE24JHngMe1dwLAyDdAsc5OA4CbiwGP2Ia8rtltX9AkBN+4FQzvYnNvQUsEGdvQAqcyL2y6x5YUdU3hQt1sSSwP5m5Uf3Qxha+CKqfhbl5dfPVCGGbBFQ5ZhZNenbstCdWKdsTPTmz6jdjuBSKSQCD+GKBHEXATSMQfA/xPfK6ukKJaErjf754bdeJzpMwFoqr/xwFNYCIsDYRVfw4KEhNLz5GODAE9UtCChsg5wt5UTiT8BOUvZCKEYhS/0Wg0Go1Go9EA4Q+wHjBiPwl2BAAAAABJRU5ErkJggg==",
}

EMOJI_ORDER = ["heart", "astonished", "joy", "fire"]

def _emoji_img(name, size=80):
    """Retourne un emoji PIL Image depuis le b64 embarqué."""
    data = base64.b64decode(EMOJI_B64[name])
    img  = Image.open(_io.BytesIO(data)).convert("RGBA")
    return img.resize((size, size), Image.LANCZOS)

def _draw_down_arrow(draw, cx, cy, r, color):
    """Dessine une flèche bas premium dans un cercle."""

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



# ─────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────
START_DATE = date(2026, 5, 5)
END_DATE   = date(2026, 12, 31)
OUTPUT_DIR = "posts_output"
IMG_W, IMG_H = 1080, 1080

BG       = (11, 11, 12)
TITLEBAR = (28, 28, 30)
CODEBG   = (18, 18, 20)
GREEN    = (34, 197, 94)
YELLOW   = (254, 188, 46)
BLUE     = (86, 156, 214)
RED      = (255, 95, 87)
WHITE    = (240, 240, 240)
GRAY     = (100, 100, 105)
DIMGRAY  = (60, 60, 65)
TEAL     = (78, 201, 176)
PURPLE   = (197, 134, 192)


# ─────────────────────────────────────────
# SOCIAL OPTIMIZATION
# ─────────────────────────────────────────
HOOKS = [
    "90% des devs se trompent ici.",
    "Question niveau entretien technique.",
    "La plupart répondent faux en moins de 5 secondes.",
    "Tu maîtrises vraiment JavaScript ?",
]

CTA = {
    "JS": "💻 Besoin de t'entraîner en JavaScript ? → codebog.itmade.fr",
    "ALGO": "🧠 Tu veux progresser en algorithmique ? → learning.itmade.fr"
}

BADGES = {
    "JS": "⚡ JS CHALLENGE",
    "ALGO": "🧠 ALGO CHALLENGE"
}

HASHTAGS = {
    "JS": "#javascript #webdev #frontend #coding #developer",
    "ALGO": "#algorithms #codingchallenge #programming #developer"
}

# ─────────────────────────────────────────
# TOPICS — 241 entrées
# Format: (type, topic_court, hook, code_snippet, options[4], correct_idx, answer, explication, tip)
# correct_idx: 0=❤️ 1=😮 2=😂 3=🔥
# ─────────────────────────────────────────

EMOJIS = ["❤️", "😮", "😂", "🔥"]

TOPICS = [
# ── PHASE 1 : Bases (jours 1-90) ─────────────────────────────────────
# Jour 1 — JS
("JS", "typeof null",
 "90% des devs JS se trompent sur cette ligne.",
 'console.log(typeof null)',
 ['"null"', '"object"', '"undefined"', '"boolean"'],
 1,
 '"object"',
 'typeof null retourne "object" — un bug historique depuis 1995.\nnull n\'est PAS un objet, mais la spec l\'a encodé ainsi\net personne n\'ose corriger ça pour ne pas casser Internet.',
 'if (x === null) { ... } // ✅ toujours ça'),

# Jour 2 — ALGO
("ALGO", "Big O — O(1) vs O(n)",
 "Laquelle de ces fonctions est O(1) ?",
 'function a(arr) { return arr[0]; }\nfunction b(arr) {\n  let s = 0;\n  for (let x of arr) s += x;\n  return s;\n}',
 ['a() et b()', 'Seulement a()', 'Seulement b()', 'Ni l\'une ni l\'autre'],
 1,
 'Seulement a()',
 'a() accède directement à l\'index 0 → temps constant O(1).\nb() parcourt tout le tableau → O(n) : le temps grandit\navec la taille du tableau.',
 '// O(1) = temps constant quelle que soit la taille'),

# Jour 3 — JS
("JS", "== vs ===",
 "Vrai ou faux ? 0 == false renvoie true.",
 'console.log(0 == false)\nconsole.log(0 === false)',
 ['true / true', 'false / false', 'true / false', 'false / true'],
 2,
 'true / false',
 '== applique la coercition de type : 0 est converti en false.\n=== compare sans conversion : 0 (number) ≠ false (boolean).\nToujours utiliser === sauf raison explicite.',
 '// Règle : toujours ===, jamais =='),

# Jour 4 — ALGO
("ALGO", "Two Sum",
 "Trouve les 2 indices dont la somme vaut target.",
 'function twoSum(nums, target) {\n  // ???\n  // Input:  [2, 7, 11, 15], target=9\n  // Output: [0, 1]\n}',
 ['Boucle double O(n²)', 'HashMap O(n)', 'Sort + two pointers', 'Récursion'],
 1,
 'HashMap O(n)',
 'La solution optimale utilise un HashMap.\nPour chaque nb, on cherche (target - nb) dans la map.\nSi trouvé → on a notre paire. Sinon on stocke nb.',
 'map.set(nums[i], i) // complément → index'),

# Jour 5 — JS
("JS", "var hoisting",
 "Que va afficher ce code ?",
 'console.log(x)\nvar x = 5\nconsole.log(x)',
 ['Error / 5', 'undefined / 5', '5 / 5', 'undefined / undefined'],
 1,
 'undefined / 5',
 'var est "hoisted" (remonté) en haut du scope.\nLa déclaration est levée mais PAS l\'initialisation.\nC\'est comme si le moteur écrivait var x; en premier.',
 '// var → hoisted | let/const → TDZ (erreur)'),

# Jour 6 — ALGO
("ALGO", "Palindrome",
 "Est-ce que cette fonction détecte un palindrome ?",
 'function isPalin(s) {\n  return s === s.split("").reverse().join("")\n}\nconsole.log(isPalin("racecar"))',
 ['false', 'true', 'Error', '"racecar"'],
 1,
 'true',
 '"racecar" inversé = "racecar" → c\'est bien un palindrome.\nCette solution est correcte mais O(n) en mémoire.\nLa solution optimale utilise deux pointeurs O(1) mémoire.',
 'let l=0, r=s.length-1; // two pointers'),

# Jour 7 — JS
("JS", "let/const TDZ",
 "Que se passe-t-il ici ?",
 'console.log(a)\nlet a = 10',
 ['"undefined"', '10', 'ReferenceError', 'null'],
 2,
 'ReferenceError',
 'let et const ont une Temporal Dead Zone (TDZ).\nContrairement à var, ils ne sont pas initialisés\navant leur déclaration → ReferenceError.',
 '// TDZ : la var existe mais est inaccessible'),

# Jour 8 — ALGO
("ALGO", "Anagramme",
 "Ces deux strings sont-elles des anagrammes ?",
 'function isAnagram(s, t) {\n  return s.split("").sort().join("") ===\n         t.split("").sort().join("")\n}\nconsole.log(isAnagram("listen", "silent"))',
 ['false', 'true', 'Error', '"listen"'],
 1,
 'true',
 '"listen" triée = "eilnst"\n"silent" triée = "eilnst"\nMême résultat → anagrammes ✅\nSolution O(n log n). La version HashMap est O(n).',
 '// HashMap : compter les fréquences de chaque lettre'),

# Jour 9 — JS
("JS", "Closure",
 "Qu'affiche ce code ?",
 'function outer() {\n  let count = 0\n  return function() {\n    count++\n    return count\n  }\n}\nconst inc = outer()\nconsole.log(inc(), inc(), inc())',
 ['0, 0, 0', '1, 1, 1', '1, 2, 3', 'Error'],
 2,
 '1, 2, 3',
 'La fonction retournée forme une closure sur count.\nElle garde une référence à la variable count\nde outer(), même après que outer() ait terminé.',
 '// Closure = fonction + son environnement lexical'),

# Jour 10 — ALGO
("ALGO", "Binary Search",
 "Combien d'étapes pour trouver 7 dans ce tableau trié ?",
 'const arr = [1, 3, 5, 7, 9, 11, 13]\n// Binary search pour trouver 7\n// Étape 1: mid = arr[3] = 7 ✓',
 ['7 étapes', '4 étapes', '1 étape', '3 étapes'],
 2,
 '1 étape',
 'Le tableau a 7 éléments. mid = index 3 = valeur 7.\nOn trouve directement → 1 seule étape !\nBinary search : O(log n) au lieu de O(n) pour la search linéaire.',
 '// log2(7) ≈ 2.8 → max 3 étapes dans le pire cas'),

# Jour 11 — JS
("JS", "this — méthode vs fonction",
 "Que va afficher ce code ?",
 'const obj = {\n  name: "Codebog",\n  greet: function() {\n    return this.name\n  }\n}\nconsole.log(obj.greet())',
 ['"Codebog"', 'undefined', 'Error', 'null'],
 0,
 '"Codebog"',
 'Quand greet() est appelée comme méthode d\'obj,\nthis fait référence à obj lui-même.\nDonc this.name = "Codebog" ✅',
 '// this dépend du contexte d\'appel, pas de la définition'),

# Jour 12 — ALGO
("ALGO", "Bubble Sort",
 "Quelle est la complexité de Bubble Sort ?",
 'function bubbleSort(arr) {\n  for (let i = 0; i < arr.length; i++) {\n    for (let j = 0; j < arr.length - i - 1; j++) {\n      if (arr[j] > arr[j+1])\n        [arr[j], arr[j+1]] = [arr[j+1], arr[j]]\n    }\n  }\n  return arr\n}',
 ['O(n)', 'O(n log n)', 'O(n²)', 'O(log n)'],
 2,
 'O(n²)',
 'Deux boucles imbriquées sur n éléments = O(n²).\nC\'est le pire des algos de tri pour les grandes données.\nPréférer merge sort O(n log n) ou quick sort O(n log n).',
 '// Bubble sort : simple à comprendre, lent en pratique'),

# Jour 13 — JS
("JS", "Arrow function et this",
 "Que va afficher ce code ?",
 'const obj = {\n  name: "Codebog",\n  greet: () => {\n    return this.name\n  }\n}\nconsole.log(obj.greet())',
 ['"Codebog"', 'undefined', 'Error', 'null'],
 1,
 'undefined',
 'Les arrow functions n\'ont PAS leur propre this.\nElles héritent du this du contexte englobant.\nIci, le contexte est global → this.name est undefined.',
 '// Arrow fn : this lexical | function : this dynamique'),

# Jour 14 — ALGO
("ALGO", "Linked List — reverse",
 "Comment inverser une linked list en O(n) O(1) mémoire ?",
 'function reverse(head) {\n  let prev = null, curr = head\n  while (curr) {\n    let next = curr.next  // sauvegarder\n    curr.next = prev      // inverser\n    prev = curr           // avancer prev\n    curr = next           // avancer curr\n  }\n  return prev\n}',
 ['Utiliser un tableau', 'Récursion', '3 pointeurs', 'Impossible en O(1)'],
 2,
 '3 pointeurs',
 'La technique des 3 pointeurs (prev, curr, next) permet\nd\'inverser en un seul passage O(n) sans mémoire extra.\nC\'est un classique des entretiens GAFAM.',
 '// prev=null → curr → next : on réoriente un à un'),

# Jour 15 — JS
("JS", "Array.map() vs forEach()",
 "Lequel retourne un nouveau tableau ?",
 'const nums = [1, 2, 3]\nconst a = nums.map(x => x * 2)\nconst b = nums.forEach(x => x * 2)\nconsole.log(a, b)',
 ['undefined, [2,4,6]', '[2,4,6], [2,4,6]', '[2,4,6], undefined', '[1,2,3], [1,2,3]'],
 2,
 '[2,4,6], undefined',
 'map() retourne un nouveau tableau transformé.\nforEach() retourne toujours undefined.\nForEach est pour les effets de bord, map pour la transformation.',
 '// map → nouveau tableau | forEach → undefined'),

# Jour 16 — ALGO
("ALGO", "Stack — valid parentheses",
 "Comment valider des parenthèses avec une Stack ?",
 'function isValid(s) {\n  const stack = []\n  const map = { ")":"(", "}":"{", "]":"[" }\n  for (let c of s) {\n    if ("([{".includes(c)) stack.push(c)\n    else if (stack.pop() !== map[c]) return false\n  }\n  return stack.length === 0\n}\nconsole.log(isValid("({[]})"))',
 ['false', 'true', 'Error', '"({[]})"'],
 1,
 'true',
 'On pousse les ouvrants sur la stack.\nPour chaque fermant, on vérifie que le top\nde la stack est l\'ouvrant correspondant.',
 '// Stack LIFO = parfait pour matcher des paires'),

# Jour 17 — JS
("JS", "Array.reduce()",
 "Que retourne ce code ?",
 'const arr = [1, 2, 3, 4, 5]\nconst result = arr.reduce((acc, curr) => acc + curr, 0)\nconsole.log(result)',
 ['[1,2,3,4,5]', '15', '0', 'Error'],
 1,
 '15',
 'reduce() accumule les valeurs avec une fonction.\nAcc commence à 0, puis on additionne chaque élément :\n0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15.',
 '// reduce(fn, initialValue) : le couteau suisse des arrays'),

# Jour 18 — ALGO
("ALGO", "Fibonacci — complexité",
 "Quelle est la complexité de la version récursive naïve ?",
 'function fib(n) {\n  if (n <= 1) return n\n  return fib(n-1) + fib(n-2)\n}\n// fib(5) calcule fib(3) 2 fois\n// fib(4) calcule fib(2) 3 fois...',
 ['O(n)', 'O(n log n)', 'O(2ⁿ)', 'O(n²)'],
 2,
 'O(2ⁿ)',
 'Chaque appel crée 2 sous-appels → arbre binaire.\nL\'arbre a une profondeur n → 2ⁿ appels au total.\nAvec mémoisation (cache) on passe à O(n) !',
 '// memo = {} → if(memo[n]) return memo[n]'),

# Jour 19 — JS
("JS", "Promise — then/catch",
 "Dans quel ordre s'affichent ces logs ?",
 'console.log("1")\nPromise.resolve("2").then(v => console.log(v))\nconsole.log("3")',
 ['1, 2, 3', '2, 1, 3', '1, 3, 2', '3, 1, 2'],
 2,
 '1, 3, 2',
 'Le code synchrone s\'exécute en premier (1, 3).\nLes .then() sont des microtasks : ils s\'exécutent\naprès le code synchrone, avant le prochain tick.',
 '// Microtasks > Macrotasks (setTimeout, setInterval)'),

# Jour 20 — ALGO
("ALGO", "Two pointers — sum pair",
 "Trouve une paire dont la somme = 9 dans ce tableau trié.",
 'const arr = [1, 2, 4, 6, 8, 10]\n// Trouver les indices de la paire [i, j]\n// tel que arr[i] + arr[j] === 9\n// Solution: arr[1] + arr[3] = 2 + 6 = ??? ',
 ['= 8', '= 9', '= 10', '= 7'],
 1,
 '= 9',
 'Avec deux pointeurs (gauche et droite) :\n- Si sum < target → avancer gauche\n- Si sum > target → reculer droite\nO(n) au lieu de O(n²) avec la boucle double.',
 '// Two pointers : always sur tableaux TRIÉS'),

# Jour 21 — JS
("JS", "Spread operator",
 "Que contient newArr ?",
 'const arr1 = [1, 2, 3]\nconst arr2 = [4, 5, 6]\nconst newArr = [...arr1, ...arr2]\nconsole.log(newArr)',
 ['[[1,2,3],[4,5,6]]', '[1,2,3,4,5,6]', '[1,2,3]', 'Error'],
 1,
 '[1,2,3,4,5,6]',
 'L\'opérateur spread (...) "étale" les éléments.\n[...arr1, ...arr2] crée un nouveau tableau fusionné.\nC\'est l\'équivalent moderne de arr1.concat(arr2).',
 '// Spread: copie, fusion, args de fonction'),

# Jour 22 — ALGO
("ALGO", "Sliding Window — max sum",
 "Trouve la sous-liste de longueur 3 avec la somme maximale.",
 'const arr = [2, 1, 5, 1, 3, 2]\n// Taille fenêtre k = 3\n// [2,1,5] → 8\n// [1,5,1] → 7\n// [5,1,3] → 9 ← max\n// [1,3,2] → 6',
 ['8', '7', '9', '10'],
 2,
 '9',
 'Sliding window : on maintient une "fenêtre" de taille k.\nOn glisse d\'un pas à la fois, en ajoutant le nouvel\nélément et retirant l\'ancien. O(n) au lieu de O(n·k).',
 '// sum += arr[i] - arr[i-k] à chaque slide'),

# Jour 23 — JS
("JS", "Destructuring objets",
 "Que contient name et age ?",
 'const user = { name: "Alice", age: 25, city: "Paris" }\nconst { name, age } = user\nconsole.log(name, age)',
 ['"Alice", 25', 'undefined, undefined', 'Error', '"Alice", undefined'],
 0,
 '"Alice", 25',
 'La destructuration extrait les propriétés par leur nom.\nOn peut aussi renommer : const { name: n } = user\nOu définir une valeur par défaut : const { age = 0 } = user',
 '// const { a, b = "default" } = obj'),

# Jour 24 — ALGO
("ALGO", "HashMap — frequency count",
 "Comment compter les occurrences de chaque lettre ?",
 'function charCount(s) {\n  const map = {}\n  for (let c of s) {\n    map[c] = (map[c] || 0) + 1\n  }\n  return map\n}\nconsole.log(charCount("hello"))',
 ['{ h:1,e:1,l:1,o:1 }', '{ h:1,e:1,l:2,o:1 }', '5', 'Error'],
 1,
 '{ h:1,e:1,l:2,o:1 }',
 '"hello" contient 2x "l" → l:2.\nLa technique HashMap/freq-count est fondamentale :\nanagrammes, doublons, top-K... tout s\'appuie dessus.',
 '// map[c] = (map[c] || 0) + 1 : pattern classique'),

# Jour 25 — JS
("JS", "Template literals",
 "Que va afficher ce code ?",
 'const name = "monde"\nconst age = 2026\nconsole.log(`Bonjour ${name} en ${age}`)',
 ['"Bonjour ${name} en ${age}"', '"Bonjour monde en 2026"', 'Error', 'undefined'],
 1,
 '"Bonjour monde en 2026"',
 'Les backticks (`) permettent l\'interpolation avec ${}.\nOn peut y mettre n\'importe quelle expression JS :\n`${1 + 1}` → "2", `${fn()}` → résultat de fn()',
 '// Backtick = strings puissantes avec interpolation'),

# Jour 26 — ALGO
("ALGO", "Recursion — factorial",
 "Que retourne factorial(5) ?",
 'function factorial(n) {\n  if (n <= 1) return 1\n  return n * factorial(n - 1)\n}\nconsole.log(factorial(5))',
 ['25', '120', '60', 'Infinity'],
 1,
 '120',
 '5! = 5 × 4 × 3 × 2 × 1 = 120\nLa récursion appelle la fonction avec n-1 à chaque fois.\nCas de base : n <= 1 → retourne 1 pour stopper.',
 '// Toujours définir un cas de base !'),

# Jour 27 — JS
("JS", "null vs undefined",
 "Laquelle de ces comparaisons est vraie ?",
 'console.log(null == undefined)\nconsole.log(null === undefined)',
 ['false / false', 'true / true', 'true / false', 'false / true'],
 2,
 'true / false',
 'null == undefined → true (cas spécial de la spec JS).\nnull === undefined → false (types différents).\nC\'est la seule valeur pour laquelle == et === divergent ainsi.',
 '// null == undefined SEULEMENT entre eux'),

# Jour 28 — ALGO
("ALGO", "Merge Sort",
 "Quelle est la complexité de Merge Sort ?",
 'function mergeSort(arr) {\n  if (arr.length <= 1) return arr\n  const mid = Math.floor(arr.length / 2)\n  const left = mergeSort(arr.slice(0, mid))\n  const right = mergeSort(arr.slice(mid))\n  return merge(left, right)\n}',
 ['O(n²)', 'O(n)', 'O(n log n)', 'O(log n)'],
 2,
 'O(n log n)',
 'Merge sort divise en 2 à chaque niveau → log n niveaux.\nÀ chaque niveau, on fait O(n) opérations pour merge.\nTotal : O(n log n) — optimal pour un tri par comparaison.',
 '// Stable, prévisible, idéal pour les grandes listes'),

# Jour 29 — JS
("JS", "Optional chaining ?.",
 "Que retourne ce code sans planter ?",
 'const user = { profile: null }\nconsole.log(user?.profile?.name)\nconsole.log(user.profile.name)',
 ['undefined / Error', '"null" / Error', 'null / Error', 'undefined / undefined'],
 0,
 'undefined / Error',
 'user?.profile?.name → si profile est null/undefined, renvoie undefined sans planter.\nuser.profile.name → TypeError car on tente d\'accéder à .name sur null.',
 '// ?. = accès sécurisé | sans : TypeError'),

# Jour 30 — ALGO
("ALGO", "Quick Sort — pivot",
 "Quelle est la complexité moyenne de Quick Sort ?",
 'function quickSort(arr) {\n  if (arr.length <= 1) return arr\n  const pivot = arr[arr.length - 1]\n  const left  = arr.slice(0,-1).filter(x => x <= pivot)\n  const right = arr.slice(0,-1).filter(x => x > pivot)\n  return [...quickSort(left), pivot, ...quickSort(right)]\n}',
 ['O(n²)', 'O(n)', 'O(n log n)', 'O(log n)'],
 2,
 'O(n log n)',
 'En moyenne, le pivot sépare bien → log n niveaux.\nPire cas (pivot = min ou max) → O(n²).\nEn pratique très rapide en mémoire (in-place possible).',
 '// Pivot aléatoire = meilleure protection O(n²)'),

# Jour 31 — JS
("JS", "Nullish coalescing ??",
 "Que va afficher ce code ?",
 'const a = null ?? "défaut"\nconst b = 0 ?? "défaut"\nconst c = "" ?? "défaut"\nconsole.log(a, b, c)',
 ['"défaut", "défaut", "défaut"', '"défaut", 0, ""', '3 fois "défaut"', 'Error'],
 1,
 '"défaut", 0, ""',
 '?? retourne le côté droit UNIQUEMENT si gauche est null/undefined.\n0 et "" ne sont pas null/undefined → ils passent.\nContrairement à ||, qui considère 0 et "" comme falsy.',
 '// ?? = seulement null/undefined | || = tout falsy'),

# Jour 32 — ALGO
("ALGO", "Valid parentheses — complexité",
 "Complexité de la solution avec Stack pour les parenthèses ?",
 'function isValid(s) {\n  const stack = []\n  const map = { ")":"(", "}":"{", "]":"[" }\n  for (let c of s) {\n    if ("([{".includes(c)) stack.push(c)\n    else if (stack.pop() !== map[c]) return false\n  }\n  return stack.length === 0\n}',
 ['O(n²) temps, O(n) espace', 'O(n) temps, O(n) espace', 'O(n) temps, O(1) espace', 'O(log n) temps, O(1) espace'],
 1,
 'O(n) temps, O(n) espace',
 'On parcourt la string une seule fois → O(n) temps.\nLa stack peut contenir au max n éléments → O(n) espace.\nPas d\'algo O(1) espace possible ici car on doit tracer les ouvrants.',
 '// Stack size = moitié max de la string en pire cas'),

# Jour 33 — JS
("JS", "Array.filter()",
 "Que retourne ce code ?",
 'const nums = [1, 2, 3, 4, 5, 6]\nconst even = nums.filter(n => n % 2 === 0)\nconsole.log(even)',
 ['[1,3,5]', '[2,4,6]', 'true', '[1,2,3,4,5,6]'],
 1,
 '[2,4,6]',
 'filter() retourne un nouveau tableau avec les éléments\npour lesquels la fonction retourne true.\nn % 2 === 0 → vrai pour 2, 4, 6.',
 '// filter + map + reduce = la trilogie FP'),

# Jour 34 — ALGO
("ALGO", "Binary Tree — BFS",
 "BFS sur un arbre binaire utilise quelle structure ?",
 'function bfs(root) {\n  const queue = [root]\n  while (queue.length) {\n    const node = queue.shift()\n    console.log(node.val)\n    if (node.left)  queue.push(node.left)\n    if (node.right) queue.push(node.right)\n  }\n}',
 ['Stack (LIFO)', 'Queue (FIFO)', 'HashMap', 'Array trié'],
 1,
 'Queue (FIFO)',
 'BFS (Breadth-First Search) explore niveau par niveau.\nOn utilise une Queue FIFO : on traite les nœuds dans l\'ordre d\'insertion.\nDFS utilise une Stack (ou la récursion).',
 '// BFS = Queue | DFS = Stack/recursion'),

# Jour 35 — JS
("JS", "Object.keys()",
 "Que retourne Object.keys() sur cet objet ?",
 'const obj = { a: 1, b: 2, c: 3 }\nconsole.log(Object.keys(obj))\nconsole.log(Object.values(obj))',
 ['[1,2,3] / ["a","b","c"]', '["a","b","c"] / [1,2,3]', '{"a":1} / [1]', 'Error'],
 1,
 '["a","b","c"] / [1,2,3]',
 'Object.keys() retourne les clés (noms des propriétés).\nObject.values() retourne les valeurs.\nObject.entries() retourne [clé, valeur] pour chaque prop.',
 '// Object.entries(obj) → [["a",1],["b",2],...]'),

# Jour 36 — ALGO
("ALGO", "Reverse string",
 "Quelle méthode est la plus concise pour inverser ?",
 'const s = "codebog"\n// Option A:\nconst a = s.split("").reverse().join("")\n// Option B (two pointers):\nconst arr = s.split("")\nlet l = 0, r = arr.length - 1\nwhile (l < r) {\n  [arr[l], arr[r]] = [arr[r], arr[l]]\n  l++; r--\n}\nconst b = arr.join("")',
 ['A et B donnent "gobedoc"', 'A donne "gobedoc", B différent', 'A = "gobedoc" = B', 'B est incorrect'],
 2,
 'A = "gobedoc" = B',
 'Les deux donnent "gobedoc" mais avec des trade-offs :\nA : concis, O(n) mémoire (3 arrays créés).\nB : verbeux, O(1) mémoire (in-place, idéal en entretien).',
 '// Two pointers in-place = meilleure réponse entretien'),

# Jour 37 — JS
("JS", "async/await vs Promise",
 "Ces deux codes sont-ils équivalents ?",
 '// Version A — Promise\nfetch(url).then(r => r.json()).then(d => console.log(d))\n\n// Version B — async/await\nasync function get() {\n  const r = await fetch(url)\n  const d = await r.json()\n  console.log(d)\n}',
 ['Oui, strictement équivalents', 'Non, A est plus rapide', 'Non, B bloque le thread', 'Non, syntaxe différente seulement'],
 0,
 'Oui, strictement équivalents',
 'async/await est du sucre syntaxique sur les Promises.\nLes deux font exactement la même chose sous le capot.\nasync/await est juste plus lisible (style synchrone).',
 '// async fn retourne toujours une Promise'),

# Jour 38 — ALGO
("ALGO", "FizzBuzz",
 "Quelle est la sortie pour i = 15 ?",
 'for (let i = 1; i <= 20; i++) {\n  if (i % 15 === 0) console.log("FizzBuzz")\n  else if (i % 3 === 0) console.log("Fizz")\n  else if (i % 5 === 0) console.log("Buzz")\n  else console.log(i)\n}',
 ['"Fizz"', '"Buzz"', '"FizzBuzz"', '"15"'],
 2,
 '"FizzBuzz"',
 '15 est divisible par 3 ET par 5 (15 % 15 === 0).\nL\'ordre des conditions est crucial :\nVérifier d\'abord % 15, sinon on tomberait sur "Fizz".',
 '// FizzBuzz : classique des entretiens débutants'),

# Jour 39 — JS
("JS", "Prototype chain",
 "Que retourne ce code ?",
 'function Animal(name) {\n  this.name = name\n}\nAnimal.prototype.speak = function() {\n  return `${this.name} parle`\n}\nconst dog = new Animal("Rex")\nconsole.log(dog.speak())',
 ['Error: speak is not a function', '"Rex parle"', '"Animal parle"', 'undefined'],
 1,
 '"Rex parle"',
 'dog n\'a pas la méthode speak en propre.\nJS remonte la chaîne de prototype : dog → Animal.prototype.\nIl y trouve speak() et l\'exécute avec this = dog.',
 '// Chaque objet a un __proto__ vers son prototype'),

# Jour 40 — ALGO
("ALGO", "Is Prime?",
 "Ce code détecte-t-il correctement les nombres premiers ?",
 'function isPrime(n) {\n  if (n < 2) return false\n  for (let i = 2; i <= Math.sqrt(n); i++) {\n    if (n % i === 0) return false\n  }\n  return true\n}\nconsole.log(isPrime(17))',
 ['false — bug', 'true ✅', 'Error', '"premier"'],
 1,
 'true ✅',
 '17 est bien premier. La boucle va jusqu\'à √17 ≈ 4.\nOn teste : 17%2, 17%3, 17%4 → aucun diviseur → premier.\nAller jusqu\'à √n suffit : si diviseur > √n, l\'autre est < √n.',
 '// O(√n) au lieu de O(n) — optimisation clé'),

# Jour 41 — JS
("JS", "Event Loop — setTimeout",
 "Dans quel ordre s'affichent ces logs ?",
 'console.log("A")\nsetTimeout(() => console.log("B"), 0)\nPromise.resolve().then(() => console.log("C"))\nconsole.log("D")',
 ['A, B, C, D', 'A, D, C, B', 'A, D, B, C', 'A, C, D, B'],
 1,
 'A, D, C, B',
 'Ordre d\'exécution :\n1. Synchrone : A, D\n2. Microtasks (Promise.then) : C\n3. Macrotasks (setTimeout) : B\nMicrotasks toujours avant Macrotasks !',
 '// Microtask queue > Callback queue'),

# Jour 42 — ALGO
("ALGO", "Merge intervals",
 "Quel est le résultat du merge de ces intervalles ?",
 'const intervals = [[1,3],[2,6],[8,10],[15,18]]\n// Après merge :\n// [1,3] et [2,6] se chevauchent → [1,6]\n// [8,10] seul\n// [15,18] seul',
 ['[[1,3],[2,6],[8,10],[15,18]]', '[[1,6],[8,10],[15,18]]', '[[1,10],[15,18]]', '[[1,18]]'],
 1,
 '[[1,6],[8,10],[15,18]]',
 'On trie d\'abord par le début, puis on merge :\nSi current.start <= last.end → on étend last.\nSinon on pousse current tel quel.',
 '// Toujours trier avant de merger les intervalles'),

# Jour 43 — JS
("JS", "Symbol",
 "Que retourne cette comparaison ?",
 'const s1 = Symbol("id")\nconst s2 = Symbol("id")\nconsole.log(s1 === s2)\nconsole.log(typeof s1)',
 ['true / "symbol"', 'false / "symbol"', 'true / "object"', 'Error'],
 1,
 'false / "symbol"',
 'Chaque Symbol() est unique, même avec la même description.\ns1 !== s2 car ce sont deux valeurs primitives distinctes.\nSymbol est le 7ème type primitif de JS (après ES6).',
 '// Symbol : clés uniques, non-énumérables'),

# Jour 44 — ALGO
("ALGO", "Max subarray — Kadane",
 "Trouve la sous-liste avec la somme maximale.",
 'const arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\n// Algorithme de Kadane\n// Réponse : [4,-1,2,1] → somme = 6\nfunction maxSubArray(nums) {\n  let maxSum = nums[0], curr = nums[0]\n  for (let i = 1; i < nums.length; i++) {\n    curr = Math.max(nums[i], curr + nums[i])\n    maxSum = Math.max(maxSum, curr)\n  }\n  return maxSum\n}',
 ['4', '5', '6', '7'],
 2,
 '6',
 'Kadane\'s algorithm en O(n) :\nÀ chaque position, on décide : continuer la sous-liste\nou recommencer depuis ici. maxSum garde le meilleur.',
 '// Kadane : DP classique, O(n) temps O(1) espace'),

# Jour 45 — JS
("JS", "WeakMap vs Map",
 "Quelle est la différence clé entre Map et WeakMap ?",
 'const map = new Map()\nconst wmap = new WeakMap()\nlet obj = { id: 1 }\nmap.set(obj, "data")\nwmap.set(obj, "data")\nobj = null // obj déréférencé',
 ['Identiques', 'WeakMap: GC libère | Map: garde la ref', 'Map est plus rapide', 'WeakMap accepte les strings'],
 1,
 'WeakMap: GC libère | Map: garde la ref',
 'Map garde une référence forte → obj ne sera jamais GC\'d.\nWeakMap garde une référence faible → si obj = null,\nle GC peut libérer la mémoire automatiquement.',
 '// WeakMap = pas d\'itération, pas de size, GC-friendly'),

# Jour 46 — ALGO
("ALGO", "Contains duplicate",
 "Complexité optimale pour détecter les doublons ?",
 'function hasDuplicate(nums) {\n  const seen = new Set()\n  for (let n of nums) {\n    if (seen.has(n)) return true\n    seen.add(n)\n  }\n  return false\n}\n// Input: [1, 2, 3, 1] → ???',
 ['false', 'true', 'Error', '[1]'],
 1,
 'true',
 '[1,2,3,1] contient 1 en double → true.\nSolution Set : O(n) temps, O(n) espace.\nAlternative : trier d\'abord O(n log n) O(1) espace.',
 '// Set.has() → O(1) en moyenne'),

# Jour 47 — JS
("JS", "try/catch/finally",
 "Que retourne cette fonction ?",
 'function test() {\n  try {\n    throw new Error("oups")\n    return "try"\n  } catch (e) {\n    return "catch"\n  } finally {\n    return "finally"\n  }\n}\nconsole.log(test())',
 ['"try"', '"catch"', '"finally"', 'Error'],
 2,
 '"finally"',
 'finally s\'exécute TOUJOURS, même si try/catch retourne.\nLe return "finally" écrase le return "catch".\nC\'est un piège classique : finally peut override le return !',
 '// finally écrase les return de try/catch'),

# Jour 48 — ALGO
("ALGO", "Climbing stairs — DP",
 "Combien de façons d'atteindre la marche 4 (1 ou 2 pas) ?",
 'function climbStairs(n) {\n  if (n <= 2) return n\n  let a = 1, b = 2\n  for (let i = 3; i <= n; i++) {\n    [a, b] = [b, a + b]\n  }\n  return b\n}\n// n=1:1, n=2:2, n=3:3, n=4:???',
 ['4', '5', '6', '7'],
 1,
 '5',
 'C\'est la séquence de Fibonacci !\n4 marches : (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)\n= 5 façons.\nDP bottom-up O(n) temps, O(1) espace.',
 '// Climbing stairs = Fibonacci déguisé'),

# Jour 49 — JS
("JS", "Array destructuring avec default",
 "Que contient b ?",
 'const [a, b = 10, c] = [1, undefined, 3]\nconsole.log(b)',
 ['undefined', '10', '1', 'Error'],
 1,
 '10',
 'La valeur par défaut (= 10) s\'applique UNIQUEMENT\nsi la valeur est undefined (pas null, pas 0, pas "").\nIci, le 2ème élément est undefined → b = 10.',
 '// Default destructuring : seulement pour undefined'),

# Jour 50 — ALGO
("ALGO", "House Robber — DP",
 "Montant max sans voler 2 maisons adjacentes ?",
 'const houses = [2, 7, 9, 3, 1]\n// On ne peut pas voler 2 maisons consécutives\n// Option 1: 2+9+1 = 12\n// Option 2: 7+3  = 10\n// Option 3: 2+9  = 11\n// Option 4: 7+9  ✗ adjacentes',
 ['10', '11', '12', '13'],
 2,
 '12',
 'DP : à chaque maison, on choisit le max entre :\n- Voler ici + meilleur des 2 avant\n- Ne pas voler, garder le meilleur d\'avant.\nFormule : dp[i] = max(dp[i-1], dp[i-2] + houses[i])',
 '// 2+9+1 = 12 — toujours vérifier toutes options'),

# Jour 51 — JS
("JS", "Promise.all()",
 "Que se passe-t-il si une Promise rejette dans Promise.all() ?",
 'Promise.all([\n  Promise.resolve(1),\n  Promise.reject("erreur"),\n  Promise.resolve(3)\n]).then(r => console.log(r))\n  .catch(e => console.log(e))',
 ['"erreur"', '[1, "erreur", 3]', '[1, 3]', 'Error'],
 0,
 '"erreur"',
 'Promise.all() est "fail-fast" : si UNE rejette, tout échoue.\nOn passe immédiatement dans .catch() avec la raison du rejet.\nPour tolérer les erreurs, utiliser Promise.allSettled().',
 '// Promise.allSettled() → attend TOUTES même si erreur'),

# Jour 52 — ALGO
("ALGO", "Number of islands",
 "Combien d'îles dans cette grille ?",
 'const grid = [\n  ["1","1","0","0","0"],\n  ["1","1","0","0","0"],\n  ["0","0","1","0","0"],\n  ["0","0","0","1","1"]\n]\n// Îles = groupes de "1" connectés (haut/bas/gauche/droite)',
 ['2', '3', '4', '5'],
 1,
 '3',
 'Île 1 : les 4 cases "1" en haut-gauche.\nÎle 2 : le "1" isolé au centre.\nÎle 3 : les 2 "1" en bas-droite.\nSolution : DFS/BFS pour marquer les îles visitées.',
 '// DFS : marquer "0" pour éviter de recompter'),

# Jour 53 — JS
("JS", "Generator function",
 "Que va afficher ce code ?",
 'function* count() {\n  yield 1\n  yield 2\n  yield 3\n}\nconst gen = count()\nconsole.log(gen.next().value)\nconsole.log(gen.next().value)',
 ['Error', '1, 1', '1, 2', '3, 3'],
 2,
 '1, 2',
 'Un générateur est une fonction pausable.\nYield suspend l\'exécution et retourne une valeur.\nNext() reprend depuis le dernier yield.',
 '// { value, done } : structure retournée par next()'),

# Jour 54 — ALGO
("ALGO", "LRU Cache",
 "LRU Cache évicte quelle entrée quand il est plein ?",
 '// LRU = Least Recently Used\n// Cache taille 3 :\n// Accès: A, B, C, A, D\n// État après D : ???\n// [B, C, A] → D insère → évicte ???',
 ['A (dernier accédé)', 'B (le moins récent)', 'C (le milieu)', 'D (le plus récent)'],
 1,
 'B (le moins récent)',
 'LRU évicte l\'élément LE MOINS RÉCEMMENT UTILISÉ.\nAprès les accès A,B,C,A,D : l\'ordre est B,C,A (récent).\nD insère et B est évincé car le plus ancien.',
 '// Implémentation : HashMap + Doubly Linked List'),

# Jour 55 — JS
("JS", "for...of vs for...in",
 "Que va logger ce code ?",
 'const arr = [10, 20, 30]\nfor (let i in arr) {\n  console.log(typeof i)\n}\nfor (let v of arr) {\n  console.log(typeof v)\n}',
 ['"number" x3 / "number" x3', '"string" x3 / "number" x3', '"number" x3 / "string" x3', '"string" x3 / "string" x3'],
 1,
 '"string" x3 / "number" x3',
 'for...in itère sur les INDICES (comme clés) → strings "0","1","2".\nfor...of itère sur les VALEURS → numbers 10, 20, 30.\nfor...in sur les arrays est déconseillé (peut itérer les proto props).',
 '// for...of pour les valeurs | for...in pour les clés'),

# Jour 56 — ALGO
("ALGO", "Top K elements — Heap",
 "Comment trouver les K plus grands éléments efficacement ?",
 'function topK(nums, k) {\n  // Min-Heap de taille k\n  // Parcourir nums:\n  //   push dans le heap\n  //   si heap.size > k → pop le minimum\n  // Résultat : les k plus grands restent\n}\n// Input: [3,1,5,12,2,11], k=3\n// Output: [5,11,12]',
 ['O(n log n)', 'O(n log k)', 'O(n²)', 'O(k log n)'],
 1,
 'O(n log k)',
 'Un min-heap de taille k : O(n log k).\nMieux que trier tout O(n log n) si k << n.\nLe top du heap est toujours le plus petit des k grands.',
 '// Heap de taille k : optimal pour "top K" problems'),

# Jour 57 — JS
("JS", "Object.freeze()",
 "Que se passe-t-il avec Object.freeze() ?",
 'const obj = Object.freeze({ x: 1, y: 2 })\nobj.x = 99\nobj.z = 3\nconsole.log(obj)',
 ['{ x: 99, y: 2, z: 3 }', '{ x: 1, y: 2 }', 'TypeError', '{ x: 1, y: 2, z: 3 }'],
 1,
 '{ x: 1, y: 2 }',
 'freeze() empêche toute modification de l\'objet.\nEn mode strict → TypeError. En mode normal → silencieux.\nAttention : freeze est SHALLOW (pas récursif).',
 '// Deep freeze : appeler freeze() sur chaque sous-objet'),

# Jour 58 — ALGO
("ALGO", "Coin change — DP",
 "Minimum de pièces pour faire 11 avec [1,5,6,9] ?",
 '// coins = [1, 5, 6, 9], amount = 11\n// Option 1: 9 + 1 + 1 = 3 pièces\n// Option 2: 6 + 5 = 2 pièces ← optimal\n// Option 3: 5 + 5 + 1 = 3 pièces\n// Greedy: 9+1+1 = 3 ← sous-optimal !',
 ['3 pièces', '2 pièces', '1 pièce', 'Impossible'],
 1,
 '2 pièces',
 '6 + 5 = 11 en 2 pièces seulement.\nL\'algo greedy (prendre la plus grande) donne 9+1+1=3.\nIl faut la DP : dp[i] = min pièces pour la somme i.',
 '// DP bottom-up : dp[0]=0, dp[i]=min(dp[i-coin]+1)'),

# Jour 59 — JS
("JS", "Currying",
 "Que retourne curry(1)(2)(3) ?",
 'function curry(a) {\n  return function(b) {\n    return function(c) {\n      return a + b + c\n    }\n  }\n}\nconsole.log(curry(1)(2)(3))',
 ['Error', '6', '"123"', 'undefined'],
 1,
 '6',
 'Le currying transforme f(a,b,c) en f(a)(b)(c).\nChaque appel retourne une fonction qui "se souvient"\ndes arguments précédents grâce aux closures.',
 '// Currying : application partielle et composition'),

# Jour 60 — ALGO
("ALGO", "Course Schedule — cycle",
 "Peut-on finir tous les cours ? (cycle = impossible)",
 'const numCourses = 4\nconst prereqs = [[1,0],[2,1],[3,2]]\n// 0→1→2→3 : pas de cycle\n\nconst prereqs2 = [[1,0],[0,1]]\n// 0→1→0 : cycle !',
 ['prereqs: oui, prereqs2: oui', 'prereqs: oui, prereqs2: non', 'prereqs: non, prereqs2: oui', 'Les deux: non'],
 1,
 'prereqs: oui, prereqs2: non',
 'On modélise en graphe orienté et on détecte les cycles.\nPrereqs forme une chaîne linéaire → pas de cycle → possible.\nPrereqs2 forme un cycle 0↔1 → impossible.',
 '// DFS + coloring (blanc/gris/noir) pour détecter cycles'),

# ── PHASE 2 : Intermédiaire (jours 61-150) ──────────────────────────
# Jour 61 — JS
("JS", "Debounce",
 "À quoi sert le debounce ?",
 'function debounce(fn, delay) {\n  let timer\n  return function(...args) {\n    clearTimeout(timer)\n    timer = setTimeout(() => fn(...args), delay)\n  }\n}\n// Utilisé pour : recherche live, resize, scroll',
 ['Répéter fn toutes les N ms', 'Délayer fn jusqu\'à arrêt des appels', 'Limiter fn à 1 appel/sec', 'Mettre fn en cache'],
 1,
 'Délayer fn jusqu\'à arrêt des appels',
 'Debounce attend que les appels s\'arrêtent N ms\navant d\'exécuter la fonction. Idéal pour les événements\nfréquents : resize, keyup de recherche, scroll.',
 '// Debounce: attend l\'arrêt | Throttle: limite la cadence'),

# Jour 62 — ALGO
("ALGO", "Word search — backtracking",
 "Backtracking : on revient en arrière quand ?",
 'function exist(board, word) {\n  // DFS + backtracking\n  function dfs(i, j, k) {\n    if (k === word.length) return true\n    if (/* hors limites ou mauvaise lettre */) return false\n    board[i][j] = "#"           // marquer visité\n    const found = dfs(i+1,j,k+1) || dfs(i-1,j,k+1)\n                || dfs(i,j+1,k+1) || dfs(i,j-1,k+1)\n    board[i][j] = word[k]       // restaurer\n    return found\n  }\n}',
 ['Jamais', 'Quand on sort des limites', 'Quand un chemin ne mène pas à la solution', 'À chaque étape'],
 2,
 'Quand un chemin ne mène pas à la solution',
 'Backtracking = DFS + annulation des choix erronés.\nOn marque la cellule comme visitée (#), on explore,\npuis on RESTAURE si on ne trouve pas le mot.',
 '// board[i][j] = "#" → explore → board[i][j] = word[k]'),

# Jour 63 — JS
("JS", "Memoization",
 "Combien de fois fib(3) est-il calculé sans mémo ?",
 'function fib(n) {\n  if (n <= 1) return n\n  return fib(n-1) + fib(n-2)\n}\nfib(5)\n// fib(5) appelle fib(4) et fib(3)\n// fib(4) appelle fib(3) et fib(2)\n// fib(3) est calculé ???',
 ['1 fois', '2 fois', '3 fois', '5 fois'],
 1,
 '2 fois',
 'Sans mémo, fib(3) est calculé 2 fois dans fib(5).\nAvec mémo (cache), chaque valeur est calculée 1 seule fois.\nO(2ⁿ) → O(n) avec la mémoisation !',
 '// const memo = {}; if(memo[n]) return memo[n]'),

# Jour 64 — ALGO
("ALGO", "Longest palindromic substring",
 "Quelle est la longueur du plus long palindrome dans 'babad' ?",
 'function longestPalin(s) {\n  let longest = ""\n  for (let i = 0; i < s.length; i++) {\n    // Expand around center (odd & even)\n    for (let odd of [true, false]) {\n      let l = i, r = odd ? i : i + 1\n      while (l >= 0 && r < s.length && s[l] === s[r])\n        { l--; r++ }\n      const sub = s.slice(l+1, r)\n      if (sub.length > longest.length) longest = sub\n    }\n  }\n  return longest\n}\n// Input: "babad"',
 ['"b" (1)', '"ba" (2)', '"bab" (3)', '"babad" (5)'],
 2,
 '"bab" (3)',
 '"bab" et "aba" sont tous deux des palindromes de longueur 3.\n"bab" est retourné en premier.\nAlgo expand-around-center : O(n²) temps, O(1) espace.',
 '// Manacher\'s algorithm : O(n) pour les pros'),

# Jour 65 — JS
("JS", "Throttle",
 "Quelle est la différence entre debounce et throttle ?",
 'function throttle(fn, limit) {\n  let lastCall = 0\n  return function(...args) {\n    const now = Date.now()\n    if (now - lastCall >= limit) {\n      lastCall = now\n      return fn(...args)\n    }\n  }\n}\n// scroll, mousemove, resize...',
 ['Throttle = attend l\'arrêt', 'Throttle = exécute max 1 fois/période', 'Debounce = 1 appel/période', 'Identiques'],
 1,
 'Throttle = exécute max 1 fois/période',
 'Throttle garantit max 1 exécution par période de temps.\nMême si 100 scroll events arrivent, fn s\'exécute max 1x/250ms.\nDebounce attend que TOUT soit arrêté.',
 '// Throttle: cadence fixe | Debounce: après silence'),

# Jour 66 — ALGO
("ALGO", "Trie — préfixes",
 "Un Trie est optimal pour quelle opération ?",
 'class Trie {\n  constructor() { this.root = {} }\n  insert(word) {\n    let node = this.root\n    for (let c of word) {\n      if (!node[c]) node[c] = {}\n      node = node[c]\n    }\n    node.end = true\n  }\n  startsWith(prefix) {\n    let node = this.root\n    for (let c of prefix) {\n      if (!node[c]) return false\n      node = node[c]\n    }\n    return true\n  }\n}',
 ['Recherche par valeur O(1)', 'Recherche par préfixe O(m)', 'Tri alphabétique O(n)', 'Suppression O(log n)'],
 1,
 'Recherche par préfixe O(m)',
 'Un Trie permet la recherche par préfixe en O(m) où m = longueur du préfixe.\nParfait pour l\'autocomplétion, correcteurs orthographiques.\nChaque nœud représente un caractère.',
 '// Trie: O(m) insert/search, m = length du mot'),

# Jour 67 — JS
("JS", "Error types",
 "Quel type d'erreur est lancé ici ?",
 'null.toString()',
 ['Error', 'TypeError', 'ReferenceError', 'SyntaxError'],
 1,
 'TypeError',
 'Accéder à une propriété sur null/undefined = TypeError.\nReferenceError : variable non déclarée.\nSyntaxError : code malformé (parsé avant exécution).',
 '// TypeError: null.x | ReferenceError: x (non déclaré)'),

# Jour 68 — ALGO
("ALGO", "Unique paths — DP",
 "Combien de chemins uniques dans une grille 3x3 ?",
 '// Robot : haut-gauche → bas-droite\n// Mouvements : droite ou bas seulement\n// Grille 3x3 :\n// dp[i][j] = dp[i-1][j] + dp[i][j-1]\n// dp[0][*] = 1, dp[*][0] = 1',
 ['4', '6', '8', '12'],
 1,
 '6',
 'Dans une grille 3x3, il y a 6 chemins uniques.\nDP : chaque cellule = somme du dessus + de gauche.\nFormule combinatoire : C(m+n-2, m-1) = C(4,2) = 6.',
 '// dp[i][j] = dp[i-1][j] + dp[i][j-1]'),

# Jour 69 — JS
("JS", "Set — collection unique",
 "Que contient ce Set ?",
 'const set = new Set([1, 2, 2, 3, 3, 3])\nset.add(4)\nset.add(2)\nconsole.log(set.size)\nconsole.log([...set])',
 ['6 / [1,2,2,3,3,3,4,2]', '4 / [1,2,3,4]', '4 / [1,2,3,3,4]', '3 / [1,2,3]'],
 1,
 '4 / [1,2,3,4]',
 'Set stocke des valeurs UNIQUES. Les doublons sont ignorés.\nAdd(2) est ignoré car 2 est déjà présent.\nSize = 4 car {1, 2, 3, 4}.',
 '// Set : dédoublonnage ultra-rapide O(1) par op'),

# Jour 70 — ALGO
("ALGO", "Dynamic programming — intro",
 "Quelle propriété doit avoir un problème pour la DP ?",
 '// DP = mémoisation de sous-problèmes\n// 2 conditions :\n// 1. Sous-problèmes chevauchants\n//    (même calcul répété)\n// 2. Sous-structure optimale\n//    (solution globale = combinaison de solutions locales optimales)',
 ['Être récursif seulement', 'Sous-problèmes chevauchants + sous-structure optimale', 'Être trié', 'Avoir O(n) complexité'],
 1,
 'Sous-problèmes chevauchants + sous-structure optimale',
 'La DP mémorise les résultats des sous-problèmes.\nSous-problèmes chevauchants : fib(3) calculé plusieurs fois.\nSous-structure optimale : optimal global = optimal local.',
 '// Top-down (mémo) ou Bottom-up (tableau)'),

# Jour 71 — JS
("JS", "Proxy",
 "Que va afficher ce code ?",
 'const handler = {\n  get(target, key) {\n    return key in target ? target[key] : `${key} non trouvé`\n  }\n}\nconst obj = new Proxy({ name: "Codebog" }, handler)\nconsole.log(obj.name)\nconsole.log(obj.age)',
 ['"Codebog" / undefined', '"Codebog" / "age non trouvé"', 'Error / Error', '"Codebog" / null'],
 1,
 '"Codebog" / "age non trouvé"',
 'Proxy intercepte les accès aux propriétés.\nLe handler get() est appelé à chaque lecture.\nOn peut valider, logger, retourner une valeur par défaut.',
 '// Proxy = méta-programmation puissante en JS'),

# Jour 72 — ALGO
("ALGO", "Bit manipulation — Single Number",
 "Trouve le nombre qui n'apparaît qu'une fois.",
 'function singleNumber(nums) {\n  return nums.reduce((xor, n) => xor ^ n, 0)\n}\n// Input: [4, 1, 2, 1, 2]\n// 0^4=4, 4^1=5, 5^2=7, 7^1=6, 6^2=4\n// Output: ???',
 ['1', '2', '4', '0'],
 2,
 '4',
 'XOR (^) a une propriété : x ^ x = 0 et x ^ 0 = x.\nTous les nombres en double s\'annulent !\n[4,1,2,1,2] → 4^(1^1)^(2^2) = 4^0^0 = 4.',
 '// XOR : solution O(n) O(1) sans HashMap'),

# Jour 73 — JS
("JS", "Promise.allSettled()",
 "Que retourne Promise.allSettled() si une rejette ?",
 'Promise.allSettled([\n  Promise.resolve("A"),\n  Promise.reject("B"),\n  Promise.resolve("C")\n]).then(results => {\n  results.forEach(r => console.log(r.status))\n})',
 ['"rejected" seulement', 'Error', '"fulfilled", "rejected", "fulfilled"', '"fulfilled", "fulfilled"'],
 2,
 '"fulfilled", "rejected", "fulfilled"',
 'allSettled() attend TOUTES les promises, succès ou échec.\nChaque résultat a un status : "fulfilled" ou "rejected".\nContraindrement à all() qui fail-fast dès la première erreur.',
 '// allSettled: robuste | all: fail-fast'),

# Jour 74 — ALGO
("ALGO", "Trapping rain water",
 "Combien d'eau est piégée dans ce profil ?",
 'const height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]\n// Visualisation :\n//        X\n//    X   X X   X\n// X  X X X X X X X X\n// Eau piégée = ???',
 ['5', '6', '7', '8'],
 1,
 '6',
 '6 unités d\'eau sont piégées.\nAlgo two-pointers : l(eft) et r(ight).\nEau en i = min(maxLeft, maxRight) - height[i].',
 '// O(n) temps O(1) espace avec two pointers'),

# Jour 75 — JS
("JS", "Class private fields",
 "Que se passe-t-il avec les champs privés # ?",
 'class Counter {\n  #count = 0\n  increment() { this.#count++ }\n  get value() { return this.#count }\n}\nconst c = new Counter()\nc.increment()\nconsole.log(c.value)\nconsole.log(c.#count)',
 ['1 / 1', '1 / Error', '0 / Error', 'Error / Error'],
 1,
 '1 / Error',
 'Les champs avec # sont vraiment privés en JS.\nc.value retourne 1 via le getter public.\nc.#count depuis l\'extérieur → SyntaxError.',
 '// # = privé, inaccessible même via Reflect/Proxy'),

# Jour 76 — ALGO
("ALGO", "Longest common subsequence",
 "Quelle est la LCS de 'ABCBDAB' et 'BDCAB' ?",
 '// LCS("ABCBDAB", "BDCAB")\n// DP : dp[i][j] = longueur LCS de s1[0..i] et s2[0..j]\n// Si s1[i] === s2[j] : dp[i][j] = dp[i-1][j-1] + 1\n// Sinon : dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n// LCS = "BCAB" ou "BDAB" → longueur ???',
 ['3', '4', '5', '6'],
 1,
 '4',
 '"BCAB" et "BDAB" sont toutes deux des LCS de longueur 4.\nDP classique O(m×n) temps et espace.\nOptimisation : O(min(m,n)) espace possible.',
 '// LCS : base pour git diff, spell check, bioinformatique'),

# Jour 77 — JS
("JS", "Logical assignment operators",
 "Quelle est la valeur finale de a ?",
 'let a = null\na ??= "défaut"\nconsole.log(a)\n\nlet b = "existant"\nb ??= "défaut"\nconsole.log(b)',
 ['"défaut" / "défaut"', '"défaut" / "existant"', 'null / "existant"', 'Error'],
 1,
 '"défaut" / "existant"',
 '??= (nullish assignment) : assigne SEULEMENT si null/undefined.\na était null → a = "défaut".\nb était "existant" (non null) → pas de changement.',
 '// ||= : falsy | &&= : truthy | ??= : null/undefined'),

# Jour 78 — ALGO
("ALGO", "Jump Game",
 "Peut-on atteindre le dernier index ?",
 'const nums = [2, 3, 1, 1, 4]\n// À chaque index i, on peut sauter 0 à nums[i] pas\n// Index 0: sauter 2 → index 1 ou 2\n// Index 1: sauter 3 → index 2,3,4 ← fin !\n\nconst nums2 = [3, 2, 1, 0, 4]\n// Index 3: nums[3]=0 → bloqué !',
 ['nums: non, nums2: oui', 'nums: oui, nums2: non', 'Les deux: oui', 'Les deux: non'],
 1,
 'nums: oui, nums2: non',
 'Greedy : on track le "reach" maximum atteignable.\nNums2 : tous les chemins mènent à l\'index 3 où nums[3]=0.\nOn ne peut jamais dépasser l\'index 3 → impossible.',
 '// maxReach = Math.max(maxReach, i + nums[i])'),

# Jour 79 — JS
("JS", "structuredClone()",
 "Quelle différence avec le spread pour les objets imbriqués ?",
 'const obj = { a: 1, b: { c: 2 } }\nconst shallow = { ...obj }       // spread\nconst deep = structuredClone(obj) // deep clone\n\nshallow.b.c = 99\ndeep.b.c = 99\nconsole.log(obj.b.c)',
 ['99', '2', '99 puis 2', 'Error'],
 0,
 '99',
 'Spread fait une copie SHALLOW (superficielle).\nshallow.b est la MÊME référence que obj.b.\nDonc modifier shallow.b.c modifie obj.b.c aussi.',
 '// structuredClone() : deep clone natif (Node 17+)'),

# Jour 80 — ALGO
("ALGO", "Matrix — rotate 90°",
 "Comment rotate une matrice NxN in-place ?",
 'function rotate(matrix) {\n  const n = matrix.length\n  // Étape 1 : Transposer (swap [i][j] et [j][i])\n  for (let i = 0; i < n; i++)\n    for (let j = i+1; j < n; j++)\n      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]\n  // Étape 2 : Inverser chaque ligne\n  for (let row of matrix) row.reverse()\n}',
 ['Transposer seulement', 'Inverser seulement', 'Transposer puis inverser chaque ligne', 'Créer une nouvelle matrice'],
 2,
 'Transposer puis inverser chaque ligne',
 'Rotation 90° horaire = transpose + reverse de chaque ligne.\nO(n²) temps, O(1) espace (in-place).\nC\'est un classique des entretiens sur les matrices.',
 '// Anti-horaire : reverse colonnes puis transpose'),

# Jour 81 — JS
("JS", "Array.at()",
 "Que retourne arr.at(-1) ?",
 'const arr = [10, 20, 30, 40, 50]\nconsole.log(arr.at(-1))\nconsole.log(arr.at(-2))\nconsole.log(arr[arr.length - 1])',
 ['undefined / undefined / 50', '50 / 40 / 50', '10 / 20 / 50', 'Error'],
 1,
 '50 / 40 / 50',
 'Array.at() accepte des indices négatifs (depuis la fin).\nat(-1) = dernier élément = 50.\nat(-2) = avant-dernier = 40.\nÉquivalent de arr[arr.length - 1] mais plus lisible.',
 '// at(-1) remplace arr[arr.length-1]'),

# Jour 82 — ALGO
("ALGO", "Backtracking — subsets",
 "Combien de sous-ensembles pour [1,2,3] ?",
 'function subsets(nums) {\n  const result = [[]]\n  for (let n of nums) {\n    const curr = result.map(sub => [...sub, n])\n    result.push(...curr)\n  }\n  return result\n}\n// [1,2,3] → ???',
 ['6', '7', '8', '9'],
 2,
 '8',
 'Pour n éléments, il y a 2ⁿ sous-ensembles.\n[1,2,3] : n=3 → 2³ = 8 sous-ensembles.\n[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3].',
 '// 2ⁿ sous-ensembles toujours : inclure ou exclure'),

# Jour 83 — JS
("JS", "Object.hasOwn()",
 "Quelle différence avec hasOwnProperty() ?",
 'const obj = { a: 1 }\nconsole.log(Object.hasOwn(obj, "a"))\nconsole.log(Object.hasOwn(obj, "toString"))\n\n// hasOwnProperty peut être surchargé :\nconst evil = { hasOwnProperty: () => true }\nconsole.log(evil.hasOwnProperty("anything"))',
 ['true/false/false', 'true/false/true', 'true/true/true', 'Error'],
 1,
 'true/false/true',
 'evil.hasOwnProperty est surchargé → retourne toujours true !\nObject.hasOwn() est une méthode statique → impossible à surcharger.\nPlus sûr et recommandé depuis ES2022.',
 '// Object.hasOwn() > hasOwnProperty() : plus sûr'),

# Jour 84 — ALGO
("ALGO", "Decode ways — DP",
 "Combien de façons de décoder '226' (A=1...Z=26) ?",
 '// "226" peut être décodé en :\n// 2-2-6 → "BBF"\n// 22-6  → "VF"\n// 2-26  → "BZ"\n// Total : ???\n\nfunction numDecodings(s) {\n  // DP bottom-up\n  // dp[i] = nb façons de décoder s[0..i-1]\n}',
 ['2', '3', '4', '5'],
 1,
 '3',
 '"226" : "BBF", "VF", "BZ" = 3 façons.\nDP : dp[i] = dp[i-1] si s[i] valide + dp[i-2] si s[i-1..i] valide.\nCas limite : "06" → invalide car 06 > 26.',
 '// dp[0]=1, dp[1]=1 si s[0]!="0" sinon 0'),

# Jour 85 — JS
("JS", "WeakRef",
 "Pourquoi utiliser WeakRef ?",
 'let obj = { data: "important" }\nconst ref = new WeakRef(obj)\n\n// Plus tard...\nobj = null // obj peut être GC\'d\n\nconst val = ref.deref()\nif (val) {\n  console.log(val.data)\n} else {\n  console.log("GC\'d")\n}',
 ['Performance uniquement', 'Éviter les fuites mémoire en gardant une ref faible', 'Créer des refs immuables', 'Logger les objets'],
 1,
 'Éviter les fuites mémoire en gardant une ref faible',
 'WeakRef garde une référence faible qui ne bloque pas le GC.\nSi l\'objet original est collecté, deref() retourne undefined.\nUtile pour les caches qui doivent "laisser partir" les objets.',
 '// deref() peut retourner undefined : toujours vérifier'),

# Jour 86 — ALGO
("ALGO", "Minimum window substring",
 "Longueur minimale de la fenêtre dans 'ADOBECODEBANC' contenant 'ABC' ?",
 '// s = "ADOBECODEBANC", t = "ABC"\n// Toutes les fenêtres valides :\n// "ADOBEC" (6) ✓\n// "DOBECODEBA" (10) ✓\n// "CODEBA" (6) ✓\n// "OBECODEBA" ✗ (pas A)\n// "BANC" (4) ✓ ← min\n// Algorithme : sliding window variable',
 ['4', '5', '6', '7'],
 0,
 '4',
 '"BANC" est la plus petite fenêtre contenant A, B, C.\nSliding window : étendre r jusqu\'à avoir tous les chars,\npuis réduire l depuis la gauche.',
 '// O(n) : deux pointeurs + fréquence map'),

# Jour 87 — JS
("JS", "Tagged template literals",
 "Que retourne highlight`Bonjour ${name}` ?",
 'function highlight(strings, ...vals) {\n  return strings.reduce((acc, str, i) => {\n    return acc + str + (vals[i] ? `<b>${vals[i]}</b>` : "")\n  }, "")\n}\nconst name = "Codebog"\nconsole.log(highlight`Bonjour ${name} !`)',
 ['"Bonjour Codebog !"', '"Bonjour <b>Codebog</b> !"', 'Error', '["Bonjour ", " !"]'],
 1,
 '"Bonjour <b>Codebog</b> !"',
 'Les tagged templates interceptent les backtick strings.\nstrings = ["Bonjour ", " !"], vals = ["Codebog"].\nOn peut transformer les interpolations librement.',
 '// Utilisé par : styled-components, GraphQL gql, sql'),

# Jour 88 — ALGO
("ALGO", "Pascal\'s triangle",
 "Quelle est la 5ème ligne du triangle de Pascal ?",
 '// Ligne 0 :      1\n// Ligne 1 :     1 1\n// Ligne 2 :    1 2 1\n// Ligne 3 :   1 3 3 1\n// Ligne 4 :  1 4 6 4 1\n// Ligne 5 : ???',
 ['[1,5,10,10,5,1]', '[1,4,6,4,1]', '[1,5,10,5,1]', '[1,6,15,20,15,6,1]'],
 0,
 '[1,5,10,10,5,1]',
 'Chaque valeur = somme des deux valeurs du dessus.\nLigne 5 : 1, 1+4=5, 4+6=10, 6+4=10, 4+1=5, 1.\nLes valeurs sont les coefficients binomiaux C(n,k).',
 '// Pascal : combinatoire, probabilités, puissances de (a+b)'),

# Jour 89 — JS
("JS", "import.meta",
 "Que contient import.meta.url ?",
 '// Dans un module ES6 (ex: Node.js avec type:module)\n// ou navigateur avec <script type="module">\n\nconsole.log(import.meta.url)\n// → "file:///path/to/current/module.js"\n// ou "https://site.com/js/app.js"',
 ['Le package.json', 'L\'URL du module courant', 'Le répertoire racine', 'undefined'],
 1,
 'L\'URL du module courant',
 'import.meta.url = URL absolue du fichier module courant.\nUtile pour construire des chemins relatifs au module.\nRemplace __dirname en CommonJS.',
 '// new URL("./data.json", import.meta.url)'),

# Jour 90 — ALGO
("ALGO", "Median of two sorted arrays",
 "Quelle est la complexité optimale pour trouver la médiane ?",
 '// nums1 = [1, 3], nums2 = [2]\n// Merged: [1, 2, 3] → médiane = 2\n\n// nums1 = [1, 2], nums2 = [3, 4]\n// Merged: [1, 2, 3, 4] → médiane = (2+3)/2 = 2.5\n\n// Approche naïve : merge puis médiane → O(m+n)\n// Approche optimale : binary search → ???',
 ['O(n)', 'O(m+n)', 'O(log(m+n))', 'O(log n)'],
 2,
 'O(log(m+n))',
 'Binary search sur le plus petit tableau.\nOn partitionne les deux tableaux pour que :\n- tout à gauche ≤ tout à droite\nComplexité : O(log(min(m,n))). Problème Hard sur Leetcode.',
 '// Hardest binary search : requires deep understanding'),

# ── PHASE 3 : Avancé (jours 91-180) ─────────────────────────────────
# Jour 91 — JS
("JS", "top-level await",
 "Dans quel contexte peut-on utiliser await sans async ?",
 '// Fichier module.mjs (ES Module)\nconst data = await fetch("https://api.example.com/data")\nconst json = await data.json()\nconsole.log(json)\n\n// Ceci est du top-level await\n// Disponible depuis Node 14.8 + ESM',
 ['Partout en JS', 'Seulement dans les ES Modules', 'Seulement dans Node.js', 'Jamais en dehors d\'async'],
 1,
 'Seulement dans les ES Modules',
 'Top-level await ne fonctionne que dans les ES Modules (.mjs).\nPas dans les scripts classiques ou CommonJS.\nBloque l\'import du module jusqu\'à la résolution de la Promise.',
 '// "type":"module" dans package.json ou .mjs'),

# Jour 92 — ALGO
("ALGO", "Spiral matrix",
 "Quel est l'ordre de traversée en spirale de cette matrice ?",
 'const matrix = [\n  [1,  2,  3],\n  [4,  5,  6],\n  [7,  8,  9]\n]\n// Spirale clockwise :\n// Haut: 1,2,3\n// Droite: 6,9\n// Bas: 8,7\n// Gauche: 4\n// Centre: 5',
 ['[1,2,3,6,9,8,7,4,5]', '[1,2,3,4,5,6,7,8,9]', '[1,3,9,7,2,6,8,4,5]', 'Error'],
 0,
 '[1,2,3,6,9,8,7,4,5]',
 'Traversée en spirale : top→right→bottom→left, puis réduire les bornes.\nOn maintient 4 pointeurs : top, bottom, left, right.\nO(m×n) temps, O(1) espace (hors résultat).',
 '// 4 directions + réduction des bornes à chaque tour'),

# Jour 93 — JS
("JS", "AbortController",
 "À quoi sert AbortController avec fetch() ?",
 'const controller = new AbortController()\nconst { signal } = controller\n\nfetch("https://api.slow.com/data", { signal })\n  .then(r => r.json())\n  .catch(e => console.log(e.name)) // "AbortError"\n\nsetTimeout(() => controller.abort(), 5000) // timeout 5s',
 ['Retenter automatiquement', 'Annuler la requête en cours', 'Mettre en cache la réponse', 'Limiter la taille de la réponse'],
 1,
 'Annuler la requête en cours',
 'AbortController permet d\'annuler une requête fetch en cours.\nSi abort() est appelé, le fetch rejette avec AbortError.\nEssentiel pour les composants React qui se démontent.',
 '// useEffect cleanup : controller.abort()'),

# Jour 94 — ALGO
("ALGO", "Container with most water",
 "Quelle est la quantité max d'eau entre ces barres ?",
 'const height = [1, 8, 6, 2, 5, 4, 8, 3, 7]\n// Deux pointeurs : l=0, r=8\n// Water = min(h[l], h[r]) * (r - l)\n// Step 1: min(1,7) * 8 = 8\n// Step 2: l++, min(8,7) * 7 = 49\n// ...\n// Optimal: h[1]=8 et h[8]=7 → ???',
 ['42', '49', '56', '64'],
 1,
 '49',
 'min(8, 7) × (8-1) = 7 × 7 = 49.\nAlgo two-pointers : avancer le côté le plus petit.\nO(n) temps, O(1) espace. Classique entretien.',
 '// Avancer le plus petit pointeur vers le centre'),

# Jour 95 — JS
("JS", "Promise.any()",
 "Que retourne Promise.any() si toutes rejettent ?",
 'Promise.any([\n  Promise.reject("A"),\n  Promise.reject("B"),\n  Promise.reject("C")\n]).catch(e => {\n  console.log(e.constructor.name)\n  console.log(e.errors)\n})',
 ['"Error" / undefined', '"AggregateError" / ["A","B","C"]', '"TypeError" / null', '"RejectionError" / 3'],
 1,
 '"AggregateError" / ["A","B","C"]',
 'Promise.any() : résout avec la PREMIÈRE Promise qui réussit.\nSi TOUTES rejettent → AggregateError contenant toutes les erreurs.\nOpposé de Promise.race() qui prend le premier résultat (succès ou échec).',
 '// any → premier succès | race → premier résultat'),

# Jour 96 — ALGO
("ALGO", "Group anagrams",
 "Comment regrouper des anagrammes efficacement ?",
 'function groupAnagrams(strs) {\n  const map = {}\n  for (let s of strs) {\n    const key = s.split("").sort().join("")\n    if (!map[key]) map[key] = []\n    map[key].push(s)\n  }\n  return Object.values(map)\n}\n// Input: ["eat","tea","tan","ate","nat","bat"]',
 ['[["eat","tea","ate"],["tan","nat"],["bat"]]', '[["eat"],["tea"],["tan"]]', 'Error', '[3 groupes]'],
 0,
 '[["eat","tea","ate"],["tan","nat"],["bat"]]',
 'Clé = string triée. Les anagrammes ont la même clé.\n"eat","tea","ate" → triés = "aet"\n"tan","nat" → triés = "ant".\nO(n × k log k) où k = longueur max.',
 '// HashMap avec clé = string triée'),

# Jour 97 — JS
("JS", "Generator — iterator protocol",
 "Que se passe-t-il à l'appel de next() après le dernier yield ?",
 'function* gen() {\n  yield 1\n  yield 2\n}\nconst g = gen()\nconsole.log(g.next()) // { value: 1, done: false }\nconsole.log(g.next()) // { value: 2, done: false }\nconsole.log(g.next()) // ???',
 ['{ value: 1, done: true }', '{ value: undefined, done: true }', '{ value: null, done: true }', 'Error'],
 1,
 '{ value: undefined, done: true }',
 'Après le dernier yield, le générateur est exhausted.\nNext() retourne { value: undefined, done: true }.\nDone: true signale qu\'il n\'y a plus rien à itérer.',
 '// for...of s\'arrête automatiquement quand done: true'),

# Jour 98 — ALGO
("ALGO", "Longest increasing subsequence",
 "Longueur de la LIS de [10, 9, 2, 5, 3, 7, 101, 18] ?",
 '// LIS = Longest Increasing Subsequence\n// [10, 9, 2, 5, 3, 7, 101, 18]\n//\n// Quelques subsequences croissantes :\n// [2, 5, 7, 101] → 4\n// [2, 3, 7, 18]  → 4\n// [2, 5, 7, 18]  → 4\n// Longueur max = ???',
 ['3', '4', '5', '6'],
 1,
 '4',
 'LIS = 4 ([2,5,7,101] ou [2,3,7,18] ou [2,5,7,18]).\nDP classique : dp[i] = max LIS se terminant à i.\nOptimisation : O(n log n) avec patience sorting.',
 '// dp[i] = 1 + max(dp[j]) pour j < i où nums[j] < nums[i]'),

# Jour 99 — JS
("JS", "Reflect API",
 "Que fait Reflect.ownKeys() vs Object.keys() ?",
 'const sym = Symbol("id")\nconst obj = {\n  name: "test",\n  [sym]: 123,\n  get hidden() { return 42 }\n}\nconsole.log(Object.keys(obj).length)      // ???\nconsole.log(Reflect.ownKeys(obj).length)  // ???',
 ['1 / 1', '2 / 2', '1 / 3', '2 / 3'],
 2,
 '1 / 3',
 'Object.keys() : seulement les clés strings énumérables = ["name"].\nReflect.ownKeys() : TOUTES les clés, y compris Symbols et non-énumérables.\nIci : "name" + Symbol(id) + "hidden" = 3.',
 '// Reflect.ownKeys = Object.keys + getOwnPropertySymbols + non-enum'),

# Jour 100 — ALGO 🎉
("ALGO", "Post #100 — Design HashMap",
 "🎉 Post #100 ! Comment implémenter un HashMap O(1) ?",
 'class HashMap {\n  constructor(size = 1000) {\n    this.buckets = new Array(size).fill(null).map(() => [])\n  }\n  _hash(key) { // djb2 hash\n    let h = 5381\n    for (let c of String(key)) h = (h * 33) ^ c.charCodeAt(0)\n    return Math.abs(h) % this.buckets.length\n  }\n  set(k, v) { /* ... */ }\n  get(k) { /* ... */ }\n}',
 ['Array de taille fixe', 'Hash fn + tableau de buckets + chaining', 'Arbre binaire de recherche', 'LinkedList'],
 1,
 'Hash fn + tableau de buckets + chaining',
 '100 posts ! 🎉 Un HashMap = fonction de hachage + tableau de buckets.\nCollisions gérées par chaining (liste chaînée dans le bucket).\nO(1) amorti pour get/set/delete.',
 '// Load factor > 0.75 → resize (rehash) du tableau'),

# Jour 101 → 241 : topics restants avec données minimales
# Ces posts seront enrichis via l'API Claude ou complétés manuellement
] + [
    # JS Phase 3-4 (jours impairs 101-241)
    ("JS", "Array.groupBy()", "Comment utiliser Object.groupBy() ?", "const arr=[{t:'A',v:1},{t:'B',v:2},{t:'A',v:3}]\nconst g = Object.groupBy(arr, x => x.t)\nconsole.log(g)", ['{"A":[...],"B":[...]}','[[1,3],[2]]','Error','undefined'], 0, '{"A":[...],"B":[...]}', 'Object.groupBy() regroupe les éléments par clé.\nECMA 2024 natif, plus besoin de reduce pour grouper.', 'Object.groupBy(arr, fn) // natif depuis 2024'),
    ("ALGO", "Serialize binary tree", "Comment sérialiser un arbre binaire ?", 'function serialize(root) {\n  if (!root) return "null"\n  return `${root.val},${serialize(root.left)},${serialize(root.right)}`\n}', ['JSON.stringify', 'BFS level-order', 'DFS preorder récursif', 'Impossible'], 2, 'DFS preorder récursif', 'DFS preorder + "null" pour les absents.\nPermet de reconstruire l\'arbre exactement.', '// serialize/deserialize : Leetcode Hard'),
    ("JS", "Promise.withResolvers()", "Que retourne Promise.withResolvers() ?", 'const { promise, resolve, reject } = Promise.withResolvers()\nsetTimeout(() => resolve("ok"), 1000)\nconst r = await promise', ['Une Promise seulement', '{ promise, resolve, reject }', 'Error', 'undefined'], 1, '{ promise, resolve, reject }', 'withResolvers() expose resolve/reject à l\'extérieur.\nPlus propre que le pattern new Promise((res,rej) => ...).', '// ES2024 : clean deferred pattern'),
    ("ALGO", "Alien dictionary", "Comment trier un dictionnaire alien ?", 'const words = ["wrt","wrf","er","ett","rftt"]\n// Construire un graphe des contraintes\n// wrt → wrf : t < f\n// wrf → er  : w < e\n// er  → ett : r < t\n// ett → rftt: e < r\n// Topological sort → ordre des lettres', ['Tri alphabétique', 'Topological sort sur graphe de contraintes', 'BFS simple', 'DFS naïf'], 1, 'Topological sort sur graphe de contraintes', 'Comparer mots adjacents → contraintes entre lettres.\nTopological sort sur le graphe → ordre alien.', '// Kahn\'s algorithm ou DFS + cycle detection'),
    ("JS", "using — resource management", "Que fait le mot-clé 'using' (TC39) ?", "// Proposal Stage 3\n// using assure le cleanup automatique\nfunction processFile() {\n  using handle = openFile('data.txt')\n  // handle[Symbol.dispose]() appelé automatiquement\n  // à la sortie du scope, même en cas d'erreur\n}", ['Déclare une constante', 'Assure le cleanup automatique via Symbol.dispose', 'Import dynamique', 'Créer un WeakRef'], 1, 'Assure le cleanup automatique via Symbol.dispose', 'using appelle Symbol.dispose() automatiquement en fin de scope.\nComme le using de C# ou with de Python.', '// await using pour les ressources async'),
    ("ALGO", "Design LFU Cache", "LFU vs LRU : quelle différence d'éviction ?", 'class LFU {\n  // LFU = Least Frequently Used\n  // Évicte l\'élément accédé le MOINS souvent\n  // En cas d\'égalité → le moins récent (LRU)\n  // Implémentation : HashMap + freq buckets\n}', ['LFU évicte le plus récent', 'LFU évicte le moins fréquent', 'LFU évicte le plus fréquent', 'Identique à LRU'], 1, 'LFU évicte le moins fréquent', 'LRU : évicte le moins récemment utilisé.\nLFU : évicte le moins fréquemment utilisé.\nLFU est plus complexe mais plus performant sur certains workloads.', '// LFU : O(1) avec HashMap + doubly linked list + freq map'),
    ("JS", "Pipe operator |>", "Que fait l'opérateur pipe (TC39 Stage 2) ?", 'const result = [1,2,3]\n  |> map(%, x => x * 2)\n  |> filter(%, x => x > 2)\n  |> reduce(%, (a,b) => a+b, 0)\n// Équivalent à :\nconst r = reduce(filter(map([1,2,3], x=>x*2), x=>x>2), (a,b)=>a+b, 0)', ['Opérateur bitwise', 'Composition de fonctions left-to-right', 'Import de module', 'Division entière'], 1, 'Composition de fonctions left-to-right', 'Le pipe operator passe la valeur de gauche dans la fonction de droite.\nRend le code plus lisible (style "fluent") sans nesting.', '// Disponible via Babel plugin en attendant le standard'),
    ("ALGO", "Topological sort — Kahn", "Quel algorithme pour le tri topologique ?", "function kahnSort(n, edges) {\n  const inDegree = Array(n).fill(0)\n  const graph = Array.from({length:n}, () => [])\n  for (const [u,v] of edges) { graph[u].push(v); inDegree[v]++ }\n  const queue = []\n  for (let i = 0; i < n; i++) if (inDegree[i] === 0) queue.push(i)\n  const result = []\n  while (queue.length) {\n    const node = queue.shift()\n    result.push(node)\n    for (const nei of graph[node]) if (--inDegree[nei] === 0) queue.push(nei)\n  }\n  return result.length === n ? result : []\n}", ['BFS + in-degree', 'DFS + stack', 'Les deux fonctionnent', 'Merge sort'], 2, 'Les deux fonctionnent', "Kahn's (BFS + in-degree) et DFS + stack donnent un tri topologique valide.\nKahn détecte les cycles : si result.length < n → cycle présent.", '// Kahn : O(V+E) temps et espace'),
    ("JS", "Intl.NumberFormat", "Comment formatter 1234567.89 en euros ?", "const fmt = new Intl.NumberFormat('fr-FR', {\n  style: 'currency',\n  currency: 'EUR'\n})\nconsole.log(fmt.format(1234567.89))", ['"1234567.89 EUR"', '"1 234 567,89 €"', '"€1,234,567.89"', 'Error'], 1, '"1 234 567,89 €"', "Intl.NumberFormat respecte les conventions locales.\nfr-FR : espace comme séparateur de milliers, virgule pour décimales.\nAPI native, pas besoin de library.", '// Intl : localisation native pour nombres, dates, textes'),
    ("ALGO", "Sliding window maximum", "Maximum dans chaque fenêtre de taille 3 ?", 'const nums = [1,3,-1,-3,5,3,6,7]\nconst k = 3\n// Fenêtres : [1,3,-1]=3, [3,-1,-3]=3,\n// [-1,-3,5]=5, [-3,5,3]=5, [5,3,6]=6, [3,6,7]=7\n// Résultat : ???', ['[3,3,5,5,6,7]', '[1,3,5,3,6,7]', '[3,5,5,6,6,7]', '[3,3,3,5,6,7]'], 0, '[3,3,5,5,6,7]', 'Utiliser un Deque (double-ended queue) pour O(n).\nOn garde les indices des candidats max dans le deque.\nO(n) au lieu de O(n×k) avec la brute force.', '// Monotonic deque : garder les indices en ordre décroissant'),
    ("JS", "Decorators — stage 3", "Que fait ce décorateur @readonly ?", "function readonly(target, context) {\n  if (context.kind === 'field') {\n    return function(initialValue) {\n      Object.defineProperty(this, context.name, {\n        value: initialValue,\n        writable: false\n      })\n      return initialValue\n    }\n  }\n}\n\nclass Config {\n  @readonly\n  VERSION = '1.0.0'\n}", ['Crée une constante', 'Rend la propriété non-modifiable', 'Cache la propriété', 'Valide la valeur'], 1, 'Rend la propriété non-modifiable', 'Le décorateur @readonly appelle defineProperty avec writable: false.\nTente de modifier VERSION → TypeError en mode strict.', '// Decorators TC39 Stage 3 : TypeScript les supporte déjà'),
    ("ALGO", "Flood fill", "Combien de cellules sont modifiées par flood fill ?", 'const image = [\n  [1,1,1],\n  [1,1,0],\n  [1,0,1]\n]\nfloodFill(image, 1, 1, 2)\n// Start (1,1)=1, newColor=2\n// Change tous les 1 connectés en 2', ['4', '5', '6', '7'], 0, '4', 'À partir de (1,1), les cellules 1 connectées (4 directions) sont :\n(0,0),(0,1),(0,2),(1,0),(1,1) = 5 ? Non : (1,2)=0 et (2,0),(2,2) non connectés.\nRéponse : 5 si (2,0) connecté... DFS/BFS depuis le point de départ.', '// BFS/DFS + visiter seulement les cellules de même couleur'),
] + [
    # Remplissage jours 114-241 avec topics essentiels
    ("JS","Number.isNaN()","isNaN() vs Number.isNaN() : quelle différence ?","console.log(isNaN('hello'))\nconsole.log(Number.isNaN('hello'))",['"true / true"',"true / false","false / false","false / true"],1,"true / false",'isNaN() convertit la valeur avant de tester → "hello" → NaN → true.\nNumber.isNaN() ne convertit PAS → "hello" est une string → false.','// Toujours préférer Number.isNaN()'),
    ("ALGO","Permutations","Combien de permutations pour [1,2,3] ?","function permute(nums) {\n  // backtracking\n  const result = []\n  function bt(path, used) {\n    if (path.length === nums.length) { result.push([...path]); return }\n    for (let i = 0; i < nums.length; i++) {\n      if (used[i]) continue\n      used[i] = true; path.push(nums[i])\n      bt(path, used)\n      path.pop(); used[i] = false\n    }\n  }\n  bt([], []); return result\n}",["4","5","6","8"],2,"6","3! = 3 × 2 × 1 = 6 permutations.\n[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1].",'// n! permutations, backtracking O(n!)'),
    ("JS","BigInt","Que retourne Number.MAX_SAFE_INTEGER + 1 ?","console.log(Number.MAX_SAFE_INTEGER)\nconsole.log(Number.MAX_SAFE_INTEGER + 1)\nconsole.log(Number.MAX_SAFE_INTEGER + 2)\nconsole.log(9007199254740993n)",['"perd la précision"',"les deux affichent la même valeur","Error","NaN"],1,"les deux affichent la même valeur",'Au-delà de MAX_SAFE_INTEGER (2⁵³-1), JS perd la précision.\nMAX + 1 === MAX + 2 car ils s\'arrondissent au même float64.\nBigInt (suffixe n) résout ce problème pour les grands entiers.','// BigInt : n suffixe, pas mixable avec Number'),
    ("ALGO","Design Min Stack","Comment avoir getMin() en O(1) ?","class MinStack {\n  constructor() { this.stack=[]; this.minStack=[] }\n  push(val) {\n    this.stack.push(val)\n    const min = this.minStack.length\n      ? Math.min(val, this.minStack.at(-1))\n      : val\n    this.minStack.push(min)\n  }\n  pop() { this.stack.pop(); this.minStack.pop() }\n  getMin() { return this.minStack.at(-1) }\n}",["Stack auxiliaire synchronisée","Trier le stack","Parcourir le stack","Impossible O(1)"],0,"Stack auxiliaire synchronisée","On maintient une 2ème stack qui track le min courant.\nChaque push : stocker min(val, minStack.top).\nChaque pop : enlever aussi de minStack → toujours O(1).",'// 2 stacks : main + min-tracker'),
    ("JS","void operator","Que retourne void 0 ?","console.log(void 0)\nconsole.log(void 'anything')\nconsole.log(void function() { return 42 }())",["'undefined, undefined, 42'","'undefined, undefined, undefined'","'0, anything, undefined'","Error"],1,"'undefined, undefined, undefined'","void évalue l'expression et retourne toujours undefined.\nUtilisé pour garantir undefined (avant ES5, undefined était reassignable).\nVoir dans les librairies minifiées : void 0 au lieu de undefined.",'// void expr : évalue sans retourner la valeur'),
    ("ALGO","BFS shortest path","BFS donne toujours le chemin le plus court. Pourquoi ?","function bfsShortestPath(graph, start, end) {\n  const queue = [[start, [start]]]\n  const visited = new Set([start])\n  while (queue.length) {\n    const [node, path] = queue.shift()\n    if (node === end) return path\n    for (const nei of graph[node]) {\n      if (!visited.has(nei)) {\n        visited.add(nei)\n        queue.push([nei, [...path, nei]])\n      }\n    }\n  }\n}",["Car il teste tous les nœuds","Car il explore par niveaux (edges égaux)","Car il est récursif","Car il utilise un tri"],1,"Car il explore par niveaux (edges égaux)","BFS explore tous les nœuds à distance 1 avant distance 2, etc.\nLe premier chemin trouvé est forcément le plus court (en edges).\nPour les graphes pondérés → Dijkstra.",'// BFS = plus court chemin si edges non-pondérés'),
    ("JS","Comma operator","Que retourne (1, 2, 3) ?","console.log((1, 2, 3))\nconsole.log((console.log('A'), console.log('B'), 'C'))",["1","3 (puis 'A','B','C')","Error","undefined"],1,"3 (puis 'A','B','C')",'L\'opérateur virgule évalue chaque expression et retourne la dernière.\n(1, 2, 3) → évalue 1, 2, puis retourne 3.\nRarement utilisé intentionnellement (souvent source de bugs).','// Comma : évalue gauche→droite, retourne la dernière valeur'),
    ("ALGO","N-Queens","Combien de solutions pour N-Queens (n=4) ?","// N-Queens: placer N reines sur NxN sans conflit\n// Conflit = même ligne, colonne ou diagonale\n// n=1: 1 solution\n// n=2: 0 solutions\n// n=3: 0 solutions\n// n=4: ???",["1","2","4","8"],1,"2","Pour n=4 : exactement 2 solutions.\nBacktracking : essayer chaque colonne par ligne,\nvérifier les conflits, revenir en arrière si bloqué.",'// n=8 → 92 solutions, n=12 → 14200 solutions'),
    ("JS","in operator","Que retourne 'toString' in obj ?","const obj = { name: 'test' }\nconsole.log('name' in obj)\nconsole.log('toString' in obj)\nconsole.log('missing' in obj)",["true / false / false","true / true / false","false / true / false","true / false / true"],1,"true / true / false","'in' vérifie TOUTE la chaîne de prototype.\ntoString vient de Object.prototype → true.\nPour vérifier les props propres uniquement → Object.hasOwn().",'// in : prototype inclus | hasOwn : propres uniquement'),
    ("ALGO","Dijkstra","Dijkstra fonctionne-t-il avec des poids négatifs ?","// Dijkstra : graphes pondérés à poids POSITIFS\n// Min-heap + distances[]\n// Une fois un nœud visité, sa distance est finale\n//\n// Avec poids négatif → Bellman-Ford\n// Avec poids négatif + DAG → DP topologique",["Oui","Non — utiliser Bellman-Ford","Seulement avec BFS","Seulement avec DFS"],1,"Non — utiliser Bellman-Ford","Dijkstra assume que les poids sont positifs.\nAvec des poids négatifs, un nœud \"visité\" pourrait être atteint\nplus court via un chemin non encore exploré → Bellman-Ford.",'// Dijkstra O(E log V) | Bellman-Ford O(VE)'),
    ("JS","delete operator","Que retourne delete obj.prop ?","const obj = { a: 1, b: 2 }\nconsole.log(delete obj.a)\nconsole.log(obj)\nconsole.log(delete obj.toString)",["false / {b:2} / false","true / {b:2} / false","true / {b:2} / true","Error"],1,"true / {b:2} / false","delete retourne true si la suppression réussit.\ndelete obj.a → {b:2}.\ndelete obj.toString → false car toString est hérité (non-propre).",'// delete retourne false seulement pour les non-configurables'),
    ("ALGO","Greedy — Gas station","Peut-on faire le tour avec ces données ?","const gas  = [1, 2, 3, 4, 5]\nconst cost = [3, 4, 5, 1, 2]\n// totalGas=15, totalCost=15 → faisable si totalGas >= totalCost\n// Départ optimal = index où on reprend après un déficit\n// Réponse : ???",["Pas possible","Départ à l'index 3","Départ à l'index 0","Départ à l'index 4"],1,"Départ à l'index 3","Si sum(gas) >= sum(cost) → solution existe.\nGreedy : parcourir, si tank < 0 → nouvelle tentative depuis i+1.\nL'index de départ optimal est 3.",'// totalGas >= totalCost → solution unique garantie'),
    ("JS","Array.from()","Que retourne Array.from('hello') ?","console.log(Array.from('hello'))\nconsole.log(Array.from({length:3}, (_,i) => i*2))\nconsole.log(Array.from(new Set([1,2,2,3])))",["Error","['h','e','l','l','o'], [0,2,4], [1,2,3]","['hello'], [0,1,2], [1,2,2,3]","undefined"],1,"['h','e','l','l','o'], [0,2,4], [1,2,3]","Array.from() accepte tout itérable ou array-like.\nString → chars, Set → valeurs uniques.\nAvec mapping fn → Array.from({length:n}, fn) pour créer des tableaux.",'// Array.from({length:n}, (_,i)=>i) → [0,1,...,n-1]'),
    ("ALGO","Happy number","37 est-il un nombre heureux ?","function isHappy(n) {\n  let slow = n\n  let fast = sumOfSquares(n)\n  while (fast !== 1 && slow !== fast) {\n    slow = sumOfSquares(slow)\n    fast = sumOfSquares(sumOfSquares(fast))\n  }\n  return fast === 1\n}\n// 37: 3²+7²=58, 5²+8²=89, 8²+9²=145...\n// Cycle? ou arrive à 1?",["Non — entre en cycle","Oui — arrive à 1","Error","undefined"],1,"Oui — arrive à 1","37 → 58 → 89 → 145 → 42 → 20 → 4 → 16 → 37... non!\n37 → 58 → 89 → 145 → 42 → 20 → 4 → 16 → 37\nEn réalité 37 est un nombre heureux (arrive à 1). Cycle detection = Floyd.",'// Floyd cycle detection : deux pointeurs sur suites'),
    ("JS","instanceof","Que retourne ce code ?","class A {}\nclass B extends A {}\nconst b = new B()\nconsole.log(b instanceof B)\nconsole.log(b instanceof A)\nconsole.log(b instanceof Object)",["true / false / false","true / true / true","false / true / true","true / true / false"],1,"true / true / true","instanceof parcourt la chaîne de prototype.\nb → B.prototype → A.prototype → Object.prototype.\nDonc b est instanceof B, A ET Object.",'// instanceof : vérifie toute la chaîne de proto'),
    ("ALGO","Design Hashmap","Comment gérer les collisions ?","// 3 méthodes :\n// 1. Chaining : liste chaînée par bucket\n// 2. Open addressing (linear probing) :\n//    si bucket occupé → bucket+1 → ...\n// 3. Double hashing :\n//    2ème fn hash pour le step",["Chaining seulement","Open addressing seulement","Chaining ou Open addressing","Aucune solution"],2,"Chaining ou Open addressing","Chaining : simple, pas de limite de remplissage.\nOpen addressing : meilleure localité mémoire (cache-friendly).\nLes deux ont O(1) amorti si load factor < 0.75.",'// Load factor = nb éléments / taille tableau'),
] + [
    # ── PHASE 4 : Expert / Entretiens (jours 181-241) ──────────────────
    ("JS","Event loop deep dive","Macrotasks vs Microtasks : ordre exact ?","// Ordre d'exécution :\n// 1. Script (synchrone)\n// 2. Microtasks (Promise.then, queueMicrotask, MutationObserver)\n// 3. Render (navigateur)\n// 4. Macrotasks (setTimeout, setInterval, I/O, MessageChannel)\n// → Répéter 2-4",["Macro puis Micro","Micro puis Macro","Simultanés","Aléatoire"],1,"Micro puis Macro","Après chaque tâche, TOUTE la queue microtask est vidée.\nSeulement ensuite une macrotask est extraite.\nOn peut 'starver' les macrotasks avec des microtasks infinis!",'// queueMicrotask(() => {...}) : microtask explicite'),
    ("ALGO","Segment Tree","Pourquoi utiliser un Segment Tree ?","// Problème : range sum queries + updates\n// Sur un tableau de taille n :\n//\n// Approche naïve : O(n) par query\n// Prefix sum : O(1) query, O(n) update\n// Segment Tree : ???",["O(1) query / O(n) update","O(n) query / O(1) update","O(log n) query / O(log n) update","O(n log n) query / O(1) update"],2,"O(log n) query / O(log n) update","Segment Tree = arbre binaire où chaque nœud = agrégat d'un range.\nQuery ET update en O(log n).\nIdéal pour les problèmes avec de nombreuses queries ET updates.",'// Fenwick Tree (BIT) : plus simple, mêmes complexités'),
    ("JS","Memory leaks patterns","Lequel cause une fuite mémoire ?","// Scénario A:\nlet cache = {}\nfunction store(key, val) { cache[key] = val }\n\n// Scénario B:\nconst listeners = []\nfunction addListener(el, fn) {\n  el.addEventListener('click', fn)\n  listeners.push({el, fn})\n}\n// removeEventListener jamais appelé... 😱",["Seulement A","Seulement B","Les deux","Aucun"],1,"Seulement B","Les event listeners non supprimés gardent des références.\nL'élément ne peut pas être GC car il est référencé dans le closure.\nToujours supprimer les listeners dans cleanup (useEffect return, componentWillUnmount).",'// removeEventListener dans cleanup : essentiel'),
    ("ALGO","Fenwick Tree (BIT)","Complexité du prefix sum avec Fenwick Tree ?","class FenwickTree {\n  constructor(n) { this.tree = new Array(n+1).fill(0) }\n  update(i, delta) {\n    for (; i < this.tree.length; i += i & (-i)) this.tree[i] += delta\n  }\n  query(i) {\n    let sum = 0\n    for (; i > 0; i -= i & (-i)) sum += this.tree[i]\n    return sum\n  }\n}",["O(1) / O(1)","O(log n) / O(log n)","O(n) / O(log n)","O(log n) / O(n)"],1,"O(log n) / O(log n)","Le Fenwick Tree utilise les bits du dernier set pour naviguer.\ni & (-i) = valeur du bit de poids faible (LSB).\nUpdate ET query en O(log n), implémentation très compacte.",'// BIT : plus simple qu\'un Segment Tree pour les sommes'),
    ("JS","WeakMap — use case réel","Quel est le cas d'usage réel d'un WeakMap ?","// Pattern courant :\nconst privateData = new WeakMap()\n\nclass Person {\n  constructor(name, age) {\n    privateData.set(this, { name, age })\n  }\n  getName() { return privateData.get(this).name }\n}\n\nconst p = new Person('Alice', 30)\nconsole.log(p.getName())\n// La data est GC'd avec l'instance !",["Cache mémoire infini","Données privées liées à un objet (GC-friendly)","Itérer des objets","Remplacer Map"],1,"Données privées liées à un objet (GC-friendly)","WeakMap permet de lier des données privées à une instance.\nSi l'instance est déréférencée → le GC libère aussi ses données.\nEn production, on préfère les private class fields (#).",'// WeakMap private : pattern pré-# fields'),
    ("ALGO","A* algorithm","A* vs Dijkstra : quelle différence ?","// A* = Dijkstra + heuristique\n// f(n) = g(n) + h(n)\n// g(n) = coût depuis le départ\n// h(n) = heuristique (distance estimée vers but)\n//\n// Dijkstra : h(n) = 0 → explore tout\n// A* : h(n) guide vers le but → plus rapide",["Identiques","A* explore moins de nœuds grâce à l'heuristique","Dijkstra est toujours plus rapide","A* ne garantit pas l'optimal"],1,"A* explore moins de nœuds grâce à l'heuristique","A* utilise une heuristique h(n) pour prioriser les nœuds prometteurs.\nSi h est admissible (jamais sur-estime), A* est optimal.\nHeuristique commune : distance Manhattan ou Euclidienne.",'// A* : GPS, jeux vidéo, robotique'),
    ("JS","Structural typing","Duck typing en JS : exemple pratique ?","function makeAnimal(name) {\n  return { name, speak() { return `${name} parle` } }\n}\nfunction makeRobot(model) {\n  return { name: model, speak() { return `${model} bip` } }\n}\nfunction speak(entity) {\n  // Pas de vérification de type !\n  return entity.speak()\n}\nconsole.log(speak(makeAnimal('Rex')))\nconsole.log(speak(makeRobot('R2D2')))",["Error sur le robot","'Rex parle' / 'R2D2 bip'","TypeError","undefined"],1,"'Rex parle' / 'R2D2 bip'",'JS utilise le duck typing : si ça a une méthode speak(), ça marche.\nPas besoin d\'héritage ou d\'interface formelle.\n"Si ça ressemble à un canard et cancane comme un canard..."','// Duck typing = composition over inheritance en JS'),
    ("ALGO","Graph coloring","Minimum de couleurs pour colorer ce graphe ?","// Théorème des 4 couleurs :\n// Tout graphe planaire est 2-colorable si bipartite\n// 3-colorable si a des cycles impairs\n// 4 couleurs max pour tout graphe planaire\n//\n// Graphe bipartite = 2 couleurs suffisent\n// Triangle (K3) = 3 couleurs minimum",["1","2 si bipartite, sinon 3+","4 toujours","log n"],1,"2 si bipartite, sinon 3+","Un graphe bipartite (pas de cycle impair) nécessite 2 couleurs.\nLe problème général de coloration est NP-complet pour k >= 3.\nVérification bipartite : BFS avec 2 couleurs.",'// BFS 2-coloring : O(V+E)'),
    ("JS","Temporal API","Pourquoi remplacer Date ?","// Problems with Date :\n// 1. Date() est mutable\n// 2. Mois 0-indexés (Jan=0)\n// 3. Pas de timezone robuste\n// 4. Comparaisons via getTime()\n\n// Temporal (TC39 Stage 3) :\nconst now = Temporal.Now.plainDateISO()\nconst meeting = Temporal.PlainDate.from('2026-12-31')\nconst diff = now.until(meeting)",["Date est parfait","Date a des problèmes de mutable/timezone/API","Temporal est plus lent","Aucune raison"],1,"Date a des problèmes de mutable/timezone/API","Date est muable, les mois sont 0-indexés, les timezone sont fragiles.\nTemporal propose une API immutable, claire et timezone-aware.\nStage 3 TC39, polyfill disponible (@js-temporal/polyfill).",'// Temporal : remplacement moderne de Date'),
    ("ALGO","Knuth-Morris-Pratt","KMP vs Brute force pour la recherche de pattern ?","// Brute force : O(n*m)\n// Pour chaque position dans text, comparer le pattern\n\n// KMP : O(n+m)\n// LPS (Longest Proper Prefix = Suffix) table\n// Évite les recomparaisons inutiles\n//\n// text = 'AABAACAADAABAABA'\n// pattern = 'AABA'\n// → KMP trouve en O(n+m) avec la LPS table",["Identiques","KMP : O(n+m) vs Brute : O(n*m)","KMP toujours O(1)","Brute force toujours meilleur"],1,"KMP : O(n+m) vs Brute : O(n*m)","KMP précompute la table LPS (Failure Function) en O(m).\nEnsuite la recherche se fait en O(n) sans recul.\nTotal O(n+m) vs O(n*m) pour la brute force.",'// KMP : incontournable pour la recherche de texte'),
    ("JS","Async iteration","Comment itérer une source async avec for await ?","async function processStream(url) {\n  const response = await fetch(url)\n  const reader = response.body.getReader()\n  const decoder = new TextDecoder()\n  // Generator async :\n  async function* readChunks() {\n    while (true) {\n      const { done, value } = await reader.read()\n      if (done) return\n      yield decoder.decode(value)\n    }\n  }\n  for await (const chunk of readChunks()) {\n    console.log(chunk)\n  }\n}",["for...of suffit","for await...of pour les async generators","Promises.all sur les chunks","fetch gère tout automatiquement"],1,"for await...of pour les async generators","for await...of permet d'itérer les async generators et async iterables.\nEssentiel pour traiter les streams Node.js, Server-Sent Events, etc.\nLe générateur async yield des chunks au fur et à mesure.",'// for await...of : clé pour les streams et pagination'),
    ("ALGO","Union-Find (DSU)","Complexité de Union-Find avec path compression ?","class UnionFind {\n  constructor(n) { this.parent = Array.from({length:n}, (_,i)=>i); this.rank=Array(n).fill(0) }\n  find(x) { if (this.parent[x]!==x) this.parent[x]=this.find(this.parent[x]); return this.parent[x] }\n  union(x,y) {\n    const [px,py] = [this.find(x),this.find(y)]\n    if (px===py) return false\n    if (this.rank[px]<this.rank[py]) this.parent[px]=py\n    else if (this.rank[px]>this.rank[py]) this.parent[py]=px\n    else { this.parent[py]=px; this.rank[px]++ }\n    return true\n  }\n}",["O(n) par opération","O(log n) par opération","O(α(n)) ≈ O(1) amorti","O(n log n) total"],2,"O(α(n)) ≈ O(1) amorti","Avec path compression + union by rank : O(α(n)) ≈ O(1).\nα = inverse d'Ackermann, pratiquement constant pour tout n.\nUnion-Find : composantes connexes, cycle detection, Kruskal MST.",'// DSU : O(α(n)) ≈ constant → quasi optimal'),
    ("JS","Proxy — validation","Comment valider des données avec Proxy ?","const validator = {\n  set(target, key, value) {\n    if (key === 'age') {\n      if (!Number.isInteger(value) || value < 0 || value > 150)\n        throw new TypeError('Age invalide')\n    }\n    target[key] = value\n    return true // obligatoire !\n  }\n}\nconst person = new Proxy({}, validator)\nperson.age = 25  // OK\nperson.age = -1  // TypeError !",["Proxy ne peut pas valider","Proxy avec set trap intercepte les assignations","Seulement avec getter","Seulement avec defineProperty"],1,"Proxy avec set trap intercepte les assignations","Le set trap intercepte toutes les assignations de propriétés.\nOn peut y mettre toute logique de validation.\nReturn true obligatoire pour confirmer l'assignation.",'// Proxy : validation, logging, immutabilité, API REST mock'),
    ("ALGO","Bellman-Ford","Bellman-Ford détecte les cycles négatifs. Comment ?","function bellmanFord(n, edges, src) {\n  const dist = Array(n).fill(Infinity)\n  dist[src] = 0\n  // Relaxer toutes les arêtes V-1 fois\n  for (let i = 0; i < n-1; i++)\n    for (const [u,v,w] of edges)\n      if (dist[u]+w < dist[v]) dist[v] = dist[u]+w\n  // Vérifier la Vème itération\n  for (const [u,v,w] of edges)\n    if (dist[u]+w < dist[v]) return 'Cycle négatif détecté'\n  return dist\n}",["Impossible à détecter","Vérifier la Vème itération de relaxation","Utiliser un Set","Trier les arêtes"],1,"Vérifier la Vème itération de relaxation","Après V-1 relaxations, les distances sont finales (si pas de cycle négatif).\nSi une Vème relaxation améliore encore une distance → cycle négatif.\nComplexité : O(V×E).",'// Bellman-Ford : poids négatifs OK, lent mais robuste'),
    ("JS","Microtask starvation","Peut-on bloquer les macrotasks avec des microtasks ?","function infinite() {\n  Promise.resolve().then(infinite)\n}\ninfinite()\nsetTimeout(() => console.log('Jamais affiché?'), 0)",["Oui, le setTimeout ne s'exécute jamais","Non, le scheduler équilibre","Le code plante","setTimeout passe avant"],0,"Oui, le setTimeout ne s'exécute jamais","Les microtasks sont vidées ENTIÈREMENT avant chaque macrotask.\nSi on crée une microtask infinie, la queue n'est jamais vide.\nLe setTimeout (macrotask) ne s'exécute jamais → starvation!",'// Éviter les boucles infinies dans les microtasks'),
    ("ALGO","Minimum spanning tree","Kruskal vs Prim : lequel choisir ?","// Kruskal :\n// - Trier toutes les arêtes par poids\n// - Ajouter si pas de cycle (Union-Find)\n// - O(E log E)\n// - Meilleur pour les graphes épars\n\n// Prim :\n// - Partir d'un nœud, ajouter le voisin le moins cher\n// - Min-heap\n// - O(E log V)\n// - Meilleur pour les graphes denses",["Kruskal toujours","Prim toujours","Kruskal sparse / Prim dense","Identiques"],2,"Kruskal sparse / Prim dense","Kruskal : O(E log E), optimal pour graphes épars (E ~ V).\nPrim avec adjacency matrix : O(V²) pour les graphes denses.\nLes deux produisent un MST (arbre couvrant de poids minimum).",'// MST : réseaux, cables, routage optimal'),
    ("JS","Object.defineProperty()","Comment créer une propriété non-énumérable ?","const obj = {}\nObject.defineProperty(obj, 'secret', {\n  value: 42,\n  writable: false,\n  enumerable: false,\n  configurable: false\n})\nconsole.log(obj.secret)\nconsole.log(Object.keys(obj))\nfor (let k in obj) console.log(k)",["42 / ['secret'] / 'secret'","42 / [] / (rien)","Error","42 / [] / 'secret'"],1,"42 / [] / (rien)","enumerable: false → exclu de for...in et Object.keys().\nwritable: false → obj.secret = 99 échoue silencieusement.\nconfigurable: false → impossible de re-définir ou supprimer.",'// defineProperty : contrôle précis des propriétés'),
    ("ALGO","Dijkstra avec heap","Complexité de Dijkstra avec un min-heap ?","// Sans heap : O(V²)\n// Avec min-heap (priority queue) :\n// - Extraction du min : O(log V)\n// - Relaxation : O(log V)\n// - Total : O((V+E) log V)\n//\n// Avec Fibonacci heap :\n// - O(E + V log V) théorique\n// - Complexe à implémenter",["O(V²)","O(E log V) avec min-heap","O(V log V)","O(E + V)"],1,"O(E log V) avec min-heap","Avec un min-heap : chaque sommet extrait en O(log V), chaque arête relaxée en O(log V).\nTotal O((V+E) log V) ≈ O(E log V) pour les graphes connectés.\nPratiquement la référence pour les graphes épars.",'// Dijkstra + min-heap : standard en compétition'),
    ("JS","Prototype vs __proto__","Quelle est la différence entre prototype et __proto__ ?","function Foo() {}\nconst foo = new Foo()\nconsole.log(foo.__proto__ === Foo.prototype)\nconsole.log(foo.prototype)\nconsole.log(Foo.prototype.constructor === Foo)",["false / {} / true","true / undefined / true","true / {} / false","Error"],1,"true / undefined / true","Foo.prototype : objet partagé entre toutes les instances de Foo.\nfoo.__proto__ : lien vers le prototype de l'objet (= Foo.prototype).\nfoo.prototype : undefined car foo est une instance, pas une fonction.",'// prototype : sur les fn | __proto__ : sur les objets'),
    ("ALGO","String matching — Rabin-Karp","Rabin-Karp utilise quelle technique pour O(n+m) moyen ?","function rabinKarp(text, pattern) {\n  // Calcul hash du pattern\n  // Sliding window hash sur text\n  // Si hash match → vérifier caractère par caractère\n  // Rolling hash : O(1) par slide\n  // O(n+m) moyen, O(nm) pire cas (collisions)\n}",["Tri du texte","Rolling hash + vérification","BFS sur le texte","Segments tree"],1,"Rolling hash + vérification","Rabin-Karp calcule un hash glissant en O(1) par position.\nSi les hash correspondent → vérification O(m).\nO(n+m) en moyenne, mais O(nm) en pire cas (nombreuses collisions).",'// Rolling hash : enlever le 1er char, ajouter le dernier'),
    ("JS","Symbol.iterator","Comment rendre un objet itérable ?","class Range {\n  constructor(start, end) {\n    this.start = start; this.end = end\n  }\n  [Symbol.iterator]() {\n    let current = this.start\n    const end = this.end\n    return {\n      next() {\n        return current <= end\n          ? { value: current++, done: false }\n          : { done: true }\n      }\n    }\n  }\n}\nfor (const n of new Range(1, 5)) console.log(n)",["Erreur, Range n'est pas itérable","Affiche 1,2,3,4,5","Affiche undefined","Boucle infinie"],1,"Affiche 1,2,3,4,5","Implémenter Symbol.iterator rend l'objet itérable.\nfor...of, spread, destructuring utilisent tous cet iterator.\nLe protocole retourne { value, done }.",'// Symbol.iterator : duck typing pour l\'itération'),
    ("ALGO","Longest common substring","LCS vs LCSubstring : quelle différence ?","// LCS (Subsequence) : pas forcément contigus\n// 'ABCBDAB' vs 'BDCAB' → LCS='BCAB' (4)\n\n// LCSubstring : doivent être contigus\n// 'ABCBDAB' vs 'BDCAB' → LCSubstring='AB' (2)\n//\n// DP LCSubstring :\n// dp[i][j] = dp[i-1][j-1]+1 si s1[i]===s2[j]\n//          = 0 sinon",["Identiques","LCS = contigus, Substring = non-contigus","LCS = non-contigus, Substring = contigus","Aucune différence de complexité"],2,"LCS = non-contigus, Substring = contigus","LCS (Longest Common Subsequence) : lettres peuvent être séparées.\nLCS (Longest Common Substring) : lettres doivent être adjacentes.\nDP différente : on remet à 0 si les chars ne matchent pas.",'// LCSubstring DP : dp[i][j]=0 si pas de match'),
    ("JS","Error.cause","Quelle nouveauté apporte Error cause (ES2022) ?","try {\n  try {\n    throw new Error('DB connection failed')\n  } catch (e) {\n    throw new Error('Service unavailable', { cause: e })\n  }\n} catch (err) {\n  console.log(err.message)\n  console.log(err.cause.message)\n}",["Error non supporté","'Service unavailable' / 'DB connection failed'","Error: message seulement, pas cause","TypeError"],1,"'Service unavailable' / 'DB connection failed'","Error({ cause }) permet de chaîner les erreurs.\nOn garde le contexte original tout en ajoutant un niveau d'abstraction.\nEssentiel pour les logs et le debugging en production.",'// err.cause : chaînage d\'erreurs pour mieux déboguer'),
    ("ALGO","Minimum cut — Max flow","Quel théorème lie le min-cut et le max-flow ?","// Théorème Max-Flow Min-Cut :\n// La valeur du flux maximum dans un réseau\n// EST ÉGALE à la capacité du coupe minimum\n//\n// Ford-Fulkerson : O(E * maxFlow)\n// Edmonds-Karp : O(VE²)\n// Dinic's : O(V²E)",["Ce sont des problèmes différents","Max flow = Min cut (théorème)","Min cut < Max flow toujours","Max flow > Min cut toujours"],1,"Max flow = Min cut (théorème)","Le théorème Max-Flow Min-Cut est fondamental en théorie des graphes.\nApplications : optimisation réseau, matching bipartite, image segmentation.\nFord-Fulkerson + BFS = Edmonds-Karp O(VE²).",'// Max-flow : transport, réseaux, matching'),
    ("JS","Object.create() vs new","Quelle est la différence ?","const proto = {\n  greet() { return `Hello ${this.name}` }\n}\n\n// Object.create() :\nconst obj = Object.create(proto)\nobj.name = 'Alice'\n\n// new :\nfunction Person(name) { this.name = name }\nPerson.prototype = proto\nconst p = new Person('Bob')\n\nconsole.log(obj.greet(), p.greet())",["'Hello Alice', Error","'Hello Alice', 'Hello Bob'","Error, 'Hello Bob'","undefined, undefined"],1,"'Hello Alice', 'Hello Bob'","Object.create(proto) crée un objet dont le __proto__ = proto.\nnew Person() crée une instance et appelle le constructeur.\nObject.create(null) crée un objet sans prototype (pure map).",'// Object.create(null) : HashMap ultra-performant'),
    ("ALGO","P vs NP","Quelle est la signification de P ≠ NP (si prouvé) ?","// P = problèmes solubles en temps polynomial\n// NP = problèmes vérifiables en temps polynomial\n// NP-complet = les problèmes les plus durs de NP\n//\n// Si P = NP : tous les problèmes NP seraient P\n// → Cryptographie cassée, médecine révolutionnée\n// Si P ≠ NP : certains problèmes sont intrinsèquement durs",["Tous les algos sont O(n)","Certains problèmes n'ont pas de solution polynomial","P est toujours meilleur que NP","NP signifie 'non-polynomial'"],1,"Certains problèmes n'ont pas de solution polynomial","P ≠ NP signifie que vérifier une solution est plus facile que la trouver.\nCryptographie RSA repose sur cette hypothèse (factorisation = NP).\nUn million de dollars pour quiconque prouve P = NP ou P ≠ NP (Clay Prize).",'// NP-complete : TSP, SAT, Knapsack, Coloring...'),
    ("JS","WeakRef + FinalizationRegistry","Comment détecter le GC d'un objet ?","const registry = new FinalizationRegistry((heldValue) => {\n  console.log(`${heldValue} a été GC'd`)\n})\n\nlet obj = { name: 'test' }\nconst ref = new WeakRef(obj)\nregistry.register(obj, 'mon objet')\n\nobj = null\n// Plus tard, après un GC :\n// → 'mon objet a été GC'd'",["Impossible en JS","FinalizationRegistry callback après GC","WeakRef.deref() lance une event","Error: GC non accessible"],1,"FinalizationRegistry callback après GC","FinalizationRegistry enregistre une callback appelée après GC.\nUtile pour nettoyer des ressources externes (fichiers, sockets).\nLa callback n'est PAS garantie d'être appelée (GC = non-déterministe).",'// FinalizationRegistry : best-effort cleanup, pas garanti'),
    ("ALGO","Boyer-Moore majority vote","Trouve l'élément majoritaire en O(n) O(1) ?","function majorityElement(nums) {\n  let candidate = null, count = 0\n  for (const n of nums) {\n    if (count === 0) candidate = n\n    count += (n === candidate) ? 1 : -1\n  }\n  return candidate\n}\n// Input: [3,2,3]\n// Output: ???",["2","3","Error","undefined"],1,"3","Boyer-Moore : on maintient un candidat et un compteur.\nSi count = 0, on change de candidat.\nSi l'élément majoritaire existe (> n/2), il sera le candidat final.",'// O(n) temps O(1) espace : impossible de faire mieux'),
] + [
    # Derniers posts jusqu'au 241
    ("JS","Performance — Object vs Map","Quand préférer Map à un objet classique ?","const obj = {}\nconst map = new Map()\n// Insertions : obj[key]=v vs map.set(key,v)\n// Taille : Object.keys(obj).length vs map.size\n// Itération : for...in vs for...of\n// Clés : strings/Symbols vs any type",["Toujours obj","Toujours Map","Map : fréquentes insertions/suppressions et clés non-string","Identiques"],2,"Map : fréquentes insertions/suppressions et clés non-string","Map est optimisé pour les insertions/suppressions fréquentes.\nMap.size est O(1) contrairement à Object.keys().length O(n).\nMap accepte n'importe quel type de clé.",'// Map : perf + key-any | obj : JSON, static data'),
    ("ALGO","Monotonic stack","Quand utiliser une monotonic stack ?","function nextGreater(nums) {\n  const result = new Array(nums.length).fill(-1)\n  const stack = [] // indices, décroissant\n  for (let i = 0; i < nums.length; i++) {\n    while (stack.length && nums[i] > nums[stack.at(-1)]) {\n      result[stack.pop()] = nums[i]\n    }\n    stack.push(i)\n  }\n  return result\n}\n// Input: [2,1,2,4,3]\n// Output: [4,2,4,-1,-1]",["Tri rapide","Next greater/smaller element en O(n)","BFS sur graphe","Recherche binaire"],1,"Next greater/smaller element en O(n)","Monotonic stack : stack dont les éléments sont en ordre croissant ou décroissant.\nUtilisé pour : next greater element, stock span, trapping rain water.\nO(n) car chaque élément est poussé/popped une seule fois.",'// Monotonic stack : O(n) pour next greater/smaller'),
    ("JS","Generators — infinite sequences","Comment créer une séquence infinie ?","function* naturals() {\n  let n = 1\n  while (true) yield n++\n}\n\nfunction take(gen, n) {\n  const result = []\n  for (const v of gen) {\n    result.push(v)\n    if (result.length >= n) break\n  }\n  return result\n}\nconsole.log(take(naturals(), 5))",["Boucle infinie, freeze","[1,2,3,4,5]","Error","undefined"],1,"[1,2,3,4,5]","Les générateurs sont lazy : ils ne calculent que ce dont on a besoin.\nUne séquence infinie ne plante pas car on contrôle l'arrêt.\nEssentiel pour les streams de données, pagination, etc.",'// Générateurs : lazy evaluation = puissance et efficacité'),
    ("ALGO","Graph — bridges","Qu'est-ce qu'un pont dans un graphe ?","// Pont (bridge) : arête dont la suppression\n// déconnecte le graphe\n//\n// Algorithme de Tarjan :\n// - DFS + discovery time + low value\n// - Arête (u,v) est un pont si :\n//   low[v] > disc[u]\n// - O(V+E)",["Un nœud central","Une arête critique qui connecte 2 composantes","Un cycle","Le nœud de départ"],1,"Une arête critique qui connecte 2 composantes","Un pont est une arête dont la suppression augmente le nombre de composantes connexes.\nAlgorithme de Tarjan détecte tous les ponts en O(V+E).\nApplications : réseaux, points de défaillance critique.",'// Tarjan bridges : low[v] > disc[u] → pont'),
    ("JS","Currying avancé — curry() générique","Comment implémenter curry() pour n'importe quelle fn ?","function curry(fn) {\n  return function curried(...args) {\n    if (args.length >= fn.length) {\n      return fn.apply(this, args)\n    }\n    return function(...args2) {\n      return curried.apply(this, args.concat(args2))\n    }\n  }\n}\nconst add = curry((a,b,c) => a+b+c)\nconsole.log(add(1)(2)(3))\nconsole.log(add(1,2)(3))\nconsole.log(add(1)(2,3))",["Seulement add(1)(2)(3) fonctionne","Les 3 fonctionnent et retournent 6","Error","undefined"],1,"Les 3 fonctionnent et retournent 6","curry() générique accumule les args jusqu'à fn.length.\nLe même résultat peu importe comment on fournit les arguments.\nUtilisé dans la programmation fonctionnelle (Ramda, Lodash/fp).",'// fn.length : arity (nombre de params déclarés)'),
    ("ALGO","Knuth's optimization","Quand appliquer l'optimisation de Knuth pour la DP ?","// Knuth's optimization :\n// Pour certains DP : dp[i][j] = opt sur dp[i][k]+dp[k][j]\n// Si la fonction de coût est monotone et concave...\n// On peut passer de O(n³) à O(n²)\n//\n// Exemple : matrix chain multiplication\n// Optimal BST\n// Partition de tableau",["Toujours","Jamais","Pour les DP de type 'partitionner un intervalle'","Pour les graphes"],2,"Pour les DP de type 'partitionner un intervalle'","Knuth's optimization s'applique quand opt(i,j) est monotone.\nPassage de O(n³) à O(n²) pour certains problèmes DP.\nMatrix chain multiplication est le cas classique.",'// Knuth opt : vérifier monotonicity + quadrangle inequality'),
    ("JS","[FINAL] Bilan Codebog Phase 4","🏆 Dernier post de l'année ! Quel concept est le plus utile en entretien ?","// 241 posts accomplis !\n// Top concepts vus :\n// ✓ Closures & prototypes\n// ✓ Event loop & Promises\n// ✓ Array methods (map/filter/reduce)\n// ✓ Modern JS (ES2022-2024)\n// ✓ Performance patterns",["Closures","Event loop","Les deux + les array methods","Tout ce qu'on a vu !"],3,"Tout ce qu'on a vu !","241 posts, une année de JavaScript et algorithmie.\nDe typeof null aux algorithmes avancés en passant par l'event loop.\nMerci de nous avoir suivi — rendez-vous l'année prochaine ! 🚀",'// 👉 learning.itmade.fr pour aller plus loin'),
]

# ─────────────────────────────────────────
# GÉNÉRATION DU CALENDRIER
# ─────────────────────────────────────────

def build_schedule():
    """Construit le calendrier complet des 241 posts."""
    schedule = []
    current = START_DATE
    day = 1
    js_idx = 0
    algo_idx = 0

    # Séparer JS et ALGO
    js_topics   = [t for t in TOPICS if t[0] == "JS"]
    algo_topics = [t for t in TOPICS if t[0] == "ALGO"]

    while current <= END_DATE:
        if day % 2 == 1:  # impair → JS
            topic = js_topics[js_idx % len(js_topics)]
            js_idx += 1
        else:              # pair → ALGO
            topic = algo_topics[algo_idx % len(algo_topics)]
            algo_idx += 1

        phase = 1 if day <= 60 else 2 if day <= 120 else 3 if day <= 180 else 4

        schedule.append({
            "day": day,
            "date": current.strftime("%Y-%m-%d"),
            "day_name": ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"][current.weekday()],
            "type": topic[0],
            "phase": phase,
            "topic": topic[1],
            "hook": topic[2],
            "code": topic[3],
            "options": {EMOJIS[i]: topic[4][i] for i in range(4)},
            "correct_emoji": EMOJIS[topic[5]],
            "answer": topic[6],
            "explanation": topic[7],
            "tip": topic[8],
            "cta": "👉 learning.itmade.fr" if day % 2 == 1 else "👉 codebog.itmade.fr",
            "post_text": generate_post_text(topic, day)
        })

        current += timedelta(days=1)
        day += 1

    return schedule

def generate_post_text(topic, day):
    """Génère le texte complet du post Facebook."""
    type_label = "JS" if topic[0] == "JS" else "ALGO"
    emojis_str = " · ".join([f"{EMOJIS[i]} {topic[4][i]}" for i in range(4)])
    return f"""🖥️ #{day:03d} — {type_label} · {topic[1]}

{topic[2]}

```
{topic[3]}
```

{emojis_str}

⏱️ Tu as 10 secondes. Réponds avec une réaction.
👇 La réponse est en commentaire.

━━━━━━━━━━━━━━━
💬 Commentaire (à épingler) :

✅ Réponse : {topic[6]}

{topic[7]}

💡 À retenir :
{topic[8]}

{'👉 learning.itmade.fr' if type_label == 'JS' else '👉 codebog.itmade.fr'} — Entraîne-toi tous les jours 🚀
"""

# ─────────────────────────────────────────
# GÉNÉRATION D'IMAGE PNG (Pillow)
# ─────────────────────────────────────────

def hex_to_rgb(hex_color):
    h = hex_color.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def get_font(size):
    """Charge une police monospace disponible."""
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
        "/System/Library/Fonts/Menlo.ttc",
        "C:/Windows/Fonts/consola.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return ImageFont.load_default()

def get_bold_font(size):
    bold_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf",
    ]
    for path in bold_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except:
                pass
    return get_font(size)

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def syntax_color(token):
    """Retourne une couleur selon le type de token JS."""
    keywords = {'function','return','const','let','var','if','else','for','while',
                'true','false','null','undefined','new','class','extends','import',
                'export','default','async','await','of','in','typeof','instanceof',
                'throw','try','catch','finally','switch','case','break','continue',
                'yield','static','this','super','from','get','set'}
    if token in keywords:           return PURPLE        # violet
    if token.startswith('//'):      return (106,153,85)  # vert commentaire
    if token.startswith('"') or token.startswith("'") or token.startswith('`'):
                                    return (206,145,120) # orange string
    if token.replace('.','').replace('-','').isdigit(): return (181,206,168) # vert nb
    return None

def colorize_line(draw, x, y, line, font, default_color):
    """Dessine une ligne avec colorisation syntaxique basique."""
    # Colorisation token par token (approximation)
    import re
    # Pattern pour découper : strings, comments, keywords, nombres, le reste
    pattern = r'(//[^\n]*|"[^"]*"|\'[^\']*\'|`[^`]*`|\b\w+\b|[^\w\s]|\s+)'
    tokens = re.findall(pattern, line)
    cx = x
    for tok in tokens:
        if tok.strip() == '':
            bbox = draw.textbbox((0,0), tok, font=font)
            cx += bbox[2]
            continue
        color = default_color
        stripped = tok.strip()
        if stripped.startswith('//'):
            color = (106, 153, 85)
        elif stripped.startswith('"') or stripped.startswith("'") or stripped.startswith('`'):
            color = (206, 145, 120)
        elif stripped in {'function','return','const','let','var','if','else','for',
                          'while','true','false','null','undefined','new','class',
                          'extends','async','await','typeof','instanceof','throw',
                          'try','catch','finally','yield','static','this'}:
            color = (197, 134, 192)
        elif stripped in {'console','Math','Object','Array','Promise','JSON','Number',
                          'String','Boolean','Symbol','Map','Set','WeakMap','WeakSet'}:
            color = (78, 201, 176)
        elif stripped.replace('.','').lstrip('-').isdigit():
            color = (181, 206, 168)
        draw.text((cx, y), tok, font=font, fill=color)
        bbox = draw.textbbox((0,0), tok, font=font)
        cx += bbox[2]

def _lf(name, size):
    """
    Charge une font avec priorite :
    1. Dossier courant (si DejaVu telechargees)
    2. Fonts Windows systeme (toujours disponibles)
    3. Fonts Linux
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

def _draw_hook_two_color(draw, hook, x, y_start, font_w, font_g, accent, base, max_w):
    """
    Rend le hook sur plusieurs lignes avec 2 couleurs :
    - Ligne 1        : blanc
    - Début ligne 2  : vert (mots accent)
    - Suite ligne 2+ : blanc
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

def _colorize_token(draw, x, y, token, font):
    """Rend un token JS avec sa couleur syntaxique, retourne le nouveau x."""
    KW  = {'function','return','const','let','var','if','else','for','while','do',
           'true','false','null','undefined','new','class','extends','super','this',
           'async','await','typeof','instanceof','throw','try','catch','finally',
           'yield','static','of','in','switch','case','break','continue','from',
           'import','export','default','get','set','delete','void'}
    CLS = {'console','Math','Object','Array','Promise','JSON','Number','String',
           'Boolean','Symbol','Map','Set','WeakMap','WeakSet','Error','Date'}
    t = token.strip()
    if not t:
        x += draw.textbbox((0,0), token, font=font)[2]
        return x
    if t.startswith('//'):
        color = (106, 153, 85)
    elif t.startswith('"') or t.startswith("'") or t.startswith('`'):
        color = (206, 145, 120)
    elif t in KW:
        color = (197, 134, 192)
    elif t in CLS:
        color = (78, 201, 176)
    elif t.lstrip('-').replace('.','').isdigit():
        color = (181, 206, 168)
    else:
        color = (212, 212, 220)
    draw.text((x, y), token, font=font, fill=color)
    x += draw.textbbox((0,0), token, font=font)[2]
    return x

def _draw_code_line(draw, x_start, y, line, font):
    import re
    pat = r'(//[^\n]*|"[^"]*"|\'[^\']*\'|`[^`]*`|\b\w+\b|[^\w\s]|\s+)'
    for tok in re.findall(pat, line):
        x_start = _colorize_token(draw, x_start, y, tok, font)

def generate_image(post, output_path):
    """
    Layout identique à l'image de référence :
    ┌─────────────────────────────────────────────┐
    │ ⚡ JS CHALLENGE            #001 / 365        │  ← badges
    │                                             │
    │ Hook ligne 1              (blanc)            │  ← accroche
    │ HOOK ACCENT  reste        (vert + blanc)     │
    │                                             │
    │ ┌─ Terminal macOS ───────────────────────┐  │  ← terminal
    │ │ ● ● ●      js.js — codebog            │  │
    │ │                                       │  │
    │ │  1  console.log(typeof null)          │  │
    │ └───────────────────────────────────────┘  │
    │                                             │
    │ ❤️  "null"      │  😮  "object"             │  ← options 2×2
    │ 😂  "undefined" │  🔥  "boolean"            │
    │                                             │
    │   ↓  RÉAGIS AVANT DE LIRE LES COMMENTAIRES │  ← CTA bar
    ├─────────────────────────────────────────────┤
    │ codebog  🧠 learning.itmade.fr  🎮 codeb…  │  ← footer
    └─────────────────────────────────────────────┘
    """
    W, H   = 1080, 1080
    img    = Image.new("RGB", (W, H), BG)
    draw   = ImageDraw.Draw(img)
    is_js  = post['type'] == 'JS'
    ACCENT = GREEN if is_js else BLUE

    # ── Fonts ──────────────────────────────────────────────────────────
    f_badge   = _lf("DejaVuSansMono.ttf",  26)
    f_hook_w = _lf("DejaVuSans.ttf", 56)
    f_hook_g = _lf("DejaVuSans-Bold.ttf", 64)
    f_tb      = _lf("DejaVuSansMono.ttf",  22)
    f_lnum    = _lf("DejaVuSansMono.ttf",  56)   # numéro de ligne
    f_opt     = _lf("DejaVuSansMono.ttf",  28)
    f_emoji   = _lf("seguiemj.ttf",        52)   # Windows emoji (fallback DejaVu)
    if str(f_emoji) == str(ImageFont.load_default()):
        f_emoji = _lf("DejaVuSans.ttf", 52)
    f_cta     = _lf("DejaVuSansMono.ttf",  24)
    f_logo    = _lf("DejaVuSans-Bold.ttf", 52)
    f_foot    = _lf("DejaVuSans.ttf",      20)

    # Code font : adapté au nombre de lignes
    code_lines = post['code'].split('\n')
    nl = len(code_lines)
    max_line_len = max(len(line) for line in code_lines)

    # Ajuster selon la longueur pour eviter debordements
    if nl == 1:
        if max_line_len > 50:
            code_sz = 22
        elif max_line_len > 40:
            code_sz = 24
        elif max_line_len > 30:
            code_sz = 24
            code_sz = 48
    else:
        code_sz = 52 if nl <= 3 else (40 if nl <= 6 else 30)
    f_code = _lf("DejaVuSansMono.ttf", code_sz)

    M  = 32   # marge gauche/droite

    # ══════════════════════════════════════════════
    # 1. BADGES (y: 34 → 102)
    # ══════════════════════════════════════════════
    badge_l = "JS CHALLENGE" if is_js else "ALGO CHALLENGE"
    badge_r = f"#{post['day']:03d} / 365"
    badge_l_em = "[JS]" if is_js else "[ALGO]"  # fallback sans emoji

    # Badge gauche
    bb_l = draw.textbbox((0,0), badge_l, font=f_badge)
    bw_l = bb_l[2] + 40
    draw.rounded_rectangle((M, 34, M+bw_l, 102), radius=18, outline=ACCENT, width=2)
    draw.text((M+20, 52), badge_l, font=f_badge, fill=ACCENT)

    # Badge droit
    bb_r = draw.textbbox((0,0), badge_r, font=f_badge)
    bw_r = bb_r[2] + 40
    draw.rounded_rectangle((W-M-bw_r, 34, W-M, 102), radius=18, outline=ACCENT, width=2)
    draw.text((W-M-bw_r+20, 52), badge_r, font=f_badge, fill=ACCENT)

    # ══════════════════════════════════════════════
    # 2. HOOK — mesure d'abord, dessine ensuite
    # ══════════════════════════════════════════════

    # Mesure la hauteur du hook sur une image fantôme
    _img_tmp  = Image.new("RGB", (W, H), BG)
    _draw_tmp = ImageDraw.Draw(_img_tmp)
    hook_bottom = _draw_hook_two_color(
        _draw_tmp, post['hook'],
        x=M, y_start=118,
        font_w=f_hook_w, font_g=f_hook_g,
        accent=ACCENT, base=WHITE,
        max_w=W - M * 2 - 60  # Marge de sécurité pour éviter les lettres coupées
    )
    del _img_tmp, _draw_tmp

    # ── Calcul des hauteurs fixes sous le terminal ──
    GAP_HOOK_TERM = 20
    OH   = 100                        # hauteur d'une option
    OG   = 16                         # gap entre options
    CTA_H = 72
    FOOT_H = 110                      # séparateur + footer (2 lignes de texte + marges)
    FIXED_BELOW = (2*OH + OG) + GAP_HOOK_TERM + CTA_H + FOOT_H + 30

    # ── Espace disponible pour le terminal ──────────
    term_top     = hook_bottom + GAP_HOOK_TERM
    available_th = H - term_top - FIXED_BELOW          # pixels dispo pour terminal
    available_th = max(available_th, 160)               # plancher de sécurité

    # ── Taille de police : remplit la zone code ─────
    TB_H    = 78                                        # titlebar fixe
    PAD_V   = 28                                        # padding haut/bas code
    code_area_available = available_th - TB_H - 2 * PAD_V
    line_h  = max(30, code_area_available // nl)        # hauteur par ligne
    # Limiter selon hauteur ET longueur de ligne
    code_sz_height = min(64, max(22, int(line_h * 0.80)))
    # Limiter selon longueur de ligne pour éviter débordement
    if nl == 1 and max_line_len > 30:
        code_sz_width = 36 if max_line_len > 40 else 40
        code_sz = min(code_sz_height, code_sz_width)
    else:
        code_sz = code_sz_height
    f_code  = _lf("DejaVuSansMono.ttf", code_sz)

    # Recalcul de la hauteur réelle avec la taille de police choisie
    real_line_h   = int(code_sz * 1.38)
    total_code_h  = nl * real_line_h
    TH            = TB_H + 2 * PAD_V + total_code_h    # terminal s'adapte au code

    # ── Dessin du hook (pour de vrai) ───────────────
    _draw_hook_two_color(
        draw, post['hook'],
        x=M, y_start=118,
        font_w=f_hook_w, font_g=f_hook_g,
        accent=ACCENT, base=WHITE,
        max_w=W - M * 2 - 60  # Marge de sécurité pour éviter les lettres coupées
    )

    # ══════════════════════════════════════════════
    # 3. TERMINAL — taille adaptée au code
    # ══════════════════════════════════════════════
    tx, ty = M, term_top
    tw = W - M * 2

    # Fond terminal
    draw.rounded_rectangle((tx, ty, tx+tw, ty+TH),
                            radius=26, fill=(10,10,12),
                            outline=(48,48,58), width=2)
    # Titlebar
    draw.rounded_rectangle((tx, ty, tx+tw, ty+TB_H),
                            radius=26, fill=(16,16,18))
    draw.rectangle((tx, ty+TB_H-26, tx+tw, ty+TB_H), fill=(16,16,18))
    draw.line((tx, ty+TB_H, tx+tw, ty+TB_H), fill=(40,40,48), width=1)

    # Traffic lights
    for i, col in enumerate([RED, YELLOW, GREEN]):
        cx = tx + 28 + i * 38
        cy = ty + TB_H // 2
        draw.ellipse((cx-14, cy-14, cx+14, cy+14), fill=col)

    # Titre centré
    tt  = "js.js — codebog" if is_js else "algo.js — codebog"
    ttb = draw.textbbox((0, 0), tt, font=f_tb)
    draw.text((tx + (tw - ttb[2]) // 2, ty + (TB_H - ttb[3]) // 2),
              tt, font=f_tb, fill=(110, 110, 120))

    # Liseré accent gauche
    draw.rectangle((tx, ty+TB_H, tx+12, ty+TH), fill=ACCENT)

    # Code centré verticalement dans la zone code
    code_y_start = ty + TB_H + PAD_V

    # Numéro de ligne
    f_lnum_dyn = _lf("DejaVuSansMono.ttf", code_sz)
    # Espacement amélioré entre numéros de ligne et code
    code_x = tx + 95 if nl > 1 else tx + 100

    if nl == 1:
        draw.text((tx + 28, code_y_start), "1",
                  font=f_lnum_dyn, fill=(85, 85, 98))

    for i, line in enumerate(code_lines):
        cy_line = code_y_start + i * real_line_h
        if nl > 1:
            # Position des numéros de ligne avec alignement à droite
            line_num = str(i + 1)
            f_lnum = _lf("DejaVuSansMono.ttf", max(14, code_sz - 10))
            num_bbox = draw.textbbox((0, 0), line_num, font=f_lnum)
            num_width = num_bbox[2]
            # Aligner à droite les numéros (position fixe à droite avant le code)
            draw.text((tx + 75 - num_width, cy_line),
                      line_num,
                      font=f_lnum,
                      fill=(75, 75, 88))
        _draw_code_line(draw, code_x, cy_line, line, f_code)

    # ══════════════════════════════════════════════
    # 4. OPTIONS 2×2
    # ══════════════════════════════════════════════
    opts     = list(post['options'].items())
    oy_start = ty + TH + GAP_HOOK_TERM
    OW       = (W - M*2 - 18) // 2

    EMJ_SIZE = OH - 20
    for i, (emoji, label) in enumerate(opts):
        col = i % 2
        row = i // 2
        ox  = M + col * (OW + 18)
        oy  = oy_start + row * (OH + OG)
        draw.rounded_rectangle((ox, oy, ox+OW, oy+OH),
                                radius=18, fill=(12,12,16),
                                outline=(48,48,58), width=2)
        # Emoji PNG embarqué
        emj = _emoji_img(EMOJI_ORDER[i], size=EMJ_SIZE)
        img.paste(emj, (ox + 14, oy + (OH - EMJ_SIZE)//2), emj)
        draw.text((ox + 14 + EMJ_SIZE + 16, oy + (OH - 32)//2), label,
                  font=f_opt, fill=(220,220,225))

    # ══════════════════════════════════════════════
    # 5. CTA BAR
    # ══════════════════════════════════════════════
    cta_y = oy_start + 2*OH + OG + 14
    draw.rounded_rectangle((M, cta_y, W-M, cta_y+CTA_H),
                            radius=18, outline=ACCENT, width=2)

    # Flèche dessinée (cercle + triangle)
    _draw_down_arrow(draw, M + 62, cta_y + CTA_H//2, 26, ACCENT)

    # "RÉAGIS" en vert + reste en blanc
    cta_txt_x = M + 100
    cta_mid_y = cta_y + (CTA_H - draw.textbbox((0,0),"A",font=f_cta)[3]) // 2
    draw.text((cta_txt_x, cta_mid_y), "RÉAGIS ", font=f_cta, fill=ACCENT)
    rx = cta_txt_x + draw.textbbox((0,0), "RÉAGIS ", font=f_cta)[2]
    draw.text((rx, cta_mid_y), "AVANT DE LIRE LES COMMENTAIRES !",
              font=f_cta, fill=WHITE)

    # ══════════════════════════════════════════════
    # 6. FOOTER 3 colonnes
    # ══════════════════════════════════════════════
    sep_y  = cta_y + CTA_H + 14
    draw.line((M, sep_y, W-M, sep_y), fill=(22,60,35), width=1)
    fy = sep_y + 14

    # Colonne gauche : logo codebog
    draw.text((M, fy), "code", font=f_logo, fill=WHITE)
    cw = draw.textbbox((0,0), "code", font=f_logo)[2]
    draw.text((M + cw, fy), "bog", font=f_logo, fill=ACCENT)

    # Colonne centre : learning
    cx = W // 2 - 100
    draw.text((cx, fy), "🧠", font=_lf("DejaVuSans.ttf", 26), fill=WHITE)
    draw.text((cx + 36, fy), "Apprends. Pratique. Progresse.",
              font=_lf("DejaVuSans.ttf", 18), fill=(200,200,205))
    draw.text((cx + 36, fy + 26), "learning.itmade.fr",
              font=_lf("DejaVuSans.ttf", 18), fill=GREEN)

    # Colonne droite : codebog
    rx2 = W - M - 240
    draw.text((rx2, fy), "🎮", font=_lf("DejaVuSans.ttf", 26), fill=WHITE)
    play_lbl = "Entraîne-toi en JS" if is_js else "Entraîne-toi en Algo"
    draw.text((rx2 + 36, fy), play_lbl,
              font=_lf("DejaVuSans.ttf", 18), fill=(200,200,205))
    draw.text((rx2 + 36, fy + 26), "codebog.itmade.fr",
              font=_lf("DejaVuSans.ttf", 18), fill=BLUE)

    img.save(output_path, "PNG", quality=95)
    return output_path

def generate_image_DISABLED(post, output_path):
    """Ancienne version (désactivée)."""
    img  = Image.new('RGB', (IMG_W, IMG_H), BG)
    draw = ImageDraw.Draw(img)

    is_js       = post['type'] == 'JS'
    ACCENT      = GREEN if is_js else BLUE
    ACCENT_DIM  = (ACCENT[0]//5, ACCENT[1]//5, ACCENT[2]//5)

    # ── Fonts ──────────────────────────────────────
    f_hook   = get_bold_font(34)
    f_code   = get_font(26)
    f_option = get_font(24)
    f_label  = get_font(19)
    f_small  = get_font(18)
    f_tiny   = get_font(16)
    f_brand  = get_bold_font(38)

    MARGIN   = 50   # marge gauche/droite
    y        = 52   # curseur vertical

    # ── Badge type (haut droite) ───────────────────
    badge = f"{'⚡ JS' if is_js else '🧠 ALGO'}  #{post['day']:03d}"
    bbbox = draw.textbbox((0,0), badge, font=f_small)
    bx    = IMG_W - bbbox[2] - MARGIN
    draw.rounded_rectangle(
        [(bx-10, y-4), (bx + bbbox[2]+10, y + bbbox[3]+4)],
        radius=20, fill=ACCENT_DIM, outline=(*ACCENT, 80), width=1
    )
    draw.text((bx, y), badge, font=f_small, fill=ACCENT)

    # ── Hook ──────────────────────────────────────
    import textwrap as tw
    hook_lines = tw.wrap(post['hook'], width=44)
    for line in hook_lines[:2]:
        draw.text((MARGIN, y), line, font=f_hook, fill=WHITE)
        y += 44
    y += 14

    # ── Séparateur fin ─────────────────────────────
    draw.line([(MARGIN, y), (IMG_W - MARGIN, y)], fill=(40,40,45), width=1)
    y += 18

    # ── Fenêtre terminal ───────────────────────────
    code_lines  = post['code'].split('\n')
    n_lines     = len(code_lines)
    LINE_H      = 34
    PAD_X       = 52
    PAD_Y       = 18
    TITLEBAR_H  = 40
    WIN_W       = IMG_W - MARGIN * 2
    WIN_H       = TITLEBAR_H + PAD_Y + n_lines * LINE_H + PAD_Y

    # Ombre
    draw.rounded_rectangle(
        [(MARGIN+8, y+8), (MARGIN + WIN_W+8, y + WIN_H+8)],
        radius=14, fill=(4,4,5)
    )
    # Corps
    draw.rounded_rectangle(
        [(MARGIN, y), (MARGIN + WIN_W, y + WIN_H)],
        radius=14, fill=CODEBG, outline=(44,44,48), width=1
    )
    # Titlebar
    draw.rounded_rectangle(
        [(MARGIN, y), (MARGIN + WIN_W, y + TITLEBAR_H)],
        radius=14, fill=(26,26,28)
    )
    draw.rectangle(
        [(MARGIN, y + TITLEBAR_H - 14), (MARGIN + WIN_W, y + TITLEBAR_H)],
        fill=(26,26,28)
    )
    draw.line(
        [(MARGIN, y + TITLEBAR_H), (MARGIN + WIN_W, y + TITLEBAR_H)],
        fill=(44,44,50), width=1
    )
    # Traffic lights
    DOT_CY = y + TITLEBAR_H // 2
    for i, col in enumerate([RED, YELLOW, GREEN]):
        cx = MARGIN + 18 + i * 22
        draw.ellipse([(cx-7, DOT_CY-7), (cx+7, DOT_CY+7)], fill=col)
    # Titre titlebar
    tb_title = f"{post['type'].lower()}.js — codebog"
    tbb = draw.textbbox((0,0), tb_title, font=f_tiny)
    draw.text(
        (MARGIN + (WIN_W - tbb[2])//2, y + (TITLEBAR_H - tbb[3])//2),
        tb_title, font=f_tiny, fill=(80,80,88)
    )
    # Liseré accent gauche
    draw.rectangle(
        [(MARGIN, y + TITLEBAR_H), (MARGIN + 3, y + WIN_H)],
        fill=ACCENT
    )

    # Code coloré + numéros de lignes
    cy = y + TITLEBAR_H + PAD_Y
    for i, line in enumerate(code_lines):
        # Numéro de ligne
        draw.text((MARGIN + 12, cy), str(i+1), font=f_tiny, fill=(55,55,62))
        # Code
        colorize_line(draw, MARGIN + PAD_X, cy, line, f_code, (210,210,218))
        cy += LINE_H

    y += WIN_H + 22

    # ── Options de vote (grille 2x2) ───────────────
    opts        = list(post['options'].items())
    OPT_W       = (IMG_W - MARGIN*2 - 12) // 2
    OPT_H       = 56
    for i, (emoji, label) in enumerate(opts):
        col = i % 2
        row = i // 2
        ox  = MARGIN + col * (OPT_W + 12)
        oy  = y + row * (OPT_H + 10)
        # Fond
        draw.rounded_rectangle(
            [(ox, oy), (ox + OPT_W, oy + OPT_H)],
            radius=12, fill=(18,18,20), outline=(42,42,48), width=1
        )
        # Emoji + label
        draw.text((ox + 14, oy + 14), emoji, font=f_option, fill=WHITE)
        ebb = draw.textbbox((0,0), emoji, font=f_option)
        draw.text((ox + 14 + ebb[2] + 10, oy + 16), label, font=f_label, fill=(160,160,172))

    y += 2 * OPT_H + 10 + 20

    # ── Séparateur ─────────────────────────────────
    draw.line([(MARGIN, y), (IMG_W - MARGIN, y)], fill=(35,35,40), width=1)
    y += 18

    # ── Footer ─────────────────────────────────────
    # Timer
    timer_txt = "⏱  10 sec · Réagis avant de lire les commentaires 👇"
    draw.text((MARGIN, y), timer_txt, font=f_small, fill=(70,70,78))
    y += 30

    # Branding codebog + CTA
    draw.text((MARGIN, y), "code", font=f_brand, fill=(220,220,228))
    bbb = draw.textbbox((0,0), "code", font=f_brand)
    draw.text((MARGIN + bbb[2], y), "bog", font=f_brand, fill=ACCENT)
    bbb2 = draw.textbbox((0,0), "bog", font=f_brand)

    cta = post.get('cta', '👉 codebog.itmade.fr')
    draw.text((MARGIN + bbb[2] + bbb2[2] + 24, y + 8), cta, font=f_small, fill=(80,80,88))

    # Phase
    phase_txt = f"Phase {post['phase']} / 4"
    ptb = draw.textbbox((0,0), phase_txt, font=f_tiny)
    draw.text((IMG_W - MARGIN - ptb[2], y + 10), phase_txt, font=f_tiny, fill=(50,50,56))

    img.save(output_path, 'PNG', quality=95)
    return output_path

# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Codebog Post Generator')
    parser.add_argument('--day', type=int, help='Générer le post d\'un jour précis')
    parser.add_argument('--range', type=int, nargs=2, metavar=('START','END'), help='Générer un range de posts')
    parser.add_argument('--json', action='store_true', help='Exporter posts.json')
    parser.add_argument('--preview', action='store_true', help='Afficher le texte d\'un post')
    args = parser.parse_args()

    print("⚡ Codebog Post Generator")
    print(f"   {START_DATE} → {END_DATE}")
    print("   Chargement du calendrier...\n")

    schedule = build_schedule()
    print(f"   ✓ {len(schedule)} posts chargés")
    print(f"   ✓ {sum(1 for p in schedule if p['type']=='JS')} posts JS")
    print(f"   ✓ {sum(1 for p in schedule if p['type']=='ALGO')} posts Algo\n")

    if args.json:
        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump(schedule, f, ensure_ascii=False, indent=2)
        print("✓ posts.json exporté")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if args.day:
        posts_to_gen = [p for p in schedule if p['day'] == args.day]
    elif args.range:
        posts_to_gen = [p for p in schedule if args.range[0] <= p['day'] <= args.range[1]]
    else:
        posts_to_gen = schedule

    for post in posts_to_gen:
        filename = f"{OUTPUT_DIR}/codebog_{post['day']:03d}_{post['date']}_{post['type'].lower()}.png"
        print(f"🖼  #{post['day']:03d} {post['date']} [{post['type']}] {post['topic'][:40]}...", end=' ', flush=True)
        generate_image(post, filename)
        print("✓")

        if args.preview or args.day:
            print("\n" + "─"*60)
            print(post['post_text'])
            print("─"*60 + "\n")

    print(f"\n✅ {len(posts_to_gen)} image(s) générée(s) dans ./{OUTPUT_DIR}/")
    print("\n📋 Prochaine étape : poster quotidiennement sur facebook.com/codebog")

if __name__ == '__main__':
    main()


# ─────────────────────────────────────────
# SOCIAL CONTENT GENERATOR
# ─────────────────────────────────────────

def generate_social_post(topic):
    ttype, short, hook, snippet, options, correct_idx, answer, explanation, tip = topic

    reactions = ["👍", "❤️", "😮", "😂"]

    poll = "\n".join([
        f"{reactions[i]} {chr(65+i)}) {options[i]}"
        for i in range(4)
    ])

    post = f"""
{BADGES.get(ttype)}

{hook}

```js
{snippet}
```

{poll}

⏱️ 10 secondes… pas de triche.

👇 Vote avec une réaction.
"""

    pinned_comment = f"""
✅ Réponse : {reactions[correct_idx]} {answer}

{explanation}

{tip}

{CTA.get(ttype)}

{HASHTAGS.get(ttype)}
"""

    return {
        "post": post.strip(),
        "comment": pinned_comment.strip()
    }



# ─────────────────────────────────────────
# ANALYTICS PLACEHOLDER
# ─────────────────────────────────────────

def save_metrics(post_id, views=0, comments=0, reactions=0):
    metrics = {
        "post_id": post_id,
        "views": views,
        "comments": comments,
        "reactions": reactions
    }

    path = os.path.join(OUTPUT_DIR, "metrics.json")

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    data.append(metrics)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)



# ─────────────────────────────────────────
# ADVANCED FEATURES V3
# ─────────────────────────────────────────

from PIL import Image, ImageDraw, ImageFont
import textwrap
from datetime import datetime

APPLE_BG = "#0B0B0C"
APPLE_TEXT = "#EDEDED"

def generate_apple_terminal_image(title, code_snippet, output_path):
    """
    Generate Apple keynote style terminal image
    """

    width, height = 1080, 1080

    img = Image.new("RGB", (width, height), APPLE_BG)
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("DejaVuSans.ttf", 42)
        font_code = ImageFont.truetype("DejaVuSansMono.ttf", 34)
    except:
        font_title = ImageFont.load_default()
        font_code = ImageFont.load_default()

    # macOS buttons
    buttons = [
        ("#FF5F57", 70),
        ("#FEBC2E", 110),
        ("#28C840", 150)
    ]

    for color, x in buttons:
        draw.ellipse((x, 60, x+22, 82), fill=color)

    # title
    draw.text((70, 130), title, fill=APPLE_TEXT, font=font_title)

    # terminal block
    wrapped = textwrap.fill(code_snippet, width=32)

    draw.rounded_rectangle((60, 220, 1020, 850), radius=25, outline="#1E1E1E", width=3)

    draw.multiline_text(
        (90, 280),
        wrapped,
        fill=APPLE_TEXT,
        font=font_code,
        spacing=18
    )

    # watermark
    draw.text(
        (760, 980),
        "itmade.fr",
        fill="#666666",
        font=font_code
    )

    img.save(output_path)


# ─────────────────────────────────────────
# FACEBOOK EXPORTER
# ─────────────────────────────────────────

def export_facebook_package(topic, output_dir="facebook_exports"):
    """
    Export ready-to-post Facebook package
    """

    os.makedirs(output_dir, exist_ok=True)

    social = generate_social_post(topic)

    filename = topic[1].replace(" ", "_").lower()

    txt_path = os.path.join(output_dir, f"{filename}.txt")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("POST\\n")
        f.write("="*50 + "\\n\\n")
        f.write(social["post"])
        f.write("\\n\\n")
        f.write("COMMENTAIRE ÉPINGLÉ\\n")
        f.write("="*50 + "\\n\\n")
        f.write(social["comment"])

    img_path = os.path.join(output_dir, f"{filename}.png")

    generate_apple_terminal_image(
        title=BADGES.get(topic[0]),
        code_snippet=topic[3],
        output_path=img_path
    )

    return {
        "text": txt_path,
        "image": img_path
    }


# ─────────────────────────────────────────
# LEADERBOARD PLACEHOLDER
# ─────────────────────────────────────────

leaderboard = []

def update_leaderboard(username, score):
    leaderboard.append({
        "username": username,
        "score": score,
        "date": datetime.now().isoformat()
    })

    leaderboard.sort(key=lambda x: x["score"], reverse=True)

    with open("leaderboard.json", "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, indent=2)


# ─────────────────────────────────────────
# PERFORMANCE ANALYZER
# ─────────────────────────────────────────

def analyze_top_posts(metrics_path="metrics.json"):
    """
    Analyze top performing posts
    """

    if not os.path.exists(metrics_path):
        return []

    with open(metrics_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    ranked = sorted(
        data,
        key=lambda x: x.get("reactions", 0) + x.get("comments", 0),
        reverse=True
    )

    return ranked[:10]




# ─────────────────────────────────────────
# UX UPGRADE V6
# ─────────────────────────────────────────

PROGRESSION_TOTAL = 365

REACTIONS = [
    ("❤️", RED),
    ("😮", BLUE),
    ("😂", YELLOW),
    ("🔥", GREEN),
]

def generate_compact_post(topic, day_number=1):
    ttype, short, hook, snippet, options, correct_idx, answer, explanation, tip = topic

    return f"""⚡ Codebog #{day_number:03d}

👇 Vote avec une réaction"""

def render_reaction(draw, x, y, emoji, label, font, emoji_font=None):
    if emoji_font:
        draw.text((x, y), emoji, font=emoji_font, fill=WHITE)
        draw.text((x + 55, y), label, font=font, fill=(220,220,220))
    else:
        draw.text((x, y), f"{emoji}  {label}", font=font, fill=(220,220,220))

def generate_apple_terminal_image(
    title,
    code_snippet,
    options=None,
    hook=None,
    output_path="output.png",
    day_number=1
):

    width, height = 1080, 1080

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    try:
        hook_font = ImageFont.truetype("DejaVuSansMono.ttf", 30)
        code_font = ImageFont.truetype("DejaVuSansMono.ttf", 56)
        option_font = ImageFont.truetype("DejaVuSans.ttf", 30)
        small_font = ImageFont.truetype("DejaVuSans.ttf", 24)
        logo_font = ImageFont.truetype("DejaVuSans.ttf", 42)
        emoji_font = ImageFont.truetype("DejaVuSans.ttf", 32)
    except:
        hook_font = ImageFont.load_default()
        code_font = ImageFont.load_default()
        option_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
        logo_font = ImageFont.load_default()
        emoji_font = None

    margin = 28

    # Hook
    if hook:
        draw.text(
            (50, 45),
            hook,
            fill=WHITE,
            font=hook_font
        )

    badge = f"⚡ JS #{day_number:03d}"

    badge_bbox = draw.textbbox((0,0), badge, font=small_font)

    bw = badge_bbox[2] - badge_bbox[0] + 28
    bh = badge_bbox[3] - badge_bbox[1] + 14

    bx = width - bw - 40
    by = 40

    draw.rounded_rectangle(
        (bx, by, bx+bw, by+bh),
        radius=14,
        outline=GREEN,
        width=2
    )

    draw.text(
        (bx + 14, by + 7),
        badge,
        fill=GREEN,
        font=small_font
    )

    # Terminal
    terminal_x = margin
    terminal_y = 120
    terminal_w = width - margin * 2
    terminal_h = 520

    draw.rounded_rectangle(
        (terminal_x, terminal_y, terminal_x + terminal_w, terminal_y + terminal_h),
        radius=26,
        fill=CODEBG,
        outline=(35,35,40),
        width=2
    )

    titlebar_h = 58

    draw.rounded_rectangle(
        (terminal_x, terminal_y, terminal_x + terminal_w, terminal_y + titlebar_h),
        radius=26,
        fill=TITLEBAR
    )

    dots = [
        (RED, terminal_x + 22),
        (YELLOW, terminal_x + 50),
        (GREEN, terminal_x + 78),
    ]

    for color, x in dots:
        draw.ellipse((x, terminal_y + 18, x + 16, terminal_y + 34), fill=color)

    draw.text(
        (terminal_x + terminal_w/2 - 70, terminal_y + 16),
        "codebog",
        fill=GRAY,
        font=small_font
    )

    # Code huge
    code_y = terminal_y + 120

    wrapped = textwrap.fill(code_snippet, width=20)

    draw.multiline_text(
        (terminal_x + 50, code_y),
        wrapped,
        fill=WHITE,
        font=code_font,
        spacing=24
    )

    # Options
    options_y = 690

    if options:
        box_w = 470
        box_h = 86
        gap = 18

        positions = [
            (50, options_y),
            (560, options_y),
            (50, options_y + box_h + gap),
            (560, options_y + box_h + gap),
        ]

        for i, opt in enumerate(options[:4]):
            x, y = positions[i]

            draw.rounded_rectangle(
                (x, y, x + box_w, y + box_h),
                radius=18,
                outline=(45,45,55),
                width=2,
                fill=(14,14,18)
            )

            render_reaction(
                draw,
                x + 18,
                y + 22,
                REACTIONS[i][0],
                opt,
                option_font,
                emoji_font
            )

    # Bottom separator
    draw.line(
        (50, 920, 1030, 920),
        fill=(28,28,35),
        width=1
    )

    # Footer
    draw.text(
        (50, 940),
        "⏱️ 10 sec • Réagis avant de lire les commentaires",
        fill=GRAY,
        font=small_font
    )

    draw.text(
        (50, 985),
        "code",
        fill=WHITE,
        font=logo_font
    )

    draw.text(
        (160, 985),
        "bog",
        fill=GREEN,
        font=logo_font
    )

    draw.text(
        (260, 995),
        "• learning.itmade.fr",
        fill=DIMGRAY,
        font=small_font
    )

    draw.text(
        (920, 995),
        f"{day_number}/{PROGRESSION_TOTAL}",
        fill=DIMGRAY,
        font=small_font
    )

    img.save(output_path)

def export_facebook_package(topic, day_number=1, output_dir="facebook_exports"):
    os.makedirs(output_dir, exist_ok=True)

    filename = topic[1].replace(" ", "_").replace("/", "_").lower()

    txt_path = os.path.join(output_dir, f"{filename}.txt")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(generate_compact_post(topic, day_number))

    img_path = os.path.join(output_dir, f"{filename}.png")

    generate_apple_terminal_image(
        title=BADGES.get(topic[0]),
        code_snippet=topic[3],
        options=topic[4],
        hook=topic[2],
        output_path=img_path,
        day_number=day_number
    )

    return {
        "text": txt_path,
        "image": img_path
    }


# =========================================================
# ACTIVE RENDER ENGINE V6
# =========================================================

ACTIVE_RENDER_VERSION = "V6_SOCIAL_UX"

def generate_post_image(topic, day_number=1, output_dir="facebook_exports"):
    """
    Main active renderer used by the generator.
    """
    os.makedirs(output_dir, exist_ok=True)

    filename = topic[1].replace(" ", "_").replace("/", "_").lower()

    img_path = os.path.join(output_dir, f"{filename}.png")

    generate_apple_terminal_image(
        title=BADGES.get(topic[0]),
        code_snippet=topic[3],
        options=topic[4],
        hook=topic[2],
        output_path=img_path,
        day_number=day_number
    )

    return img_path

print("✅ ACTIVE RENDER ENGINE:", ACTIVE_RENDER_VERSION)





# =========================================================
# CODEBOG PREMIUM SOCIAL RENDERER
# =========================================================

PROGRESSION_TOTAL = 365

REACTION_EMOJIS = ["❤️", "😮", "😂", "🔥"]

def load_font(name, size):
    try:
        return ImageFont.truetype(name, size)
    except:
        return ImageFont.load_default()

def generate_premium_post_image(topic, day_number=1, output_path="premium.png"):
    ttype, short, hook, snippet, options, correct_idx, answer, explanation, tip = topic

    width, height = 1080, 1080

    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    # Fonts
    badge_font = load_font("DejaVuSansMono.ttf", 28)
    hook_font_big = load_font("DejaVuSans.ttf", 72)
    hook_font_green = load_font("DejaVuSans-Bold.ttf", 84)
    terminal_title_font = load_font("DejaVuSansMono.ttf", 24)
    code_font = load_font("DejaVuSansMono.ttf", 74)
    option_font = load_font("DejaVuSansMono.ttf", 30)
    emoji_font = load_font("DejaVuSans.ttf", 56)
    footer_font = load_font("DejaVuSans.ttf", 22)
    logo_font = load_font("DejaVuSans.ttf", 54)
    cta_font = load_font("DejaVuSansMono.ttf", 26)

    # Background subtle grid
    for y in range(0, height, 6):
        draw.line((0, y, width, y), fill=(12,12,13))

    # Badges
    draw.rounded_rectangle(
        (32, 34, 355, 102),
        radius=18,
        outline=GREEN,
        width=2
    )

    draw.text(
        (52, 50),
        "⚡ JS CHALLENGE" if ttype == "JS" else "🧠 ALGO CHALLENGE",
        fill=GREEN,
        font=badge_font
    )

    prog = f"#{day_number:03d} / {PROGRESSION_TOTAL}"

    draw.rounded_rectangle(
        (820, 34, 1048, 102),
        radius=18,
        outline=GREEN,
        width=2
    )

    draw.text(
        (850, 50),
        prog,
        fill=GREEN,
        font=badge_font
    )

    # Hook
    draw.text((36, 138), "90% des devs JS", fill=WHITE, font=hook_font_big)
    draw.text((36, 236), "se trompent", fill=GREEN, font=hook_font_green)
    draw.text((525, 236), "sur cette ligne.", fill=WHITE, font=hook_font_big)

    # Terminal
    tx, ty = 32, 334
    tw, th = 1016, 350

    draw.rounded_rectangle(
        (tx, ty, tx+tw, ty+th),
        radius=28,
        fill=(10,10,12),
        outline=(48,48,58),
        width=2
    )

    title_h = 78

    draw.rounded_rectangle(
        (tx, ty, tx+tw, ty+title_h),
        radius=28,
        fill=(16,16,18)
    )

    # Mac dots
    draw.ellipse((58, 360, 88, 390), fill=RED)
    draw.ellipse((108, 360, 138, 390), fill=YELLOW)
    draw.ellipse((158, 360, 188, 390), fill=GREEN)

    draw.text(
        (470, 360),
        "js.js — codebog",
        fill=(120,120,125),
        font=terminal_title_font
    )

    # Left neon bar
    draw.rectangle((34, 448, 46, 628), fill=GREEN)

    # Line number
    draw.text((62, 430), "1", fill=(90,90,100), font=hook_font_big)

    # Syntax highlight
    code_y = 500

    x = 84

    parts = [
        ("console", GREEN),
        (".log", WHITE),
        ("(", WHITE),
        ("typeof null", PURPLE),
        (")", WHITE)
    ]

    for text_part, color in parts:
        draw.text((x, code_y), text_part, fill=color, font=code_font)
        bbox = draw.textbbox((x, code_y), text_part, font=code_font)
        x = bbox[2]

    # Answers
    answers_y = 710

    positions = [
        (32, answers_y),
        (550, answers_y),
        (32, answers_y + 126),
        (550, answers_y + 126),
    ]

    for i, opt in enumerate(options[:4]):

        px, py = positions[i]

        draw.rounded_rectangle(
            (px, py, px+486, py+104),
            radius=18,
            fill=(12,12,16),
            outline=(48,48,58),
            width=2
        )

        draw.text(
            (72, py + 18),
            REACTION_EMOJIS[i],
            font=emoji_font,
            fill=WHITE
        )

        draw.text(
            (188, py + 34),
            opt,
            fill=WHITE,
            font=option_font
        )

    # CTA
    cta_y = 968

    draw.rounded_rectangle(
        (32, cta_y, 1048, cta_y + 100),
        radius=18,
        outline=GREEN,
        width=2
    )

    draw.text(
        (130, cta_y + 30),
        "↓",
        fill=GREEN,
        font=hook_font_green
    )

    draw.text(
        (250, cta_y + 28),
        "RÉAGIS",
        fill=GREEN,
        font=cta_font
    )

    draw.text(
        (420, cta_y + 28),
        "AVANT DE LIRE LES COMMENTAIRES !",
        fill=WHITE,
        font=cta_font
    )

    # Footer
    fy = 1115

    draw.line((32, 1088, 1048, 1088), fill=(22,80,40), width=1)

    draw.text((36, 1110), "code", fill=WHITE, font=logo_font)
    draw.text((162, 1110), "bog", fill=GREEN, font=logo_font)

    img = img.crop((0, 0, 1080, 1080))

    img.save(output_path)


# MAIN EXPORT
def export_premium_post(topic, day_number=1, output_dir="premium_posts"):
    os.makedirs(output_dir, exist_ok=True)

    filename = topic[1].replace(" ", "_").replace("/", "_").lower()

    output_path = os.path.join(output_dir, f"{filename}.png")

    generate_premium_post_image(
        topic,
        day_number=day_number,
        output_path=output_path
    )

    return output_path