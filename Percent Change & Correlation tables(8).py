import quandl 
import pandas as pd
import pickle 
import matplotlib.pyplot as plt 

api_key = open('api_key.txt').read()


def state_list():
	fitty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fitty_states[0][1][1:]


def grab_initial_state_data():
	states= state_list()
	main_df = pd.DataFrame()
		
	for abbri in fitty_states[0][1][1:]:
		query = ('YALE-RBCI' +str(abbri))
		df = quandl.get(query,authtoken=api_key)
		#df.rename(columns={'NSA Value':str(abbv) + ' NSA Value' , 'SA Value' : str(abbv) + ' SA Value'}, inplace=True)

		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)
	print(main_df.head())
	

pickle_out = open('fitty_states.pickle','wb')
pickle.dump(main_df, pickle_out)
pickle_out.close()

HPI_data = pd.read_pickle('pickle.pickle')
HPI_data.plot()
plt.leyend().remove()
plt.show()