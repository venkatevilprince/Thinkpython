import datetime
#s= raw_input("enter the DOB (example : 19-03-1994)")
s = "19-03-1994"


def get_dates(s):
    """gets the dates from the entered string
       Note : exceptions are not handled"""
    date_ = int(s[:2])
    month_ = int(s[3:5])
    year_ = int(s[6:10])
    return (year_, month_, date_,)
dob = get_dates(s)
today_date = datetime.date.today()
#now = "{:%d.%m.%Y}".format(today_date)
#today = get_dates(now)
my_dob = datetime.date(dob[0],dob[1],dob[2])
#print my_dob,today_date
x = today_date - my_dob


def form_age(days_lived):
    """Craetes and returns datetime.date variable with
       age in years, months and days"""
    age_year, age_month = divmod(days_lived, 365)
    age_month, age_day = divmod(age_month, 30)
    return datetime.date(age_year, age_month, age_day)
age = form_age(x.days)
print "you are {} years {} month and {} days old".format(age.year, age.month, age.day)
bday = datetime.date(today_date.year, dob[1], dob[2])
if (bday < today_date):
    bday = bday.replace(year = bday.year + 1)
print "Next Bday :",bday
print "Days unitil next Bday :", (bday - today_date).days, "days"


