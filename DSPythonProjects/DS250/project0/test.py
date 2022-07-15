
# Talk to Brother Hathaway and tell him that I think it is the RAM/Storage/outdated computer
# or talk to Brother Mclaughlain and tell him Ben Fuqua sent you
#%%
import pandas as pd   
import altair as alt  
from altair_saver import save as s

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
chart.save('test.png')
#%%
s(chart, 'test.png')

# %%


print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))
# %%
