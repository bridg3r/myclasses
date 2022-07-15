# %%
import pandas as pd 
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

#remember to always know the encoding for a file
dat = pd.read_csv(url, encoding = 'latin1')
# %%
s = pd.Series(['1. Ant.  ', '2. Bee!\n', '3. Cat?\t', '4. Beat?\t', np.nan])
s.str.strip()
s.str.strip('123.!? \n\t')
s.str.strip('1234.!? \n\t')

# %%
s.str.replace('Ant.', 'Man')
# s.str.replace('a', 8) strings can only replace strings
s.str.replace('a', '8')
s.str.replace('a', '8', case = False)
s.str.replace('a|e', '8', case = False)

s.str.replace('\d', '', case = False)
# %%
s2 = pd.Series(['1-20', '21-50', '51-80', '81-100', np.nan])
s3 = pd.Series(
    [
        "this is a regular sentence",
        "https://docs.python.org/3/tutorial/index.html",
        np.nan
    ]
)

s2.str.split("-", expand = True)\
    .rename({0: 'lower', 1: 'upper'}, axis = 1)

#%
two_columns = s2.str.split("-", expand = True).rename(
   columns = {0: 'minimum', 1: 'maximum'})

two_columns.fillna("").agg("__".join, axis = 1)

two_columns.minimum.str.cat(two_columns.maximum, sep = "__")

# %%
