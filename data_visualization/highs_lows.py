import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = 'data_visualization\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs =[], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi=128)
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=11)
plt.xlabel('Date', fontsize=9)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=9)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

#    for index, column_header in enumerate(header_row):        
#       print(index, column_header)