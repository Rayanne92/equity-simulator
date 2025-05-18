# Equity Simulator

**Equity Simulator** est une application Python qui permet aux traders de simuler différents scénarios de leur stratégie de trading, en visualisant l'impact potentiel sur leurs courbes d'equity. Cet outil aide à mieux comprendre les résultats possibles, la gestion des risques, et à ajuster les stratégies en conséquence.

---

## Fonctionnalités

- Saisie des paramètres clés :
  - Capital initial
  - Taux de réussite moyen (%)
  - Ratio Risque / Récompense (RRR)
  - Nombre de trades par simulation
  - Nombre de scénarios simulés
  - Méthode de gestion du risque (risque en % ou montant fixe)
  - Valeur de risque par trade

- Simulation Monte-Carlo basée sur ces paramètres
- Visualisation interactive des scénarios de courbes d’equity via un graphique Plotly (ouverture dans navigateur)
- Statistiques détaillées à la fin de chaque simulation :
  - Equity minimale et maximale
  - Nombre maximal de trades gagnants et perdants
  - Drawdown maximal, moyen et individuel

---

## Installation

1. Cloner ce dépôt :

```bash
git clone https://github.com/ton-utilisateur/equity-simulator.git
cd equity-simulator
```

2. Installer les dépendances Python :

```bash
pip install -r requirements.txt
```

Le fichier ```requirements.txt``` doit contenir :

```nginx
plotly
pandas
```