# Wall Street Pulse

Análisis de noticias financieras bajo incertidumbre — Artículo 3 del curso
**Modelos de Razonamiento bajo Incertidumbre (MRI)**.

El proyecto explora la relación entre el contenido de noticias financieras
(evento de mercado, sector, sentimiento) y el comportamiento observado del
índice asociado (cambio porcentual, volumen de operación).

## Datos

`data/raw/financial_news.csv` — 3,024 noticias financieras, 12 columnas.
`data/raw/dict_financial_news.csv` — diccionario de datos de las 12 columnas.

| Columna | Tipo | Descripción |
|---|---|---|
| `Date` | fecha | Fecha de publicación |
| `Headline` | texto | Titular de la noticia (~5% nulos) |
| `Source` | texto | Medio (Reuters, Bloomberg, CNBC, Financial Times…) |
| `Market_Event` | categórica | Evento de mercado que origina la noticia |
| `Market_Index` | categórica | Índice asociado (S&P 500, DAX, FTSE 100…) |
| `Index_Change_Percent` | float | Cambio % del índice, rango −5 a +5 (~5% nulos) |
| `Trading_Volume` | float | Volumen en millones (1M–500M) |
| `Sentiment` | categórica | Positive / Neutral / Negative (~5% nulos) |
| `Sector` | categórica | Sector afectado |
| `Impact_Level` | categórica | High / Medium / Low |
| `Related_Company` | texto | Empresa mencionada |
| `News_Url` | texto | URL de la fuente (~5% nulos) |

> Hay nulos en `Sentiment`, `Index_Change_Percent`, `Headline` y `News_Url`
> (~5% cada uno). Conviene decidir explícitamente cómo tratarlos antes de
> modelar, ya que `Sentiment` es una variable central del análisis.

## Requisitos

- [uv](https://docs.astral.sh/uv/) ≥ 0.12.8
- Python 3.12 (uv lo instala solo si no está presente)

## Instalación

```bash
git clone https://github.com/JuanPVenegas13/Wall-Street-Pulse.git
cd Wall-Street-Pulse
uv sync --dev
```

`uv sync --dev` crea el entorno e instala las dependencias exactas de
`uv.lock`, incluido `ipykernel` para los notebooks.

### Entorno fuera de OneDrive (importante en Windows)

El repositorio vive dentro de una carpeta sincronizada con OneDrive. OneDrive
convierte los archivos del entorno virtual en *placeholders* (reparse points)
con **Files On-Demand**, y entonces `uv` falla al reemplazar paquetes con:

```
error: failed to remove directory ...dist-info: Access is denied. (os error 5)
```

Por eso el entorno **no** se crea en `.venv/` dentro del proyecto, sino fuera
del área sincronizada. La variable ya está configurada a nivel de usuario:

```powershell
[Environment]::SetEnvironmentVariable(
  'UV_PROJECT_ENVIRONMENT',
  "$env:USERPROFILE\.venvs\wall-street-pulse",
  'User'
)
```

Si `uv` vuelve a fallar con `os error 5`, es que el entorno se creó dentro de
OneDrive: verifica la variable, borra `.venv/` y repite `uv sync --dev`.

## Uso

```bash
# Abrir los notebooks (VS Code usa el kernel del entorno automáticamente)
code notebooks/01_analysis_eda.ipynb

# Ejecutar un script dentro del entorno
uv run python -c "import pandas as pd; print(pd.read_csv('data/raw/financial_news.csv').shape)"

# Agregar una dependencia de análisis / de desarrollo
uv add scikit-learn
uv add --dev nbstripout
```

En VS Code, el kernel debe apuntar a
`%USERPROFILE%\.venvs\wall-street-pulse\Scripts\python.exe`
(ya preconfigurado en `.vscode/settings.json`).

Los notebooks se ejecutan con la **raíz del proyecto** como directorio de
trabajo, así que las rutas relativas se escriben desde ahí:

```python
import pandas as pd
df = pd.read_csv("data/raw/financial_news.csv")
```

## Estructura

```
Wall-Street-Pulse/
├── data/
│   ├── raw/            # datos fuente (versionados)
│   ├── interim/        # intermedios (ignorados por git)
│   └── processed/      # datos listos para modelar (ignorados)
├── notebooks/
│   └── 01_analysis_eda.ipynb
├── src/art3_wall_street/   # código reutilizable, instalado como paquete
├── pyproject.toml
└── uv.lock             # versiones exactas — sí se versiona
```

`src/art3_wall_street/` se instala en modo editable, así que desde cualquier
notebook se puede importar sin tocar `sys.path`:

```python
from art3_wall_street import ...
```

`data/interim/` y `data/processed/` se ignoran porque son derivados: se
regeneran desde `data/raw/`. Sus carpetas se conservan con `.gitkeep`.

## Notas de trabajo con notebooks

Los `.ipynb` guardan las salidas de cada celda dentro del JSON, incluidas las
imágenes de las gráficas en base64. Eso hace los diffs ilegibles y engorda el
repositorio. Para evitarlo:

```bash
uv add --dev nbstripout
uv run nbstripout --install
```

Limpia las salidas al hacer commit, sin alterar lo que ves en el editor.
