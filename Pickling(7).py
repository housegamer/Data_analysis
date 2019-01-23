import quandl 
import pandas as pd
import pickle 


api_key = open('api_key.txt').read()


def state_list():
	fitty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fitty_states[0][1][1:]


def grab_initial_state_data():
	states= state_list()
	main_df = pd.DataFrame()
		
	for abbri in fitty_states[0][1][1:]:
		query = 'YALE-RBCI'+str(abbri)
		df = quandl.get("YALE/RBCI",authtoken=api_key)
		#df.rename(columns={'NSA Value':str(abbri) + ' NSA Value' , 'SA Value' : str(abbri) + ' SA Value'}, inplace=True)
		
		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.merge(df)
	print(main_df.head())

	pickle_out = open('fitty_states.pickle','wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()

print(grab_initial_state_data())

'''pickle_in = open('fitty_states', 'rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)'''