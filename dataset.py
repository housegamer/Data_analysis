import quandl
import pandas as pd 


#api_key = open('','r').read()

#df = quandl.get('ZILLOW/Z63144_ZRIFAH')
#print(df.head())


states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')

# This is a list:
#print(states)

#This is a dataframe:
#print(states[0])

#This is a column:
print(states[0][0])

for abbv in states[0][0][1:]:
	print(" " +str(abbv))