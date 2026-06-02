import logging
import azure.functions as func
import os
from sqlalchemy import create_engine, text

bp = func.Blueprint()

@bp.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def poc_sqlalchemy(myTimer: func.TimerRequest) -> None:

    sql_server = os.getenv('SQL_SERVER_SOURCE')
    sql_database = os.getenv('SQL_DATABASE_SOURCE')
    sql_user = os.getenv('SQL_USER_SOURCE')
    sql_pass = os.getenv('SQL_PASSWORD_SOURCE')


    logging.info(f"""servidor: {sql_server}, banco: {sql_database}, usuario: {sql_user}, senha: {sql_pass}""")

    engine = create_engine(f'postgresql+psycopg2://{sql_user}:{sql_pass}@{sql_server}/{sql_database}')

   
    try:
        with engine.connect() as conn:
            # Cria um cursor para executar a consulta   
            cursor = conn.connection.cursor()

            query = "select top 5 * from erp.pedido_item"

            # Executa a consulta SQL
            cursor.execute(query)

            # Busca todos os resultados da consulta
            rows = cursor.fetchone()

            logging.info(rows)           

    except Exception as e:
        logging.error(f"Erro ao ler erp.pedido: {str(e)}")
        raise
