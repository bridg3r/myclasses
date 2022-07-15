#%%
import pandas as pd
import altair as alt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
#%%

dat = pd.read_csv('https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.csv')


# %%
dat['hp'] = dat['hp'].replace(np.NaN, dat.hp.dropna().mean())
# %%
chart1 = alt.Chart(dat).mark_circle().encode(
    alt.X( 'hp', axis=alt.Axis(title="Miles per Gallon")
    ),
    y=alt.Y('mpg', axis=alt.Axis(title="Horse Power"))
).properties(title='This is dope.')

markline = pd.DataFrame({'hp': [80, 160]})

chart2 = alt.Chart(markline).mark_rule().encode(
    alt.X('hp')
)

chart3 = chart1 + chart2
chart3 = chart3.configure_title(anchor='start')
# %%

q2 = dat.filter(['cyl', 'carb'])

q2.pivot_table( 
    columns = 'cyl', 
    values = 'carb').reset_index()