import datetime


def transfer_date(raw_date: str) -> datetime.date:
    """
    Example:
    "14-12-2021" => datetime(day=14, month=12, year=2021)
    :param raw_date: str
    :return: datetime.date
    """
    date_obj = datetime.datetime.strptime(raw_date, '%d-%m-%Y').date()
    return date_obj