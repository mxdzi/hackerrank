def dayOfProgrammer(year):
    if year == 1919:
        return f"26.09.{year}"
    elif year < 1918:
        return f"13.09.{year}" if year % 4 != 0 else f"12.09.{year}"
    else:
        return f"12.09.{year}" if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)) else f"13.09.{year}"
