import pandas as pd


df = pd.read_csv('AUSBS-M.csv')
print(df.head())

df.set_index('series_id', inplace= True)
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())

# To get rid of the header
df.to_csv('newcsv3.csv', header = False)


# To change the names of the header
df=pd.read_csv('newcsv3.csv', names= ['asdf','asdfasdf','feeeee','eieowow'])
print(df.head())

# Turn your data to Html format
df.to_html('example.html')

# Renaming column
df.rename(columns={'name':'buttstuff'}, inplace= True)
print(df.header())