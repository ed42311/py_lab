import numpy as np
import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
headers = ['Airport ICAO Code','Count','Airport Name','Timezone']
df = pd.read_csv('./airports.csv',names=headers)

df = df.set_index('Airport ICAO Code')
print(df.head())

# SJO = df.loc['SJO']
# sjo_normal = SJO / SJO.max()

# df['Date'] = df['Date'].map(lambda x: datetime.strptime(str(x), '%Y/%m/%d %H:%M:%S.%f'))
# x = df['Count']
# y = df['Airport ICAO Code']

# # plot
# plt.plot(x,y)
# plt.show()