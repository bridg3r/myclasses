#%%
import pandas as pd
import altair as alt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

dat = pd.read_csv('https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.csv')

# Try recreating this chart using the mtcars missing. 
# Note that hp has missing values, and you will have to replace them with the mean. 
# Please drop all cars with a missing name

dat = dat.dropna(subset=['car'])
dat['hp'] = dat.hp.replace(np.NaN, dat.hp.dropna().mean())

chart1 = alt.Chart(dat).encode(
        alt.X( # edit the x-axis
            'hp', # select column for x-axis
            axis=alt.Axis(
                format='+.1f', # 4 digits no comma
                title="Horse Power"), # change column title
        ), 
        alt.Y(
            'mpg',
            axis=alt.Axis(title='Miles per Gallon')
    ),
    ).properties(
    title='This is dope.' # change chart title
    ).mark_circle()

markline = pd.DataFrame({'hp': [80, 160], 'annotations':['Big','Real Big'], 'pos': [25, 20]})

chart2 = alt.Chart(markline).mark_rule().encode(
    alt.X('hp')
)

annotation = alt.Chart(markline).mark_text(
    align='right',
    fontSize = 10,
    dx = -3
).encode(
    x='hp',
    y='pos',
    text='annotations'
)


chart3 = chart1 + chart2 + annotation
chart3 = chart3.configure_title(anchor='start').configure_mark(color='red')
chart3

# Try writing code to recreate the following table.
# Have cyl on the rows and carb on the columns
# Each value shows the counts of each.

new = dat.groupby(['cyl', 'carb']).size().unstack(fill_value=0)

new.columns
new  = new.rename(columns={'carb': 'cyl'})

# %%
