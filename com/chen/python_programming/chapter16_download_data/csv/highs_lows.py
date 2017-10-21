import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'file/sitka_weather_07-2014.csv'

def getData():
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)

        for index, column_header in enumerate(header_row):
            print(index,column_header)

        highs ,dates= [],[]
        for row in reader:
            current_date =datetime.strptime(row[0],"%Y-%m-%d")
            dates.append(current_date)
            high = int(row[1])
            highs.append(high)
        data = []
        data.append(dates)
        data.append(highs)

        return data

fig = plt.figure(dpi=128,figsize=(10,6))
data = getData()
plt.plot(data[0],data[1],c = 'red')

plt.title('daily high temperatures, July 2014'.title(),fontsize = 24)
plt.xlabel('',fontsize = 8)

# 绘制倾斜的日期标签
fig.autofmt_xdate()

plt.ylabel('Temperature(F)',fontsize = 8)
plt.tick_params(axis='both',which = 'major',labelsize = 8)

plt.show()

