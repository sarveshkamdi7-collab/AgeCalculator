from datetime import date, datetime

user_name = input('Enter name of user: ')
today = date.today()


def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def month_days(month, year):
    if month == 2:
        return 29 if leap_year(year) else 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    raise ValueError(f'Invalid month {month}. Use 1-12.')


def day_of_year(d):
    total = d.day
    for m in range(1, d.month):
        total += month_days(m, d.year)
    return total


def calculate_total_days(birth, current):
    fixed = 0
    year = birth.year
    while year < current.year:
        fixed += 366 if leap_year(year) else 365
        year += 1
    fixed += day_of_year(current) - day_of_year(birth)
    return fixed


def calculate_age(birth, current):
    years = current.year - birth.year
    months = current.month - birth.month
    days = current.day - birth.day

    if days < 0:
        months -= 1
        prev_month = current.month - 1 or 12
        prev_year = current.year if current.month != 1 else current.year - 1
        days += month_days(prev_month, prev_year)
    if months < 0:
        years -= 1
        months += 12
    return years, months, days


birth = datetime.strptime(input('Enter your birthday in format (YYYY-MM-DD): '),
                          '%Y-%m-%d').date()

years, months, days = calculate_age(birth, today)
total_days = calculate_total_days(birth, today)

print('_' * 76)
print()
print(': Name of user is', user_name)
print()
print(': Your age is', years, 'years,', months, 'months,', days, 'days')
print()
print(': Total months passed since your birth:', years * 12 + months)
print()
print(': Total days passed since your birth:', total_days)
print('_' * 76)
