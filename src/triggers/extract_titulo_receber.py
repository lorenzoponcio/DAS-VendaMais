import logging
import azure.functions as func

bp = func.Blueprint()

@bp.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def extract_titulo_receber(myTimer: func.TimerRequest) -> None:

    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Tabela titulo_receber')