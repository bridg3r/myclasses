# %%
# import packages
import pandas as pd
import numpy as np
import altair as alt

import urllib3
import json

# %%
# the long way to help us understand json files and 
# end product: imported "flights" data set
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)

#%%
#analyze the data
# 17 columns, 924 rows
#num_of_delays_late_aircraft have -999 for missing and minutes_delayed_nas
# airport_code                     1
# num_of_delays_weather            1
# minutes_delayed_weather          1
# minutes_delayed_security         1
# minutes_delayed_nas              1
# minutes_delayed_late_aircraft    1
# minutes_delayed_carrier          1
# num_of_delays_total              1
# num_of_delays_security           1
# airport_name                     1
# num_of_delays_nas                1
# num_of_delays_late_aircraft      1
# num_of_delays_carrier            1
# num_of_flights_total             1
# year                             1
# month                            1
# minutes_delayed_total            1
flights.columns.value_counts()
flights.shape
flights.describe()

#%%

#Question 1
#Extract below
# Airport code
# num_of_delays_total
# num_of_flights_total
# minutes_delayed_total

#%%
# 27 missing months
# no missing in num_of_delays_total
# no missing num_of_flights_total
# no missing minutes_delayed_total

#%%
flights_2 = flights.groupby(['airport_code']).sum().reset_index()

flights_2 = flights_2.assign(
    avg_minute_delay = lambda x: x.minutes_delayed_total / x.num_of_flights_total,
    avg_hour_delay = lambda x: x.avg_minute_delay / 60, 
    proportion = lambda x: x.num_of_delays_total / x.num_of_flights_total
)

print(flights_2
    .head(7)
    .filter(["airport_code", "num_of_delays_total", "num_of_flights_total", "proportion","avg_hour_delay"])
    .to_markdown(index=False))


#%%
#Question 2
# ffill fill na function
flights5 = flights
flights5['month'] = flights['month'].replace('n/a', np.NaN).fillna(method='ffill')

#%%

flights5 = flights.groupby(['month']).sum().reset_index()

flights5 = flights5.assign(
    proportion = lambda x: x.num_of_delays_total / x.num_of_flights_total
)


chart5 = alt.Chart(flights5).mark_bar().encode(
    alt.X(
        "month",
        sort=["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",],
        axis=alt.Axis(title="Month")
    ),
    y=alt.Y('proportion', axis=alt.Axis(title="Proportion (Total Delays / Total Flights)"))
).properties(
    title='Flight Delays by Month'

)

chart5

chart5.save('flight_delays_by_month.png')


#%%

# Question 3
flights6 = flights
flights6['month'] = flights['month'].replace('n/a', np.NaN).fillna(method='ffill')

flights6 = flights6.assign(
    severe = lambda x: x.num_of_delays_weather,
    fixed_late_aircraft = lambda x: x.num_of_delays_late_aircraft.replace(-999, np.NaN),
    fixed_late_aircraft1 = lambda x: x.fixed_late_aircraft.fillna(x.fixed_late_aircraft.mean()),
    fixed_late_aircraft2 = lambda x: x.fixed_late_aircraft1 * .3,
    true_nas = lambda x: np.where(
        x.month.isin(['April', 'May', 'June', 'July', 'August']), 
        x.num_of_delays_nas * 0.4,
        x.num_of_delays_nas * 0.65
        ),
    true_weather = lambda x: x.fixed_late_aircraft2 + x.severe + x.true_nas,
    true_percent_weather = lambda x: x.true_weather / x.num_of_flights_total
)

flights6 = flights6.groupby(['airport_code']).sum().reset_index()

print(flights6
    .head(7)
    .filter(["airport_code",
    "num_of_delays_weather",
    "true_weather",
    "true_percent_weather"])
    .to_markdown(index=False))
 
#%%
#Question 4
chart6 = alt.Chart(flights6).mark_bar().encode(
    alt.X(
        "airport_code",
        axis=alt.Axis(title="Airport Code")
    ),
    y=alt.Y('true_percent_weather', axis=alt.Axis(title="True Weather Delays Proportion"))
).properties(
    title='True Weather Delays by Airport')

chart6

chart6.save('True_Weather_Delay_Totals_by_Airport.png')

# %%
# Question 5

clean = flights.assign(
    month = flights.month.replace('n/a', np.NaN), 
    num_of_delays_late_aircraft = flights.num_of_delays_late_aircraft.replace(-999, np.NaN),
    num_of_delays_carrier = flights.num_of_delays_carrier.replace("1500+", "1750").astype('int64')
    #year is already missing
)


clean.to_json('flights_clean.json')
# %%
