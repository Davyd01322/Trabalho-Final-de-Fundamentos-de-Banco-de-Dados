import matplotlib.pyplot as plt

def bar_visitas(df):
    fig, ax = plt.subplots()

    if df.empty:
        ax.text(
            0.5, 0.5,
            "Nenhum dado encontrado",
            ha="center", va="center",
            transform=ax.transAxes
        )
        ax.set_axis_off()
        return fig

    ax.bar(df["estado_conservacao"], df["total_visitas"])
    ax.set_ylabel("Total de Visitas")
    ax.set_xlabel("Estado de Conservação")
    ax.set_title("Distribuição de frequência de visitas\npor estado de conservação")
    ax.tick_params(axis="x", rotation=45)
    return fig