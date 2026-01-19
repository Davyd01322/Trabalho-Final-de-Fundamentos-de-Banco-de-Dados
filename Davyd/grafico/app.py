import panel as pn
from data import carregar_estado
from plots import bar_visitas

pn.extension()
categoria = pn.widgets.Select(
    name="Categoria",
    options=["","Péssimo","Ruim","Regular", "Bom", "Otimo"]
)

def atualizar_bar(cat):
    if cat:
        p = cat
    else:
        p = None
    
    df = carregar_estado(p)
    return bar_visitas(df)

app = pn.Column(
    "# Gráfico de visitas (SQL + Panel)",
    pn.bind(atualizar_bar, categoria)
)

app.servable()