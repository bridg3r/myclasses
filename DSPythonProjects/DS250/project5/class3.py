# %%
import pandas as pd 
import altair as alt
import numpy as np

# %%
url = 'https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv'

dat_cols = pd.read_csv(url, encoding = "ISO-8859-1", nrows = 1).melt()

dat = pd.read_csv(url, skiprows=2, header = None, encoding = "ISO-8859-1" )
# %%
# we want to use this with the .replace() command that accepts a dictionary.
variables_replace = {
    'Which of the following Star Wars films have you seen\\? Please select all that apply\\.':'seen',
    'Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.':'rank',
    'Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.':'view',
    'Do you consider yourself to be a fan of the Star Trek franchise\\?':'star_trek_fan',
    'Do you consider yourself to be a fan of the Expanded Universe\\?\x8cæ':'expanded_fan',
    'Are you familiar with the Expanded Universe\\?':'know_expanded',
    'Have you seen any of the 6 films in the Star Wars franchise\\?':'seen_any',
    'Do you consider yourself to be a fan of the Star Wars film franchise\\?':'star_wars_fans',
    'Which character shot first\\?':'shot_first',
    'Unnamed: \d{1,2}':np.nan,
    ' ':'_',
}

values_replace = {
    'Response':'',
    'Star Wars: Episode ':'',
    ' ':'_'
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

# separate '-'
# remove non numeric stuff
# pick one value
# convert to int
# %%
dat = dat.dropna(subset=['household_income', 'age', 'star_wars_fans'])
#%%
incomr_col = dat.household_income\
    .str\
        .split(" - ", expand = True)\
        .rename({0:"salary_min", 1:"salary_max"}, axis = 1)\
        .salary_min\
        .str.replace(",|\$|\+| ","")\
        .astype("int")

#%%
age_col = dat.age\
    .str\
        .split("-", expand = True)\
        .rename({0:"age_min", 1:"age_max"}, axis = 1)\
        .age_min\
        .str.replace("> ","")\
        .astype("int")
# %%
#map text to year in school number string
#convert to int
# what is series vs data frame?

#%%
grade_mapping = {
    "Less than high school degree": 9,
    "High school degree":12,
    "Some college or Associate degree": 210,
    "Bachelor degree": 16,
    "Graduate degree": 18
}

dat.education.replace(grade_mapping)
# %%
pd.get_dummies(dat.star_wars_fans, drop_first=True)

pd.get_dummies(dat.shot_first).drop("I don't understand this question", axis=1 )
# %%
pd.get_dummies(dat.filter(['star_wars_fans', 'expanded_fan']))
# %%
pd.get_dummies(dat\
    .filter(['star_wars_fans', 'expanded_fan']), drop_first=True, dummy_na=True)
# %%
pd.get_dummies(dat, drop_first=True, dummy_na=True)