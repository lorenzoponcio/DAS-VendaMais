import logging
import azure.functions as func
import os
import time

from sqlalchemy import create_engine, text

bp = func.Blueprint()

@bp.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def poc_sqlalchemy(myTimer: func.TimerRequest) -> None:

    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    try:
        logging.info("Iniciando POC SQLAlchemy")

        inicio_total = time.perf_counter()

        logging.info("Criando engine...")

        engine = create_engine(
            f"mssql+pymssql://{sql_user}:{sql_pass}@{sql_server}:1433/{sql_database}"
        )

        logging.info("Abrindo conexão...")

        with engine.connect() as conn:

            logging.info("Executando consulta...")

            inicio_query = time.perf_counter()

            result = conn.execute(
                text("SELECT TOP 5 * FROM erp.pedido_item")
            )

            rows = result.fetchall()

            fim_query = time.perf_counter()

            logging.info(f"Linhas retornadas: {len(rows)}")

            for row in rows:
                logging.info(row)

            logging.info(
                f"Tempo da query SQLAlchemy: {fim_query - inicio_query:.4f} segundos"
            )

        fim_total = time.perf_counter()

        logging.info(
            f"Tempo total SQLAlchemy: {fim_total - inicio_total:.4f} segundos"
        )

    except Exception as e:
        logging.exception(f"Erro na POC SQLAlchemy: {e}")
        raise