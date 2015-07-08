import datetime
weekday_dict = {
    1:'Monday',   
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday',
}

def get_weekday():
    """Returns the week number of today"""
    today_date = datetime.date.today()
    return today_date.isoweekday()

week_num = get_weekday()
print weekday_dict[week_num]
