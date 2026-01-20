import panel as pn
from data import carregar_visitas_por_data
from plots import bar_visitas

pn.extension()

def atualizar():
    df = carregar_visitas_por_data()
    return bar_visitas(df)

app = pn.Column(
    "## Gráfico de Visitas (CRUD)",
    pn.bind(atualizar)
)

app.servable()
