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
def extract_estoque_saldo(myTimer: func.TimerRequest) -> None:

    # Origem
    sql_server = os.getenv("SQL_SERVER_SOURCE")
    sql_database = os.getenv("SQL_DATABASE_SOURCE")
    sql_user = os.getenv("SQL_USER_SOURCE")
    sql_pass = os.getenv("SQL_PASSWORD_SOURCE")

    # Destino
    sql_server_dest = os.getenv("SQL_SERVER_DEST")
    sql_database_dest = os.getenv("SQL_DATABASE_DEST")
    sql_user_dest = os.getenv("SQL_USER_DEST")
    sql_pass_dest = os.getenv("SQL_PASSWORD_DEST")

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
        # Buscar dados da origem
        with pyodbc.connect(conn_str_source) as conn_source:
            cursor_source = conn_source.cursor()

            query_source = """
                SELECT *
                FROM erp.estoque_saldo
            """

            cursor_source.execute(query_source)
            rows = cursor_source.fetchall()

            if not rows:
                logging.info("Nenhum registro encontrado na origem.")
                return

        # Inserir no destino
        with pyodbc.connect(conn_str_dest) as conn_dest:
            cursor_dest = conn_dest.cursor()

            inserted_count = 0

            for row in rows:

                # Chave primária da origem
                id_origem = row.id_estoque_saldo

                # Verifica se o registro já existe no destino
                cursor_dest.execute(
                    """
                    SELECT COUNT(1)
                    FROM dbo.estoque_saldo
                    WHERE cd_registro_origem = ?
                    """,
                    str(id_origem)
                )

                exists = cursor_dest.fetchone()[0]

                if exists:
                    logging.info(
                        f"Registro já existe no destino. cd_registro_origem={id_origem}"
                    )
                    continue

                insert_sql = """
                    INSERT INTO dbo.estoque_saldo (
                        id_produto,
                        dt_referencia,
                        qt_saldo,
                        dt_inclusao,
                        dt_atualizacao,
                        nm_sistema_origem,
                        cd_registro_origem
                    )
                    VALUES (
                        ?, ?, ?, ?, ?, ?, ?
                    )
                """

                values = (
                    row.id_produto,
                    row.dt_referencia,
                    row.qt_saldo,
                    row.dt_inclusao,
                    row.dt_atualizacao,
                    row.nm_sistema_origem,
                    str(id_origem)
                )

                cursor_dest.execute(insert_sql, values)
                inserted_count += 1

            conn_dest.commit()

            logging.info(
                f"{inserted_count} novos registros inseridos no destino."
            )

    except Exception as e:
        logging.error(f"Erro ao migrar estoque_saldo: {str(e)}")
        raise