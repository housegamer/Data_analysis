import pandas as pd 
import matplotlib.pyplot as plt 



web_stats = {'day':[1,2,3,4,6],
			'visitors':[55,65,56,12,32],
			'bouce_rates':[55,64,74,15,77]	}

df = pd.DataFrame(web_stats)

print(df)