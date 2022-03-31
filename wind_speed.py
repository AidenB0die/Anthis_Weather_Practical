import plotly.graph_objects as go
import csv
from datetime import datetime
t = []
l = []
filename = 'data/Eminence_Data.csv'
with open(filename, newline='') as f:
    reader = csv.DictReader(f)

    for row in reader:
        tt = float(row['windspeed'])
        ll = float(row['winddir'])
        t.append(tt)
        l.append(ll)
        fig = go.Figure()


    fig.add_trace(go.Barpolar(
        r=t[:5],
        theta=l[:5],
        name='2012',
        marker_color='rgb(3, 61, 252)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[5:10],
    theta=l[5:10],
    name='2013',
    marker_color='rgb(3, 252, 161)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[10:15],
    theta=l[10:15],
    name='2014',
    marker_color='rgb(252, 3, 65)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[15:20],
    theta=l[15:20],
    name='2015',
    marker_color='rgb(173, 252, 3)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[20:25],
    theta=l[20:25],
    name='2016',
    marker_color='rgb(252, 128, 3)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[25:30],
    theta=l[25:30],
    name='2017',
    marker_color='rgb(206, 3, 252)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[30:35],
    theta=l[30:35],
    name='2018',
    marker_color='rgb(98, 3, 252)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[35:40],
    theta=l[35:40],
    name='2019',
    marker_color='rgb(240, 101, 142)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[40:45],
    theta=l[40:45],
    name='2020',
    marker_color='rgb(176, 151, 159)'
    ))
    fig.add_trace(go.Barpolar(
    r=t[45:50],
    theta=l[45:50],
    name='2021',
    marker_color='rgb(164, 181, 235)',
    ))

fig.update_traces(
    width=3,

    )

fig.update_layout(
    title='Wind Speed and Direction, Eminence Indiana           r=Wind Speed         Theta = Wind Direction',
    font_size=16,
    legend_font_size=16,
    polar_angularaxis_rotation=90,
    template='plotly_dark'



)
fig.show()
