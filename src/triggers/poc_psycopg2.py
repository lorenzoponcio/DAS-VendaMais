import logging
import azure.functions as func
import os
import psycopg2
import time

bp = func.Blueprint()

@bp.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def poc_psycopg2(myTimer: func.TimerRequest) -> None:

    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    logging.info("Iniciando POC psycopg2")
    logging.info(f"servidor: {sql_server}, banco: {sql_database}, usuario: {sql_user}")

    try:
        inicio_total = time.perf_counter()

        logging.info("Abrindo conexão...")

        conn = psycopg2.connect(
            database=sql_database,
            user=sql_user,
            password=sql_pass,
            host=sql_server,
            port=5432,
            connect_timeout=10
        )

        logging.info("Conexão aberta com sucesso")

        with conn:
            with conn.cursor() as cursor:
                query = "SELECT * FROM erp.pedido_item LIMIT 5"

                logging.info("Executando query...")
                inicio_query = time.perf_counter()

                cursor.execute(query)

                logging.info("Query executada, buscando resultados...")

                rows = cursor.fetchall()

                fim_query = time.perf_counter()

                logging.info(f"Quantidade de linhas retornadas: {len(rows)}")
                logging.info(f"Tempo da query: {fim_query - inicio_query:.4f} segundos")

                for row in rows:
                    logging.info(row)

        conn.close()

        fim_total = time.perf_counter()
        logging.info(f"Tempo total: {fim_total - inicio_total:.4f} segundos")

    except Exception as e:
        logging.exception(f"Erro na POC psycopg2: {e}")
        raise