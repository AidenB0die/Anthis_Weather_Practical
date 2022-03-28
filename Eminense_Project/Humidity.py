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

headerColor = '#BD0000'
rowEvenColor = '#BD5E00'
rowOddColor = '#EB7500'

fig = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>Dates</b>','<b>July 21</b>','<b>July 22</b>','<b>July 23</b>','<b>July 24</b>', '<b>July 25</b>'],
    line_color='black',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=[
      ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'],
      [Alphabet[0]],
      [],
      [],
      []],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
    align = ['left', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))
])

fig.show()