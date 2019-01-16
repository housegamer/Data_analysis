import quandl 
import pandas as pd


api_key = open('api_key.txt').read()
'''df = quandl.get('YALE/RBCI', authtoken=api_key)
print(df.head())'''

fitty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# This gives you a list of the page
#print(fitty_states)

# This gives you a DataFrame of the list
#print(fitty_states[0])

# This is a column
#print(fitty_states[0][0])

for abbri in fitty_states[0][1][1]:
	print('YALE-RBCI' +str(abbri))