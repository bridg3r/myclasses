#%%
import pandas as pd   
import altair as alt   

#%%
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
us_names = pd.read_csv(url)

#%%
us_names
us_names.query('year == 1910')
#%%
bridger_names = us_names.query("name == 'Bridger'")

chart1 = (alt.Chart(bridger_names)
    .encode(
        alt.X(
            'year', 
            axis=alt.Axis(format='.4'),
            scale = alt.Scale(domain = (1980, 2015))
        ), 
        alt.Y('Total', scale = alt.Scale(domain = (0, 220))),
    )
    .mark_line()
)

birthday = bridger_names.query("year == 1999")


brithday_chart = (alt.Chart(birthday)
    .encode(
        alt.X(
            'year', 
            axis=alt.Axis(format='.4'),
            scale = alt.Scale(domain = (1980, 2015))
        ), 
        alt.Y('Total', scale = alt.Scale(domain = (0, 220))),
    )
    .mark_rule())

chart1 = chart1 + brithday_chart
chart1
#chart1.save('birthday_chart.png')

# %%
brittany_names = us_names.query("name == 'Brittany'")

chart2 = (alt.Chart(brittany_names)
    .encode(
      alt.X(
        'year', 
        axis=alt.Axis(format='.4'),
        scale = alt.Scale(domain = (1960, 2020))
      ), 
      alt.Y(
          'Total',
          scale = alt.Scale(domain = (0, 40000))
        ),
    )
    .mark_line()
)

chart2
chart2.save('brittany_names.png')

# %%
anakin_names = us_names.query("name == 'Anakin'")

chart3 = (alt.Chart(anakin_names)
    .encode(
      alt.X('year', 
      axis=alt.Axis(format='.4'),
      scale = alt.Scale(domain = (1997, 2015))
    ), 
      alt.Y('Total', scale = alt.Scale(domain = (0, 200))),
     )
    .mark_line()
)

release_dates = anakin_names.query("year == 1999 | year == 2002 | year == 2005")

release_chart = (alt.Chart(release_dates)
    .encode(
      alt.X('year', 
      axis=alt.Axis(format='.4'),
      scale = alt.Scale(domain = (1997, 2015))
    ), 
      alt.Y('Total', scale = alt.Scale(domain = (0, 200))),
     )
    .mark_rule()
)

chart3 = chart3 + release_chart
chart3
#chart3.save('anakin_names.png')


# %%

mary_names = us_names.query("name == 'Mary' | name == 'Peter' | name == 'Martha' | name == 'Paul'")

chart4 = (alt.Chart(mary_names)
    .encode(
      alt.X(
          'year', 
          axis=alt.Axis(format='.4'),
          scale = alt.Scale(domain = (1910, 2015))
        ), 
      alt.Y('Total', scale = alt.Scale(domain = (0, 60000))),
      color = 'name'
     )
    .mark_line()
)

chart4
#chart4.save('christian_names.png')

# %%
