#Problem 19: https://projecteuler.net/problem=19

def is_leap_year(year):
    if year % 100 == 0 and year % 400 == 0: return True
    if year % 4 == 0: return True
    return False

def count_sundays():
    months = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30 ,31 , 30, 31]
    count = 0
    day = 0
    for year in range(1900, 2001):
        for month in range(12):
            days = months[month]
            if month == 1 and is_leap_year(year): days = months[month][1]
            elif month == 1: days = months[month][0]
            if day % 7 == 0 and year > 1900: count += 1
            day += days
    return count


if __name__ == '__main__':
    print(f"Solution: {count_sundays()}")