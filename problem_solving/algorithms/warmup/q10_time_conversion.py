import datetime

def timeConversion(s):
    t = datetime.datetime.strptime(s, "%I:%M:%S%p")
    return t.strftime("%H:%M:%S")
