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
        inicio = time.perf_counter()

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

            cursor.execute(query)
            rows = cursor.fetchall()

            logging.info(f"Linhas retornadas: {len(rows)}")

            for row in rows:
                logging.info(row)

        conn.close()

        fim = time.perf_counter()
        logging.info(f"Tempo total pymssql: {fim - inicio:.4f} segundos")

    except Exception as e:
        logging.exception(f"Erro na POC pymssql: {e}")
        raise