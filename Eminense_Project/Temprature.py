import plotly.graph_objects as go

from datetime import datetime
import csv

filename = "Data/Eminence_Data.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    temp = []
    date = []

    for row in reader:
        temps = float(row[4])
        d = str(row[1])
        date.append(d)
        temp.append(temps)

print(temp)
print(date)
feels_like = [74.9, 80.3, 87.7, 89.6, 88.8, 75.2, 75, 78.2, 66.8, 67.9, 73.7, 77.9, 72.4, 67, 65.9, 75.4, 71.2, 73.4,
              74.6, 77.6, 85.8, 83.7, 85.7, 89.1, 83.5, 86.4, 85.7, 77, 75.8, 72.5, 71.1, 72.1, 70.5, 75.2, 77.2, 85.5,
              72.2, 69.8, 69.7, 70.9, 85.5, 72.2, 69.8, 69.7, 70.9, 80, 76.7, 79, 76.6, 77.5, 74.8, 75.1, 78, 80.5,
              81.9, ]

feels_like_max = [86.4, 93.4, 103.1, 97.1, 106.4, 86.2, 85, 91.6, 75, 77.6, 84.6, 89.5, 75.3, 75.3, 73.7, 83.9, 81.2,
                  81.9, 84.2, 89.4, 99.2, 94.8, 100.5, 102.3, 94.5, 98.3, 97.2, 91, 83.7, 81.4, 76, 79.7, 77.3, 87.2,
                  87.7, 101.2, 75.5, 80.1, 78.8, 80.8, 101.2, 75.5, 80.1, 78.8, 80.8, 93.1, 90.5, 87.3, 85.6, 89.3,
                  84.6, 84.1, 89.6, 94.1, 95.6]
# then temperature
temperature = [75.4, 80.3, 85.6, 86.3, 86.2, 74.6, 74.5, 76.5, 66.8, 67.9, 73.5, 76.9, 72.4, 67.0, 65.9, 75.1, 71.3,
               73.4, 74.4, 76.2, 81.2, 81.5, 81.4, 83.4, 80.8, 82.3, 82.0, 76.1, 75.3, 72.5, 71.1, 72.1, 70.5, 74.5,
               76.6, 81.3, 72.2, 69.8, 69.7, 70.9, 81.3, 72.2, 69.8, 69.7, 70.9, 78.2, 75.4, 78.2, 76.0, 76.7, 74.2,
               74.6, 76.6, 78.0, 79.1]

temp_max = [88.7, 93.5, 99.2, 95.2, 100.9, 83.1, 81.5, 86.1, 75, 77.6, 84.3, 87, 75.3, 75.3, 73.7, 83.3, 81.9, 82.2,
            84.2, 85.3, 89, 88.4, 90.5, 91.6, 87.8, 90.7, 90.1, 84.6, 82.1, 81.3, 76, 79.7, 77.3, 84.5, 85.6, 91.4,
            75.5, 80.1, 78.8, 81, 91.4, 75.5, 80.1, 78.8, 81, 87.5, 84.8, 85, 84.3, 87.8, 82.4, 82, 85.5, 86.8, 87.2]

temp_min = [59.5, 66.3, 73.3, 80.6, 73.5, 65.6, 69.4, 69, 56.8, 55.6, 60.5, 66.1, 65, 57.8, 55.1, 68.4, 58.3, 63.6,
            63.2, 65.1, 72.7, 77.4, 72.4, 76.1, 72.3, 75.2, 75.7, 72, 68, 62.8, 67.6, 67.9, 62.9, 64.1, 67.2, 73.4,
            65.9, 58.7, 59.4, 59.3, 73.4, 65.9, 58.7, 59.4, 59.3, 70.2, 69.4, 73.1, 65.9, 64.7, 65.9, 68.2, 67, 69.2,
            71.9]

feels_like_min = [59.5, 66.3, 73.3, 84.2, 73.5, 65.6, 69.4, 69, 56.8, 55.6, 60.5, 66.1, 65, 57.8, 55.1, 68.4, 58.3,
                  63.6, 63.2, 65.1, 72.7, 77.4, 72.4, 76.1, 72.3, 75.2, 75.7, 72, 68, 62.8, 67.6, 67.9, 62.9, 64.1,
                  67.2, 73.4, 65.9, 58.7, 59.4, 59.3, 73.4, 65.9, 58.7, 59.4, 59.3, 70.2, 69.4, 73.1, 65.9, 64.7, 65.9,
                  68.2, 67, 69.2, 71.9]
# - starts the dates in five day increments
# 2012
dates = [datetime(year=2012, month=7, day=21),
         datetime(year=2012, month=7, day=22),
         datetime(year=2012, month=7, day=23),
         datetime(year=2012, month=7, day=24),
         datetime(year=2012, month=7, day=25),
         # 2013
         datetime(year=2013, month=7, day=21),
         datetime(year=2013, month=7, day=22),
         datetime(year=2013, month=7, day=23),
         datetime(year=2013, month=7, day=24),
         datetime(year=2013, month=7, day=25),
         # 2014
         datetime(year=2014, month=7, day=21),
         datetime(year=2014, month=7, day=22),
         datetime(year=2014, month=7, day=23),
         datetime(year=2014, month=7, day=24),
         datetime(year=2014, month=7, day=25),
         # 2015
         datetime(year=2015, month=7, day=21),
         datetime(year=2015, month=7, day=22),
         datetime(year=2015, month=7, day=23),
         datetime(year=2015, month=7, day=24),
         datetime(year=2015, month=7, day=25),
         # 2016
         datetime(year=2016, month=7, day=21),
         datetime(year=2016, month=7, day=22),
         datetime(year=2016, month=7, day=23),
         datetime(year=2016, month=7, day=24),
         datetime(year=2016, month=7, day=25),
         # 2017
         datetime(year=2017, month=7, day=21),
         datetime(year=2017, month=7, day=22),
         datetime(year=2017, month=7, day=23),
         datetime(year=2017, month=7, day=24),
         datetime(year=2017, month=7, day=25),
         # 2018
         datetime(year=2018, month=7, day=21),
         datetime(year=2018, month=7, day=22),
         datetime(year=2018, month=7, day=23),
         datetime(year=2018, month=7, day=24),
         datetime(year=2018, month=7, day=25),
         # 2019
         datetime(year=2019, month=7, day=21),
         datetime(year=2019, month=7, day=22),
         datetime(year=2019, month=7, day=23),
         datetime(year=2019, month=7, day=24),
         datetime(year=2019, month=7, day=25),
         # 2020
         datetime(year=2020, month=7, day=21),
         datetime(year=2020, month=7, day=22),
         datetime(year=2020, month=7, day=23),
         datetime(year=2020, month=7, day=24),
         datetime(year=2020, month=7, day=25),
         # 2021
         datetime(year=2021, month=7, day=21),
         datetime(year=2021, month=7, day=22),
         datetime(year=2021, month=7, day=23),
         datetime(year=2021, month=7, day=24),
         datetime(year=2021, month=7, day=25),
         ]

fig = go.Figure(data=[go.Ohlc(x=dates, tickwidth=0.5,
                              open=feels_like_max, high=temp_max,
                              low=temp_min, close=feels_like_min)])

fig.show()
