"""Reproduce las figuras del cuaderno notebooks/01_analysis_eda.ipynb.

Se ejecuta desde la raíz del repositorio:

    python paper/render_figs.py

Deja los PNG en paper/figs/, que es de donde los toma el .tex.
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/raw/financial_news.csv")
orden = ["Low", "Medium", "High"]
OUT = "paper/figs"

# --- Celda 6: distribución de la variable objetivo y del sentimiento ---
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.countplot(data=data, x="Impact_Level", order=orden, ax=axes[0])
sns.countplot(data=data, x="Sentiment", ax=axes[1])
plt.tight_layout()
fig.savefig(f"{OUT}/eda_distribuciones.png", dpi=200, bbox_inches="tight")
plt.close(fig)

# --- Celda 11: indicadores numéricos por nivel de impacto ---
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
sns.boxplot(data=data, x="Impact_Level", y="Index_Change_Percent", order=orden, ax=axes[0])
sns.boxplot(data=data, x="Impact_Level", y="Trading_Volume", order=orden, ax=axes[1])
plt.tight_layout()
fig.savefig(f"{OUT}/eda_numericas.png", dpi=200, bbox_inches="tight")
plt.close(fig)
