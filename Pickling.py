import quandl
import pandas as pd 
import pickle

# Not necesary
api_key = open('api_key.txt','r').read()


def state_list():
	states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
	return states[0][0][1:]
	
def grab_initial_state_data():	
	state_data = state_list()
	main_df = pd.DataFrame()

	for abbv in states_data:
		query = "Name/Postal "+str(abbv)
		df = quandl.get(query, authtoken=api_key)

		if main_df.empty:
			main_df= df 
		else:
			main_df = main_df.join(df)

	print(main_df.head())

	pickle_out = open('states.pickle','wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()

grab_initial_state_data()

#pickle_in = opne('states.pickle','rb')

