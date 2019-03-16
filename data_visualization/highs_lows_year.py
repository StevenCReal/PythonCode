import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = "data_visualization\sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        highs.append(int(row[1]))
        lows.append(int(row[3]))

fig = plt.figure(dpi=128)
plt.plot(dates, highs, c='red', alpha=0.8)
plt.plot(dates, lows, c='blue', alpha=0.8)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)

plt.title("Daily high and low temperatures - 2014", fontsize=11)
plt.xlabel("Date", fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()