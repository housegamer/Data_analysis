import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style 
style.use('ggplot')
import numpy as np 


web_stats = {'Day':[1,2,3,4,5,6],
			'Visitors':[45,65,35,86,34,66],
			'Bounce_Rate':[55,67,34,77,34,23]}

df = pd.DataFrame(web_stats)

# Setting an Index as Day
df.set_index('Day', inplace=True)
print(df.head())

# To reference a specific column
print(df['Visitors'])
# OR
print(df.Visitors)

# Reference a specific column
print(df[['Bounce_Rate','Visitors']])

# Converting to a list
print(df.Visitors.tolist())

# Converting to an array, have to import numpy FIRST
print(np.array(df[['Bounce_Rate','Visitors']]))