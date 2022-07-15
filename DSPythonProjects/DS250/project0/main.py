#%%
import pandas as pd   
import altair as alt   

#%%
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

chart = (alt.Chart(mpg)
  .encode(
    x='displ', 
    y='hwy')
  .mark_circle()
)

chart
#%%
chart.save("chart.png")
#%%





alt.Chart(mpg).mark_point()


# %%
