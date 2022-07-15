#%%

import altair as alt
import numpy as np
import pandas as pd

#%%

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] * 4
days.sort()

df=pd.DataFrame({
    'hour': ["9am", "10am", "11am", "12pm"] * 5,
    'dayofweek': days,
    'cnt': [5, 18, 2, 3, 19, 1, 9, 0, 7, 10,
        12, 3, 1, 17, 6, 7, 10, 11, 3, 4]}) 

chart = alt.Chart(df, height=210).mark_rect().encode(
    alt.Y(
        "hour",
        sort=["9am", "10am", "11am", "12pm"],
        title="Hour"), 
    alt.X(
        "dayofweek",
        sort=["Mon", "Tue", "Wed", "Fri", "Thurs"],
        title="Day of Week"),
        color=alt.Color(
            "cnt", 
            scale=alt.Scale(
                range=['lightyellow','red']), 
        legend=alt.Legend(title='Count')
    ),
    tooltip=[
        alt.Tooltip("cnt:Q", title="Count")
    ]
).properties(width=250)

chart
# %%
