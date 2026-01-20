import hvplot.pandas
import panel as pn

def bar_visitas(df):
    if df.empty:
        return pn.pane.Markdown("Nenhum dado para exibir")

    return df.hvplot.bar(
        x="data",
        y="total",
        title="Visitas por dia",
        height=400,
        width=700
    )
