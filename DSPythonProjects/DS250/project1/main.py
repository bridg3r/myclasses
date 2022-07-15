#%%
import pandas as pd   
import altair as alt   


#%%
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
us_names = pd.read_csv(url)

#%%
us_names.name.value_counts().reset_index()

number_of_johns = (us_names
    .query("name == 'John' and Total > 0")
    .assign(mystates = lambda x: x.UT + x.OR + x.ID)
    )

number_of_johns

#%%
base = (alt.Chart(number_of_johns, title = 'History of the name John in the US')
    .encode(
      x = alt.X(
        'year', axis=alt.Axis(format='.4'), title = 'Birth year name'
        ),
      y = alt.Y(
        'Total', 
        scale = alt.Scale(domain= [0, 65000]),
        title = 'Count of name',
        )
    )
    .mark_line()
)

bmark = alt.Chart(my_data)
    .encode(
      x = 'year'
      y = "Total",
      text
      )
#%%

us_names.groupby(['name']).sum()

#Which name has been given teh most and the least?
(us_names
    .filter(['name', 'Total'])
    .groupby(['name'])
    .sum()
    .reset_index()
    .sort_values(['Total'])

)

# %%
oliver_names = us_names.query("name == 'Oliver'")


chart = (alt.Chart(oliver_names)
  .encode(
    x='name', 
    y='')
  .mark_circle()
)

chart

# %%
