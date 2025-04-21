def q3():
    from datetime import date

    date1 = (10, 4, 2024)
    date2 = (10, 4, 2025)

    d1 = date(date1[2], date1[1], date1[0])
    d2 = date(date2[2], date2[1], date2[0])

    days_between = abs((d2 - d1).days)
    print("Number of days between:", days_between)
q3()