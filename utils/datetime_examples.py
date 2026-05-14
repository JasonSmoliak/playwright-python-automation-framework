from datetime import datetime


def get_current_timestamp():

    return datetime.now()


def format_timestamp():

    now = datetime.now()

    return now.strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def generate_report_name():

    now = datetime.now()

    return now.strftime(
        "report_%Y%m%d_%H%M%S.html"
    )
