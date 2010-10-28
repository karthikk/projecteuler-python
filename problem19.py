#!/usr/bin/python

def problem19():

    def is_leap_year(year):
        return (year%4 == 0 and year%100!=0) or (year%400 == 0)

    sunday, monday, tuesday, wednesday, thursday, friday, saturday = range(7)
    firsts = [0] * 7
    year = 1901
    normal_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    leap_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    first_of_month = tuesday
    while year <= 2000:
        days_in_months = normal_days
        if is_leap_year(year):
            days_in_months = leap_days
        for i, num_days in enumerate(days_in_months):
            firsts[first_of_month] += 1
            if (year == 2000):
                print first_of_month
            first_of_month += num_days
            first_of_month %= 7
        year += 1

    print firsts

if __name__ == "__main__":
    problem19()
