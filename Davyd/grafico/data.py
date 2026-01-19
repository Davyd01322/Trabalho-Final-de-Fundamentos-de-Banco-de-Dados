import pandas as pd
from db import get_conn

def carregar_estado(estado=None):
    sql = """
            SELECT estado_conservacao, COUNT(*) AS total_visitas
            FROM patrimonio
    """
    
    params = []
    if estado:
        sql += "WHERE estado_conservacao = %s"
        params.append(estado)
    
    sql += "GROUP BY estado_conservacao"

    with get_conn() as conn:
        return pd.read_sql(sql, conn, params=params)