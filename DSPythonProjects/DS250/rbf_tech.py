#%%
import pandas as pd
import numpy as np
 
#%%
raw = pd.read_csv('https://github.com/BYUIDSS/DSS_W22_HFB_Technology/raw/master/raw_data/activity_log%20(1).csv')

# %%
'''
1. Filter New Ticket Created to square brackets
2. Filter columns w/ new ticket created
3.
'''

splitted_raw = raw.description.str.split( "[", expand = True).rename(columns = {0: 'Keywords', 1: 'Info'})

rare = pd.concat([raw.drop(columns = 'description'), splitted_raw], axis = 1)

rare['Keywords'] = rare.Keywords.str.strip()

# %%
