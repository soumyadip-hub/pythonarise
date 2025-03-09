# def hello_func():
#     return 'hello soumya'
# print(hello_func().upper())

# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# courses = ['math','art']
# info = {'name':'john','age':22}
#
# # student_info('math','art',name='john',age=22)
# student_info(*courses,**info)
#

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


def is_leap(year):
    """return for leap year and ,false return for  no n-leap year"""
    return year % 4 == 0 and (year % 100!= 0 or year % 400 == 0)


def days_in_month(year, month):
    """:return number of days in that month in that year"""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2020,2))

















