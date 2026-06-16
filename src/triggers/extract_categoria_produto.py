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
        # =========================
        # 1. Buscar dados na origem
        # =========================
        with pyodbc.connect(conn_str_source) as conn_source:
            cursor_source = conn_source.cursor()

            query_source = """
                SELECT TOP 5 *
                FROM erp.categoria_produto
                ORDER BY id
            """

            cursor_source.execute(query_source)
            rows = cursor_source.fetchall()

            if not rows:
                logging.info("Nenhum registro encontrado na origem.")
                return

            all_columns = [column[0] for column in cursor_source.description]

        # Não inserir a coluna identity do destino
        identity_columns = ["id_categoria"]

        columns_insert = [
            column
            for column in all_columns
            if column.lower() not in identity_columns
        ]

        # =========================
        # 2. Inserir no destino
        # =========================
        with pyodbc.connect(conn_str_dest) as conn_dest:
            cursor_dest = conn_dest.cursor()

            inserted_count = 0

            for row in rows:
                source_id = getattr(row, "id_categoria")

                cursor_dest.execute(
                    """
                    SELECT COUNT(1)
                    FROM dbo.categoria_produto
                    WHERE id_origem = ?
                    """,
                    source_id
                )

                exists = cursor_dest.fetchone()[0]

                if exists:
                    logging.info(
                        f"Categoria já existe no destino. id_origem={source_id}"
                    )
                    continue

                columns_sql = ", ".join(["id_origem"] + columns_insert)
                placeholders = ", ".join(["?"] * (len(columns_insert) + 1))

                insert_sql = f"""
                    INSERT INTO dbo.categoria_produto ({columns_sql})
                    VALUES ({placeholders})
                """

                values = [source_id] + [
                    getattr(row, column)
                    for column in columns_insert
                ]

                cursor_dest.execute(insert_sql, values)
                inserted_count += 1

            conn_dest.commit()

            logging.info(
                f"{inserted_count} novos registros inseridos no destino."
            )

    except Exception as e:
        logging.error(f"Erro ao migrar categoria_produto: {str(e)}")
        raise