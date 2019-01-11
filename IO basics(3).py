import pandas as pd 



df = pd.read_csv('YALE-RBCI.csv')
print(df.head())

'''
df.set_index('Date', inplace= True)

#Create a new csv file
df.to_csv('newcsv2.csv')


# reading back csv
df = pd.read_csv("newcsv2.csv", index_col=0)
print(df.head())
'''


# renaming columns
df.columns = [2,'Austing_HPI','White','Blah']
print(df.head()) 

# saving to a csv file
df.to_csv('newcsv3.csv')

# removing the header of the csv
df.to_csv('newcsv4.csv', header=False)

# reading a csv with no header
df = pd.read_csv('newcsv4.csv', names=['Date', 'Cost Index', 'U.S. Population(Millions)', 'Long Rate'], )
print(df.head())

# converting to html format/table
df.to_json('example.json') 

