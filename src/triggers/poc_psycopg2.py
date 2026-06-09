import logging
import azure.functions as func
import os
import psycopg2

bp = func.Blueprint()

@bp.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def poc_psycopg2(myTimer: func.TimerRequest) -> None:

    sql_server = os.getenv('SQL_SERVER_SOURCE')
    sql_database = os.getenv('SQL_DATABASE_SOURCE')
    sql_user = os.getenv('SQL_USER_SOURCE')
    sql_pass = os.getenv('SQL_PASSWORD_SOURCE')

    logging.info(f"servidor: {sql_server}, banco: {sql_database}, usuario: {sql_user}")

    try:
        with psycopg2.connect(
            database=sql_database,
            user=sql_user,
            password=sql_pass,
            host=sql_server,
            port=5432
        ) as conn:

            with conn.cursor() as cursor:
                query = "SELECT * FROM erp.pedido_item LIMIT 5"

                cursor.execute(query)

                rows = cursor.fetchall()

                for row in rows:
                    logging.info(row)

    except Exception as e:
        logging.error(f"Erro ao ler erp.pedido_item: {str(e)}")
        raise