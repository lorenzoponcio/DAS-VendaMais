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
def extract_entrega(myTimer: func.TimerRequest) -> None:

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
                FROM erp.entrega
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
                id_origem = row.id_entrega

                # Verifica se o registro já existe no destino
                cursor_dest.execute(
                    """
                    SELECT COUNT(1)
                    FROM dbo.entrega
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
                    INSERT INTO dbo.entrega (
                        id_pedido,
                        id_transportadora,
                        id_regiao,
                        dt_prometida,
                        dt_entrega,
                        ds_status_entrega,
                        cd_rastreio,
                        ds_observacao,
                        dt_inclusao,
                        dt_atualizacao,
                        nm_sistema_origem,
                        cd_registro_origem
                    )
                    VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )
                """

                values = (
                    row.id_pedido,
                    row.id_transportadora,
                    row.id_regiao,
                    row.dt_prometida,
                    row.dt_entrega,
                    row.ds_status_entrega,
                    row.cd_rastreio,
                    row.ds_observacao,
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
        logging.error(f"Erro ao migrar entrega: {str(e)}")
        raise