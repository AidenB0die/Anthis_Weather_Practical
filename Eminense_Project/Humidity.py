import plotly.graph_objects as go
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
            high = float(row[9])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rains.append(high)


for i in rains:
    Alphabet.append(rains[0:5])
    del rains[0:5]

headerColor = '#00AADD'
rowEvenColor = '#BD5E00'
rowOddColor = '#EB7500'


fig = go.Figure(data=[go.Table(
    header=dict(values=['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
                line_color='black',
                fill_color='darkorange',
                align='left'),
    cells=dict(values=[['July 21', 'July 22', 'July 23', 'July 24' , 'July 25'], # 1st column
                       Alphabet[0],
                       Alphabet[1],
                       Alphabet[2],
                       Alphabet[3],
                       Alphabet[4],
                       Alphabet[5],
                       Alphabet[6],
                       Alphabet[7],
                       Alphabet[8],
                       Alphabet[9]], # 2nd column
               line_color='black',
               fill_color='orange',
               align='left'))
])

fig.show()