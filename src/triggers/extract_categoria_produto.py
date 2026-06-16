import logging
import azure.functions as func
import os
import pyodbc

bp = func.Blueprint()

@bp.timer_trigger(
    schedule="0 * * * * *",
    arg_name="myTimer",
    run_on_startup=False,
    use_monitor=False
)
def extract_categoria_produto(myTimer: func.TimerRequest) -> None:

    # Origem
    sql_server = os.getenv('SQL_SERVER_SOURCE')
    sql_database = os.getenv('SQL_DATABASE_SOURCE')
    sql_user = os.getenv('SQL_USER_SOURCE')
    sql_pass = os.getenv('SQL_PASSWORD_SOURCE')

    # Destino
    sql_server_dest = os.getenv('SQL_SERVER_DEST')
    sql_database_dest = os.getenv('SQL_DATABASE_DEST')
    sql_user_dest = os.getenv('SQL_USER_DEST')
    sql_pass_dest = os.getenv('SQL_PASSWORD_DEST')

    conn_str_source = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pass};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    conn_str_dest = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={sql_server_dest};"
        f"DATABASE={sql_database_dest};"
        f"UID={sql_user_dest};"
        f"PWD={sql_pass_dest};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    try:
        with pyodbc.connect(conn_str_source) as conn_source:
            cursor_source = conn_source.cursor()

            query_source = """
                SELECT TOP 5 *
                FROM erp.categoria_produto
            """

            cursor_source.execute(query_source)
            rows = cursor_source.fetchall()

            if not rows:
                logging.info("Nenhum registro encontrado na origem.")
                return

            columns = [column[0] for column in cursor_source.description]

        with pyodbc.connect(conn_str_dest) as conn_dest:
            cursor_dest = conn_dest.cursor()

            columns_sql = ", ".join(columns)
            placeholders = ", ".join(["?"] * len(columns))

            insert_sql = f"""
                INSERT INTO dbo.categoria_produto ({columns_sql})
                VALUES ({placeholders})
            """

            data = [tuple(row) for row in rows]

            cursor_dest.executemany(insert_sql, data)
            conn_dest.commit()

            logging.info(f"{len(data)} registros inseridos no destino com sucesso.")

    except Exception as e:
        logging.error(f"Erro ao migrar erp.categoria_produto: {str(e)}")
        raise