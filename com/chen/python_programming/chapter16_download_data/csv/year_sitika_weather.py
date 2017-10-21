import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename = 'file/sitka_weather_2014.csv'
filename = 'file/death_valley_2014.csv'


def getData():
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

        for index, column_header in enumerate(header_row):
            print(index, column_header)

        highs, dates, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    data = []
    data.append(dates)
    data.append(highs)
    data.append(lows)
    return data


fig = plt.figure(dpi=128, figsize=(10, 6))
data = getData()
plt.plot(data[0], data[1], c='red', Alpha=0.5)
plt.plot(data[0], data[2], c='blue', Alpha=0.5)

# 填充两条线之间的区域
plt.fill_between(data[0], data[1], data[2], facecolor='blue', alpha=0.1)

plt.title('daily high and low temperatures, 2014'.title(), fontsize=24)
plt.xlabel('', fontsize=8)

# 绘制倾斜的日期标签
fig.autofmt_xdate()

plt.ylabel('Temperature(F)', fontsize=8)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.show()
