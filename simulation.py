# simulation.py

import numpy as np

def run_simulation(
    capital: float,
    winrate: float,
    rrr: float,
    num_trades: int,
    num_simulations: int,
    risk_type: str,
    risk_value: float
):
    all_equities = []
    all_drawdowns = []

    for _ in range(num_simulations):
        equity = [capital]
        max_equity = capital
        wins_streak = 0
        losses_streak = 0
        max_win_streak = 0
        max_loss_streak = 0
        peak = capital
        dd_list = []

        for _ in range(num_trades):
            if risk_type == "Pourcentage":
                risk = equity[-1] * (risk_value / 100)
            else:  # Montant fixe
                risk = risk_value

            is_win = np.random.rand() < (winrate / 100)

            if is_win:
                pnl = risk * rrr
                wins_streak += 1
                losses_streak = 0
            else:
                pnl = -risk
                losses_streak += 1
                wins_streak = 0

            max_win_streak = max(max_win_streak, wins_streak)
            max_loss_streak = max(max_loss_streak, losses_streak)

            new_equity = equity[-1] + pnl
            equity.append(new_equity)

            # Drawdown calcul
            peak = max(peak, new_equity)
            dd = (peak - new_equity)
            dd_list.append(dd)

        all_equities.append(equity)
        all_drawdowns.append(dd_list)

    # Moyenne des courbes
    equity_matrix = np.array(all_equities)
    mean_equity = np.mean(equity_matrix, axis=0)

    # Statistiques globales
    min_equity = np.min(equity_matrix[:, -1])
    max_equity = np.max(equity_matrix[:, -1])
    max_drawdowns = [max(dd) for dd in all_drawdowns]
    avg_drawdowns = [np.mean(dd) for dd in all_drawdowns]

    stats = {
        "Equity minimale": round(min_equity, 2),
        "Equity maximale": round(max_equity, 2),
        "Drawdown max": round(max(max_drawdowns), 2),
        "Drawdown moyen": round(np.mean(avg_drawdowns), 2),
        "Drawdown max individuel": round(np.mean(max_drawdowns), 2),
        "Max trades gagnants": max_win_streak,
        "Max trades perdants": max_loss_streak,
    }

    return {
        "curves": all_equities,
        "mean": mean_equity,
        "stats": stats
    }
