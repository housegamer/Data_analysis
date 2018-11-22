import quandl
import pandas as pd 
import pickle
import matplotlib.pyplot as plt 

# Not necesary
api_key = open('api_key.txt','r').read()

def state_list():
	state = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
	return state[0][0][1:]
	
def grab_initial_state_data():	
	state_data = state_list()
	main_df = pd.DataFrame()

	for abbv in state_data:
		query = "Name/Postal "+str(abbv)
		df = quandl.get(query, authtoken=api_key)

		if main_df.empty:
			main_df= df 
		else:
			main_df = main_df.join(df)

	print(main_df.head())

	pickle_out = open('state.pickle','wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()
HPI_data = pd.read_pickle('state.pickle')

HPI_data.plot()
plt.legend().remove()
plt.show()



#grab_initial_state_data()
#pickle_in = opne('states.pickle','rb')

