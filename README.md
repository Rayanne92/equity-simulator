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
git clone https://github.com/Rayanne92/equity-simulator.git
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

## Usage

Lancez l’application avec :

```bash
python main.py
```

## Fonctionnement rapide
1. Saisissez vos paramètres de trading dans l’interface.
2. Cliquez sur "Lancer la simulation".
3. Un graphique interactif s’ouvre dans votre navigateur montrant les différentes courbes d’equity simulées.
4. Les statistiques clés s’affichent sous les paramètres.

## Description mathématique du modèle

L’**Equity Simulator** modélise l’évolution du capital d’un trader à travers une suite de trades, selon les paramètres suivants :

- \( C_0 \) : Capital initial
- \( p \) : Taux de réussite (probabilité de gain)
- \( RRR \) : Ratio Risque/Récompense
- \( n \) : Nombre de trades par simulation
- \( m \) : Nombre de simulations
- \( r \) : Taille du risque par trade (en % ou en montant fixe)

À chaque trade \( i \), on risque \( R_i \) défini par :
\[
R_i = \begin{cases}
r \times C_{i-1} & \text{si risque en pourcentage}\\
r & \text{si risque fixe}
\end{cases}
\]

Le capital évolue ainsi :
\[
C_i = C_{i-1} + 
\begin{cases}
R_i \times RRR & \text{avec probabilité } p \\
- R_i & \text{avec probabilité } 1-p
\end{cases}
\]

En réalisant \( m \) simulations indépendantes, on obtient une distribution des trajectoires \( \{C_i^{(j)}\} \), ce qui permet d’estimer :

- Les valeurs minimales et maximales d’equity
- Le nombre maximal de trades gagnants et perdants
- Les drawdowns maximaux et moyens, définis par :
\[
DD^{(j)} = \max_{1 \leq i \leq n} \left( \max_{1 \leq k \leq i} C_k^{(j)} - C_i^{(j)} \right)
\]

Ce modèle fournit ainsi un outil quantitatif d’évaluation et de gestion du risque pour les stratégies de trading.
