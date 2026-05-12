# 🖥️ Codebog Post Generator

> **241 posts Facebook** · 5 mai → 31 décembre 2026  
> 121 challenges JavaScript + 120 challenges Algorithmie

![Codebog](assets/banner.png)

---

## 🚀 Présentation

**Codebog** est une page Facebook de défis quotidiens pour les développeurs.  
Chaque jour, un extrait de code avec 4 options — le format idéal pour l'engagement organique.

| Type | Format | Fréquence |
|------|--------|-----------|
| ⚡ JS Challenge | Jours impairs | 1/jour |
| 🧠 Algo Challenge | Jours pairs | 1/jour |

---

## 📁 Structure du projet

```
codebog/
├── codebog_generator.py   # Script principal
├── requirements.txt       # Dépendances Python
├── assets/
│   └── logo.png           # Logo Codebog
├── posts_output/          # Images PNG générées (gitignored)
├── facebook_exports/      # Packages texte + image (gitignored)
└── scripts/
    └── batch_week.sh      # Génération hebdomadaire
```

---

## ⚙️ Installation

```bash
# Cloner le repo
git clone https://github.com/ton-user/codebog.git
cd codebog

# Installer les dépendances
pip install -r requirements.txt
```

---

## 🎯 Utilisation

```bash
# Générer UN post (image + texte)
python codebog_generator.py --day 1

# Générer une semaine
python codebog_generator.py --range 1 7

# Générer TOUS les posts (241)
python codebog_generator.py

# Exporter le JSON complet
python codebog_generator.py --json

# Exporter le package Facebook complet (image + texte épinglé)
python -c "from codebog_generator import *; export_facebook_package(TOPICS[0])"
```

---

## 📋 Format d'un post

**Image** (1080×1080 PNG) : fenêtre terminal macOS avec le code  
**Texte du post** : hook + code + 4 options de vote par réaction  
**Commentaire épinglé** : réponse + explication + tip + CTA

---

## 📊 Roadmap des phases

| Phase | Jours | Période | Niveau |
|-------|-------|---------|--------|
| 1 | 1–60 | Mai–Juin | Bases JS + Algo simple |
| 2 | 61–120 | Juil–Août | Intermédiaire |
| 3 | 121–180 | Sept–Oct | Avancé |
| 4 | 181–241 | Nov–Déc | Expert / Entretiens GAFAM |

---

## 🔗 Liens

- 🌐 [learning.itmade.fr](https://learning.itmade.fr) — Algorithmie
- 🌐 [codebog.itmade.fr](https://codebog.itmade.fr) — JavaScript
- 📘 [facebook.com/codebog](https://facebook.com/codebog)

---

## 📄 Licence

MIT — ITMade SASU © 2026
