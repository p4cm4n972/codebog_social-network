"""
Configuration et constantes pour le générateur de posts Codebog.
"""
from datetime import date

# ─────────────────────────────────────────
# DATES ET SORTIES
# ─────────────────────────────────────────
START_DATE = date(2026, 5, 5)
END_DATE   = date(2026, 12, 31)
OUTPUT_DIR = "posts_output"

# ─────────────────────────────────────────
# DIMENSIONS
# ─────────────────────────────────────────
IMG_W, IMG_H = 1080, 1080

# ─────────────────────────────────────────
# COULEURS
# ─────────────────────────────────────────
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
    "Combien de temps pour trouver l'output ?",
    "Cette question trompe les seniors.",
    "Devine l'output sans exécuter le code.",
    "Trick question des meilleurs codeurs.",
    "90% des juniors échouent sur cette ligne.",
    "Connais-tu vraiment les bases ?",
    "Output ? Tu as 10 secondes.",
    "Ça paraît facile… mais regarde bien.",
    "Quelle est ta réponse ?",
]

CTA = {
    "JS": "💻 Besoin de t'entraîner en JavaScript ? → codebog.itmade.fr",
    "ALGO": "🧠 Tu veux progresser en algorithmique ? → learning.itmade.fr"
}

# ─────────────────────────────────────────
# EMOJIS EMBARQUÉS (Base64)
# ─────────────────────────────────────────
EMOJI_B64 = {
    "heart": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAACyElEQVR4nO2d23HbMBBFbzTuwSnIKcCVpoCkoKQK5SdMNBBBLsB9Qvd8yha4uIdLkJiRBBBCCCGEEEIIIYS48cVq4Pv7x11UwO+fZjVIiK5TdVDpZHp4ychUp8pAVyfUYiUiY52XBtCeUIuWiMx13mbfaD0prWNkr3NKgMekNI5Voc7h1pk60K8fn7uvf/32XTrEaJt7hv/IaJ22k+oF3yIUIZ1cVPgbIxLE/zg0KWnwLQIRZ5OLDn9DKkG0BriEL3zvUS1ZwgfktZwKyDSpjb2aqtTZMn0busuVs19zjEIcCsh4Vm081Valzj10O4AM0xWQ+azauL9/3KvU2fubbgcMPFiZjlGIXQEVzqpq9DLVXwOunMEvdvYDwJvJqFuQylsRK/L0uGxy+VHYjFuFdovCpgNaXjBoKXwOCIYCgqGAYCggmH8rMh++fNnuhm7tC8Sex6xvvT8QG9qMuQYEQwHBPAngZciOvWzZAcFQQDC7AngZ0qeXKTsgmK4AdoEeR1myA4I5FMAuuM5ZhuyAYE4FsAvmkWQn6gBKGEf18wEjA5KxrIbWAEo4ZzSj4UWYEvrMZDN1F0QJz8xmMn0bSgn/uZJFia8CyEr4d0W0vIqIdN+W0rKqCIvLrslWxIrrg9WczPaCVpRggelm3CoSLOdhvhtaXYJ1/dyOPsDj5HERULELvGp264BKEjxrdb0EVZLghfsakF2Cd30hi3BWCRF18S7oL1EnRZiATF0QWUtoB2SSEEX4JShaQvTxwwUAcSFEhw8kEQD4h5EhfCCRAE+yhA8kE+ARTKbwgWQCgHwBWZNOAGD4ey0J5aYUAOiHlTF8ILEAQC+0rOEDyQVokDl8oICA7AFeJb0AYF5CBXklBAATv81SIHygkABAHmqV8IFiAoDzcCuFDxQUcES18IGiAioG3aOkAOBZwkpSSrHqZxEIIYSszx+Tjilez5QCQwAAAABJRU5ErkJggg==",
    "astonished": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAEnUlEQVR4nO1dOVJcMRBtKJcTnHIFJ06nyonxUSalfAdfxKmPYghJnfgKpJCQ4EgzGo2WVqs3/dHLYP6XWu+pW8vXArBgiitrA7B4eYT33nc+ffNfPpcGUsjGwpsoLozBEH5ze9ed7uvzQ/MZa0FMMy8RTyEbi5IoVkKoZ2pBegkexFDLKEe8Bekl5MTQEEJFgJR8T8SnSIWQFkE08ZmIT6ElhJgAMfkzEZ8iFkJCBPYEt0J8CikhrrkSAtgu+QCn5eEcKLIJsGXyAyREYHGlYExK/P7+rfre718fObIfBsXOEJJGw9GwACn5rcKUoC0Gh50cIgwJEJNPLVAKaSG47RwVgSxAIP/Hz6/FZ1pk1sjgFmIkr9a7IyKQBKiRTyUuV0guETjTLqVFFeFDrwGnMf9ozChZ4X2uENHKZ/T91M6b2zt4fX6Al0d47xGhS61Sb2fhiF5PQI8DJL9SbRFYvroHYqv219HLD0qAFXr6EHjCeEFTgEU+DVgRuntBJHz+U//933cVM87gwK5qSz1c+1sFTKElhKJdrV5RUYCh2c3eAqaQEsLArtZ3hGYboE4+VxoSaRLSaPGXFYDc5+ckboNp5XjNhiBS7EcYttvtTv5+enpqpzsajpzYVWoLVHpBaQHT/6MKLAAPdp2FIO7aXyok+pmR8OHIrtK4gPWjfApMISnPjsKTXScCkBpfiR4LRx5e7YJTnrMewDHtQKk5Gl5gaVeOV9EQtNDGEsAYBwHWrKcO0t7Q8gBjiAlAGcRoDHy82TUugMYUMiUPr3YlEA1BPTVHczrCk11XAEwN8MCwv1pIwck4S7vC5JzKZFwoCGnWURAe7OLzAAD+4T9XHHdoV/AA3jaAs+G7hLRAohHmMFCiB+PULpk2IBjqbVWEQ7tkG2FsgbXXBTmyS2dhltXCqxYc2LXmgoyxBDCGTghixCxbX7GYRgDs1qXw3CxCuBeAumdsFiGuAY6rtTBnrGmCY8Oe9KY/CuJVcm49oLo390t+FnP/Nz+Jtr9/c+sJh3WKnr4Jl8gvEX/2fkEILyLEHuBOgOxGaCTxZ2llhPAgQiyAq3EAJ/mld721CQcBrBtibvJraViKkC5Td+UBMTjIl0iLGy4EsKiRXkJRVgDr8YBEjfXgBTleTwSwPsj6UhDzbB6CLEOBhzB0JoB1b0gyVFiGodImPXMPuHRUBbBujLeCGo9ZAVZjLAPSUQXLC8bQ4q8owPICXpT4rHqAdY9odmAO8HPXCyrN5XtPm4qmANJeYDk/L5k39vhKlAesUNSHnrNDu0OQhggSoUIr/PTygxZAsldkEYak82Q/OTdOdDYv0K79PZW1OwRJiZCrkRzEaX2Yp56eTuqGziKCd/IBGG/Q4MRM64LMbtAI0BYBoH9lHIBP8gGEb1Eahed7adzcohQgdY/YqAjc5HPfqMfat5e8zK1XCMlaD8A3LpruLkmrHTJSd0mu21QbmO421RjrPuE21o3aCTZ1o3aMdad8HurffUun81qIUZpK0fwebvrh3UIMD6THcLHyAXNmNUUUzGSh9eoPFwKkkLy1z5rwFK6MqYEiijeyc/gP166ChkA7XfoAAAAASUVORK5CYII=",
    "joy": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAEcUlEQVR4nO2dv24UMRDG5yJECtLyBogGiYoyIFHxFulOPEGegg7RoHR5i1RIkJKWBt0b0IYCmlAEJ16f7Z1/3vF551cll9zu+Ptsr9fr9QA4pmysA8Bycw231O+cnPZfvi4D5IiNpTdTuggGI/iTp6/Jx/3969vs/1gbYnrykvAcsbGUTLEyYvGTWoheogczFjtRTngL0UvkzFjCiEUMSMXvSfiU1IjWJjQ9+CEJn7KUEc0MiMU/JOFTYiNamKB+wFGET2llxJHWgQDGFR9gWh7NG0U1A0YWP9DCBJWmFIIZVfgcoUuSdkfiFrBG8QEeyittCSID1ip+QMMEtgFrFz8gNYFlgIs/RWIC2QAXPw/XBJIBLn4djgloA1o+pRoRrF7kLshrfx2qPigDvOuhQemKZg1w8XlgTVCdjHPoVA3w2i8D0woelf6gOeo5e/+3+vfLz4+1TkViybhuruE2N3FXnMmT1v65wpVobYZFXLWZ02wXJK393EJKv9vy2Bpx5XStXgM4tV8j0BYmWMZV0zHbBXG7n1qApSbM+Q6VHuIqdUN7BmiKTw1U4xgtjqkVV84ElfsArQBz39Hut3uIK2ZigNbQU1JrW46Ceokr1jnbAijdT1oTNAJNj8GpbT3GldPVpyKMKd4JY9juruD4/O7nPx/easRzMByffwEAgO0O4OLZO/Zx7q/G1NHPdne195kkkENCWvZ4NMTqgnIB1D4fCe2y+zXAGDfAGDfAmCMAf/CyNPGDGlYLKF3x1zAK0i47uwtKT7gG8QOaZd8AeBdkQbgX8IuwMW6AMeK5oMCargEAemVnt4D01nsN0xABzbL7XBARnwsaDDfAGDfAGJ+KINJkKiKsU8HssVY64RrED0jLHj8RYz+SdPiIH0k6ergBxrSfinj+VXKKPvj5Zu8j9akI6oXYpyLKv9dIF+j6VAQRn4oYjKwBlPsBB09O18lF+OQUNtgl6ula0MsXr/7/9HL6j58IEfbKx4cyXcDdYtizH98n/xLWimJQf0HD4bNnAGY0tKZpByxzmpTeEVNrAWmTHBnNslYNqLUCq7fbe2ROi5qOWQO4e2GuoRVIyoh+Uz7GW0EdSe0HqBjgrWAf7doPgNi6GPOcIPs+7v19wRjkxMfW/lplVhkFZV9kHqglcMTHMmsAdpZ0VBO44mM390b389hHlqWXlw+tSypVHk3xARgGAPBNAOjfiFqrpYgPoGwAAO3B/ex2YJ0ZMdddYvt8al4B8lCTunqidyO0hAfgJXVgjfW1TYhpbQhlYNBafABBChPOOiL2hnlMU7ijMOoQU5LORJT/pMXWZpZobkWGRZzEx2p7Sy1abUeJaussSkuZoXEXq5VFSS0jXMs8Yj1tAqudUU81leHoydxapDNUfSgfBzXa0pZWuSQ9m+oMB5dNNcbzCc/jGbUThsqoHeM55fMsZkCgtPTRwozSQGEJ4QOLGxBjYUYPoseYGhDALAjmmIIZClsJH+jCgJSWWfusBU/pKpgaHFN6EzvHP858bTstmHbXAAAAAElFTkSuQmCC",
    "fire": "iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAADSUlEQVR4nO1dW07DQBDbIC6GxBm4Ax+cph/cgTMgcTT4WqlUabPztKcdf0JJHHs8swlLGKPRsOD3Y/yiOVjwhCZgwRS/sgllDbgUvaoJG5qAFCtCb6c611UqAatVXikNZQyQilrFhBIGaMWsYAK9AVYR2U2gHVYRwjEOZ8oERFUtYxroDIgWic0EKgOyxGEygcaAbFFYTIAPJQYhkMMZmgAG8cfA8oAZwCL+BIoPxADXi/16dTsUwoR0A0LEL2xC2vBxv7A90d++XU+RMZxTEpAi/q2vK5GRhnAD0sRf/b4Q0SaEGpAuvvRzBKC5Ez6EVNQigznMAIqlZoEk8CfAKqKTCVEpCFlmuZD1rl6HJWrEspQzARGtw+GYESlwN8BMMrJvE84ErgRkCGQ8h3cKXA0wkcusTqIkcCQAIYjhnJ4pcDNATQpZjQRJwCaAQAAtB68UuBigIsMg/gSQC8cMKAqPFJgNKF/9EyBOnQAjrCkwGcC2s6Ei8hPA2H4mACsitQFd/T7oGeAEbUGqDCh517uKZI6dAEdoClNsQPd+X+QloEL7mUji/Cz58HYaG7wN/RxsL3nBmi3duiIyAIIjwY8+DzbkCOKNRuIEaKMsFf4IWiOEG7qkCeAcwt7iRx3TAeIWFDoHokWaxw9qS5qti7EJkLSfzAqVnCt4NcTRghDtgaQlxRqwMsCQQqyc2/kP/y6hMsBtmzZDFTpx0GoS34KCKygUCdxxM4Ch+ieAXHIMqJiCJM6YBDBV/wSIk9oA8dCplILgxw/n4LgPeGCYlpOqRxLvljMm4FP+I52AwjAZwPgi1GxYNegEgNEGgNEGgGE24JHngMe1dwLAyDdAsc5OA4CbiwGP2Ia8rtltX9AkBN+4FQzvYnNvQUsEGdvQAqcyL2y6x5YUdU3hQt1sSSwP5m5Uf3Qxha+CKqfhbl5dfPVCGGbBFQ5ZhZNenbstCdWKdsTPTmz6jdjuBSKSQCD+GKBHEXATSMQfA/xPfK6ukKJaErjf754bdeJzpMwFoqr/xwFNYCIsDYRVfw4KEhNLz5CODAE9UtCChsg5wt5UTiT8BOUvZCKEYhS/0Wg0Go1Go9EA4Q+wHjBiPwl2BAAAAABJRU5ErkJggg==",
}

EMOJI_ORDER = ["heart", "astonished", "joy", "fire"]

# Mapping noms -> emojis Unicode pour l'affichage
EMOJI_UNICODE = {
    "heart": "❤️",
    "astonished": "😮",
    "joy": "😂",
    "fire": "🔥"
}
