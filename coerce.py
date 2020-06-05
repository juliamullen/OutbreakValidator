from dateutil import parser as dateparser


def corece_list(datum):
    if isinstance(datum, (list, tuple)):
        return datum
    else:
        return [datum]

def coerce_date(date):
    try:
        dateparser.parse(date)
        return date.strftime("%Y-%m-%d")
    except (ValueError, OverflowError) as e:
        print(f"Could not parse {date}")
        return date

def coerce_type():
    pass
