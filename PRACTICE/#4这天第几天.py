# method 1
def isleapyear(year):
    if (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0
                                               and year % 400 == 0):
        return True


date = int(input('Enter the date(yyyymmdd): '))
year = int(date / 10000)
month = int((date - year * 10000) / 100)
day = date - year * 10000 - month * 100
days = 0
DofM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
if isleapyear(year):
    DofM[2] = 29

for m in range(month):
    days += DofM[m]
days += day
print(days)
