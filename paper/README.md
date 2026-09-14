# Artículo

Clasificación del impacto de noticias financieras con naïve Bayes multinomial.

## Compilar

```bash
cd paper
pdflatex articulo_wall_street_pulse.tex && pdflatex articulo_wall_street_pulse.tex
```

Requiere `texlive-lang-spanish` (paquete `babel-spanish`).

## Regenerar las figuras

Las dos figuras de `figs/` son las que produce el cuaderno
`notebooks/01_analysis_eda.ipynb`. Para volver a generarlas, desde la raíz del
repositorio:

```bash
python paper/render_figs.py
```

Dependencias: `pandas`, `matplotlib`, `seaborn`.
