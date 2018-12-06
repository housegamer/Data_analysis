import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt 


api_key = open('api_key.txt','r').read()

def state_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fiddy_states[0][1][1:]

def grab_initial_state_data():
	states = state_list()
	main_df = pd.DataFrame()

	for abbv in fiddy_states[0][1][1:]:
		query = "FMAC/HPI_48660"+str(abbv)
		print(query)
		df = quandl.get(query, authtoken=api_key)
		df[abbv] = (df[abbv] - df[abbv]) / df[abbv][0] * 100

		if main_df.empty:
			main_df = df 
		else:
			main_df = main_df.join(df)
	
	print(main_df.head()) 

	# Printing out PickleB
	pickle_out = open('fiddy_states.pickle','wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()

def HPI_Benchmark():
	df = quandl.get("FMAC/HPI_48660", authtoken=api_key)
	df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0]*100.0
	return df 

fig = plt.figure()
ax1 = plt.subplot2grid((1,1)(0,0))

HPI_data - pd.read_pickle('fiddy_states')

TX1yr = HPI_data['TX'].resample('A', how = 'mean')

HPI_data['TX'].plot(ax = ax1)
TX1yr.plot(ax=ax1)

plt.legend().remove()
plt.show()

