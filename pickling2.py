import quandl
import pandas as pd
import pickle 

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

		if main_df.empty:
			main_df = df 
		else:
			main_df = main_df.join(df)
	
	print(main_df.head()) 

	# Printing out Pickle
	pickle_out = open('fiddy_states.pickle','wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()


# Printing out 
#grab_initial_state_data()

pickle_in = open('fiddy_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data) 

HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2)