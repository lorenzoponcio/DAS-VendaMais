import logging
import azure.functions as func
import os

bp = func.Blueprint()

@bp.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def extract_titulo_receber(myTimer: func.TimerRequest) -> None:

    sql_server = os.getenv('SQL_SERVER_SOURCE')
    sql_database = os.getenv('SQL_DATABASE_SOURCE')
    sql_user = os.getenv('SQL_USER_SOURCE')
    sql_pass = os.getenv('SQL_PASSWORD_SOURCE')

    # if myTimer.past_due:
    #     logging.info('The timer is past due!')

    logging.info(f"""servidor: {sql_server}, banco: {sql_database}, usuario: {sql_user}""".format(sql_server=sql_server, sql_database=sql_database, sql_user=sql_user))