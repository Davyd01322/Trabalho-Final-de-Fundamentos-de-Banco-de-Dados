import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = os.getenv("DB_PORT", "5432")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def carregar_visitas_por_data():
    sql = """
        select
            data_::date as data,
            count(*) as total
        from public.visita_cultural
        group by data
        order by data
    """

    df = pd.read_sql(sql, engine)

    if df.empty:
        return df

    # evita bug do hvplot
    df["data"] = df["data"].astype(str)

    return df
