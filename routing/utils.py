from datetime import date


def date_to_mysql_string(d: date) -> str:
    return f"'{str(d).replace('-', '/')}'"
