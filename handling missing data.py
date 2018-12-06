import matplotlib.pyplot as plt 
import pickle
import pandas as pd

#grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data = pd.read_pickle('fiddy_states.pickle')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how='mean')

print(HPI_data[['TX','TX1yr']].head())

HPI_data[['TX','TX1yr']].plot(ax=ax1)

plt.lengend(loc=4)
plt.show()

