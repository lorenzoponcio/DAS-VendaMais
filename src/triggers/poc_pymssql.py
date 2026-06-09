import logging
import azure.functions as func
import os
import pymssql
import time

bp = func.Blueprint()

@bp.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def poc_pymssql(myTimer: func.TimerRequest) -> None:

    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    try:
        logging.info("Iniciando POC pymssql")

        inicio_total = time.perf_counter()

        conn = pymssql.connect(
            server=sql_server,
            user=sql_user,
            password=sql_pass,
            database=sql_database,
            port=1433,
            login_timeout=10,
            timeout=30
        )

        with conn.cursor() as cursor:

            query = "SELECT TOP 5 * FROM erp.pedido_item"

            logging.info("Executando consulta...")

            inicio_query = time.perf_counter()

            cursor.execute(query)
            rows = cursor.fetchall()

            fim_query = time.perf_counter()

            logging.info(f"Linhas retornadas: {len(rows)}")

            for row in rows:
                logging.info(row)

            logging.info(
                f"Tempo da query pymssql: {fim_query - inicio_query:.4f} segundos"
            )

        conn.close()

        fim_total = time.perf_counter()

        logging.info(
            f"Tempo total pymssql: {fim_total - inicio_total:.4f} segundos"
        )

    except Exception as e:
        logging.exception(f"Erro na POC pymssql: {e}")
        raise