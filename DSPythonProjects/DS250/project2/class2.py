#%%
import pandas as pd
import numpy as np
import altair as alt
import urllib3
import json

#%%
# Cars
url_cars = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"
cars = pd.read_json(url_cars)

# the long way to help us understand json files and 
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)

df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman', np.nan],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip',np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT, pd.NaT],
                    "power": [np.nan, np.nan, np.nan, np.nan]})

#%
df.dropna(how="all", axis = 1)

#%
df.dropna(how="all", axis = 1).dropna(how="all")

# %%
# drop rows with NA for a specified column
df.dropna(subset = ['born'], axis = 0)

#%%
flights.dropna(subset = ['month'])

#%%
flights.month.replace('n/a', np.NaN)

#%%
flights.columns

#%%
flights.airport_code.value_counts() # feels good
flights.airport_name.value_counts()
# %%
pd.crosstab(flights.month, flights.year)
# %%
pd.crosstab(flights.month, flights.airport_code)
# %%
flights.year.describe()
flights.year.isna().sum()
flights.year.value_counts()
flights.shape
# %%
flights.num_of_delays_late_aircraft.describe()

#%%

flights.num_of_delays_late_aircraft.replace(-999, np.)

datc = flights.assign()
    num_of_delays_late_aircraft