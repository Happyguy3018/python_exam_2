from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go
data=dict()
for user_id in list (dataset.keys()):
    for bank, money in ( dataset[user_id]).items():
        if user_id in data:
            data[user_id] += sum(money)
        else:
            data[user_id] = sum(money)


#Вивести кругову діаграму: якого товару на яку суму продано.

diagram =go.Pie(labels=list(data.keys()), values=list(data.values()))

plotly.offline.plot([diagram], filename="task5.html")