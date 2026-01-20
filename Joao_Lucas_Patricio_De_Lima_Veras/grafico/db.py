import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="patrimonios",
        user="postgres",
        password="jl12345678",
        host="localhost",
        port=5432
    )