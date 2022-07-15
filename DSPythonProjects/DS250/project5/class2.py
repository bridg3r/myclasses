#%%
import pandas as pd
import altair as alt
import numpy as np

url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'
#%%

#%%
dat_cols = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 1).melt()

dat = pd.read_csv(url, skiprows =2, header = None, encoding = "ISO-8859-1" )
# %%
# %%
# Which of the following Star Wars films have you seen? Please select all that apply.' as 'seen'
# Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.' as 'rank'
# Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.' as 'view'
# Do you consider yourself to be a fan of the Star Trek franchise?' as 'star_trek_fan'
# Do you consider yourself to be a fan of the Expanded Universe\\?\x8cæ' as 'expanded_fan'
# Are you familiar with the Expanded Universe?' as 'know_expanded'
# Have you seen any of the 6 films in the Star Wars franchise?' as 'seen_any'
# Do you consider yourself to be a fan of the Star Wars film franchise?' as 'star_wars_fans'
# Which character shot first?' as 'shot_first'
# see the code snippet for the other four replaclements.  
# the four examples.  Should fix the other questions.

# this is not complete.
variables_replace = {
    'Which of the following Star Wars films have you seen\\? Please select all that apply\\.':'seen',
    'Do you consider yourself to be a fan of the Expanded Universe\\?\x8cæ':'expanded_fan',
    'Unnamed: \d{1,2}':np.nan,
    ' ':'_',
}
# one example.  My code has three.
# 'Response' is replaced with '' 
# ' ' is replaced with '_'
values_replace = {
    'Star Wars: Episode ':'',
}

dat_cols_use = (dat_cols
    .assign(
        value_replace = lambda x:  x.value.str.strip().replace(values_replace, regex=True),
        variable_replace = lambda x: x.variable.str.strip().replace(variables_replace, regex=True)
    )
    .fillna(method = 'ffill')
    .fillna(value = "")
    .assign(column_names = lambda x: x.variable_replace.str.cat(x.value_replace, sep = "__").str.strip('__').str.lower())
    )
dat_cols_use

dat.columns = dat_cols_use.column_names.to_list()
# %%
