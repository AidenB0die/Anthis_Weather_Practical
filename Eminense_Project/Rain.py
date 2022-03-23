import plotly.express as px
import csv
from datetime import datetime

Alphabet = []

filename = 'data/Eminence_Data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # gets date, high, and low temps
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[1], '%Y-%m-%d')
        try:
            high = float(row[10])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rains.append(high)

for i in rains:
    Alphabet.append(rains[0:5])
    del rains[0:5]
    
print(Alphabet)
fig = px.imshow(Alphabet,
                labels=dict(x="How much Rain per Day", y="Year", color="How Much Rain"),
                x=['July 21', 'July 22', 'July 23', 'July 24', 'July 25'],
                y=['2012', '2013', "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
               )
fig.update_xaxes(side="top")
fig.show()
