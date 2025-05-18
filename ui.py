# ui.py

import tkinter as tk
from tkinter import ttk, messagebox
from simulation import run_simulation
import plotly.graph_objects as go
import pandas as pd
import tempfile
import os
import webbrowser

def start_ui():
    root = tk.Tk()
    root.title("Equity Simulator")
    root.geometry("1000x700")
    root.configure(padx=20, pady=20, bg="#f8f8f8")

    # === Cadre paramètres ===
    param_frame = tk.LabelFrame(root, text="Paramètres de simulation", padx=10, pady=10, bg="#f8f8f8", font=("Segoe UI", 10, "bold"))
    param_frame.pack(fill="x", pady=10)

    def create_labeled_entry(parent, label_text, row, default=""):
        label = tk.Label(parent, text=label_text, bg="#f8f8f8", font=("Segoe UI", 10))
        label.grid(row=row, column=0, sticky="e", padx=5, pady=5)
        entry = tk.Entry(parent, font=("Segoe UI", 10))
        entry.grid(row=row, column=1, padx=5, pady=5)
        entry.insert(0, default)
        return entry

    # Champs
    capital_entry = create_labeled_entry(param_frame, "Capital initial ($):", 0, "10000")
    winrate_entry = create_labeled_entry(param_frame, "Taux de réussite moyen (%):", 1, "50")
    rrr_entry = create_labeled_entry(param_frame, "Risque / Récompense (RRR):", 2, "2")
    trades_entry = create_labeled_entry(param_frame, "Nombre de trades par simulation:", 3, "100")
    sims_entry = create_labeled_entry(param_frame, "Nombre de scénarios simulés:", 4, "50")

    # Type de risque
    tk.Label(param_frame, text="Méthode de gestion du risque :", bg="#f8f8f8", font=("Segoe UI", 10)).grid(row=5, column=0, sticky="e", padx=5, pady=5)
    risk_type_var = tk.StringVar(value="Pourcentage")
    risk_type_menu = ttk.Combobox(param_frame, textvariable=risk_type_var, values=["Pourcentage", "Montant fixe"], state="readonly", font=("Segoe UI", 10))
    risk_type_menu.grid(row=5, column=1, padx=5, pady=5)

    risk_value_entry = create_labeled_entry(param_frame, "Risque par trade (% ou $):", 6, "1")

    # === Cadre résultats ===
    results_frame = tk.LabelFrame(root, text="Statistiques des simulations", padx=10, pady=10, bg="#f8f8f8", font=("Segoe UI", 10, "bold"))
    results_frame.pack(fill="x", pady=10)

    results_labels = {}
    for i, label in enumerate([
        "Equity minimale", "Equity maximale", "Max trades gagnants",
        "Max trades perdants", "Drawdown max", "Drawdown moyen", "Drawdown max individuel"
    ]):
        tk.Label(results_frame, text=label + " :", bg="#f8f8f8", font=("Segoe UI", 10)).grid(row=i, column=0, sticky="e", padx=10, pady=2)
        var = tk.Label(results_frame, text="-", bg="#f8f8f8", font=("Segoe UI", 10, "bold"))
        var.grid(row=i, column=1, sticky="w")
        results_labels[label] = var

    # === Graphique Plotly ===
    def afficher_graphique_plotly(curves, moyenne):
        df = pd.DataFrame(curves).T
        fig = go.Figure()

        for col in df.columns:
            fig.add_trace(go.Scatter(y=df[col], mode='lines', line=dict(color='gray', width=1), opacity=0.2, showlegend=False))

        fig.add_trace(go.Scatter(y=moyenne, mode='lines', name='Moyenne', line=dict(color='black', width=2)))

        fig.update_layout(title='Simulations d\'Equity',
                          xaxis_title='Trades',
                          yaxis_title='Solde',
                          template='plotly_white')

        # Ouvrir le graphique dans le navigateur temporairement
        tmpfile = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
        fig.write_html(tmpfile.name)
        webbrowser.open("file://" + os.path.realpath(tmpfile.name))

    # === Simulation ===
    def lancer_simulation():
        try:
            capital = float(capital_entry.get())
            winrate = float(winrate_entry.get())
            rrr = float(rrr_entry.get())
            num_trades = int(trades_entry.get())
            num_simulations = int(sims_entry.get())
            risk_type = risk_type_var.get()
            risk_value = float(risk_value_entry.get())

            # Simulation
            result = run_simulation(
                capital,
                winrate,
                rrr,
                num_trades,
                num_simulations,
                risk_type,
                risk_value
            )

            afficher_graphique_plotly(result["curves"], result["mean"])

            stats = result["stats"]
            for key, label in results_labels.items():
                label.config(text=str(stats.get(key, "-")))

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue :\n{e}")

    # === Bouton ===
    run_button = tk.Button(root, text="Lancer la simulation", command=lancer_simulation,
                           bg="black", fg="white", font=("Segoe UI", 11, "bold"), padx=10, pady=5)
    run_button.pack(pady=10)

    root.mainloop()
