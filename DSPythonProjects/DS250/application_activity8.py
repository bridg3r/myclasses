#%%
import pandas as pd
import altair as alt
# %%
aa8 = pd.read_excel('/Users/bridg3r/Downloads/201712 Pulse of the Nation.xlsx')

# %%
'''
aa8.AgeRange.value_counts(sort=True)
65+      292
55-64    175
45-54    164
35-44     80
25-34     63
18-24     26
'''
aa8.filter(['AgeRange', 'GovtPorn']).query("AgeRange == '65+'").value_counts(sort=True)

aa8.filter(['AgeRange', 'GovtPorn']).query("AgeRange == '55-64'").value_counts(sort=True)

aa8.filter(['AgeRange', 'GovtPorn']).query("AgeRange == '45-54'").value_counts(sort=True)

aa8.filter(['AgeRange', 'GovtPorn']).query("AgeRange == '35-44'").value_counts(sort=True)

aa8.filter(['AgeRange', 'GovtPorn']).query("AgeRange == '25-34'").value_counts(sort=True)

aa8.filter(['AgeRange', 'GovtPorn']).query("AgeRange == '18-24'").value_counts(sort=True)
# %%
aa8.Race.value_counts(sort=True)
"""
White                 713
Don't Know/Refused     22
Latino                 20
Asian                  19
Other                  15
Black                  11
"""

aa8.filter(['Race', 'BlackLives']).query("Race == 'White'").value_counts(sort=True)

aa8.filter(['Race', 'BlackLives']).query("Race == 'Latino'").value_counts(sort=True)

aa8.filter(['Race', 'BlackLives']).query("Race == 'Asian'").value_counts(sort=True)

aa8.filter(['Race', 'BlackLives']).query("Race == 'Other'").value_counts(sort=True)

aa8.filter(['Race', 'BlackLives']).query("Race == 'Black'").value_counts(sort=True)
# %%

aa8.Education.value_counts(sort=True)
"""
College degree         242
Some college           224
High school or less    164
Graduate degree        160
Other                    8
"""

aa8.filter(['Education', 'EasilyOffended']).query("Education == 'College degree'").value_counts(sort=True)

aa8.filter(['Education', 'EasilyOffended']).query("Education == 'Some college'").value_counts(sort=True)

aa8.filter(['Education', 'EasilyOffended']).query("Education == 'High school or less'").value_counts(sort=True)


aa8.filter(['Education', 'EasilyOffended']).query("Education == 'Other'").value_counts(sort=True)
# %%


aa8.Gender.value_counts(sort=True)
"""
Male                  428
Female                364
Don't Know/Refused      4
Other                   4
"""

aa8.filter(['Gender', 'GunRestrict']).query("Gender == 'Male'").value_counts(sort=True)

aa8.filter(['Gender', 'GunRestrict']).query("Gender == 'Female'").value_counts(sort=True)

aa8.filter(['Gender', 'GunRestrict']).query("Gender == 'Other'").value_counts(sort=True)
#%%