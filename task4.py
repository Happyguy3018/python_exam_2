from data import dataset
from task1 import *
import re
import plotly
import plotly.graph_objs as go
data=dict()
for user_id in list (dataset.keys()):
    for bank, money in ( dataset[user_id]).items():
        if user_id in data:
            data[user_id] += sum(money)
        else:
            data[user_id] = sum(money)
#Вивести стовпчикову діаграму: хто скільки грошей витратив.
dataset
diagram = go.Bar(x=list(data.keys()),y=list(data.values()))

fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='task4.html')