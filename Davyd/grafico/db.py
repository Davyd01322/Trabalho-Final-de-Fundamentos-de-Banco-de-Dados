import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="patrimonios",
        user="postgres",
        password="3,14eoPi",
        host="localhost",
        port=5432
    )