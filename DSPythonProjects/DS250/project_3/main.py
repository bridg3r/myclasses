#%%
import pandas as pd
import numpy as np
import sys
import altair as alt
import datadotworld as dw

# Question 1: The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

#%%
# BYU-Idaho ID + Name; just gives info, doesn't need to be used
results = dw.query('byuidss/cse-250-baseball-database', 
    "SELECT schoolid, name_full FROM schools WHERE city = 'Rexburg'")

idbyuid = results.dataframe
idbyuid

#%%
# players FROM BYU-Idaho
results4 = dw.query('byuidss/cse-250-baseball-database', 
    "SELECT DISTINCT playerid, schoolid FROM CollegePlaying WHERE schoolid = 'idbyuid'")

college_playing = results4.dataframe
college_playing 

#%%
# Player salary info
results3 = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT playerid, yearid, teamid, salary FROM salaries')

salaries5 = results3.dataframe
salaries5

# %%
# Join BYU-I school ID
q = '''
SELECT DISTINCT s.playerid, 
    s.yearid, 
    s.teamid,
    s.salary,
    cp.schoolid
FROM salaries as s
    JOIN CollegePlaying as cp ON s.playerid = cp.playerid
WHERE schoolid = 'idbyuid'
ORDER BY salary DESC
'''

question1 = dw.query('byuidss/cse-250-baseball-database', q).dataframe

print(question1
    .head(15)
    .filter(["playerid", "yearid",
"salary", "schoolid"])
    .to_markdown(index=False))

# %%
# Question 2: This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)
# question 2a: Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.

q2a = '''
SELECT playerid,
yearid,
h / ab as batting_avg
FROM batting
WHERE ab >= 1
ORDER BY h / ab DESC
LIMIT 5;
'''

question2a = dw.query('byuidss/cse-250-baseball-database', q2a).dataframe

print(question2a
    .head(5)
    .filter(["playerid", "yearid", "batting_avg"])
    .to_markdown(index=False))

#%%
# Question 2b: Use the same query as above, but only include players with more than 10 “at bats” that year. Print the top 5 results.
q2b = '''
SELECT playerid,
yearid,
h/ab as Batting_Average
FROM Batting
WHERE ab >= 10
ORDER BY h/ab DESC
LIMIT 5
'''

question2b = dw.query('byuidss/cse-250-baseball-database', q2b).dataframe

print(question2b
    .head(5)
    .filter(["playerid", "yearid", "Batting_Average"])
    .to_markdown(index=False))

#%%
# Question 2c: Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.

q2c = '''
SELECT playerid,
SUM (h) / SUM (ab) as Batting_Average
FROM Batting 
GROUP BY playerid
HAVING ab > 100
ORDER BY Batting_Average DESC
LIMIT 5
'''

question2c = dw.query('byuidss/cse-250-baseball-database', q2c).dataframe



print(question2c
    .head(5)
    .filter(["playerid", "Batting_Average"])
    .to_markdown(index=False))

# %%
q2d = '''
SELECT playerid,
SUM (h) / SUM (ab) as batting_avg
FROM batting
WHERE playerid = 'hazlebo01'
LIMIT 5
'''

question2d = dw.query('byuidss/cse-250-baseball-database', q2d).dataframe

question2d
# %%
# Question 3 Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to visualize the comparison. Provide the visualization and its description.

#find the most popular team based on all time attendance
q3 = '''
SELECT franchid, 
SUM (attendance) as all_time_attendance
FROM Teams
GROUP BY franchid
HAVING all_time_attendance > 0
ORDER BY SUM (attendance) DESC
LIMIT 100
'''

question3 = dw.query('byuidss/cse-250-baseball-database', q3).dataframe

question3
#%%
#find the all time total payed salary of the two most popular teams (Yankees and Dodgers)
q3b = '''
SELECT teamid, 
SUM (salary) as all_dollars_payed
FROM Salaries
GROUP BY teamid
ORDER BY SUM (salary) DESC
LIMIT 100
'''

question3b = dw.query('byuidss/cse-250-baseball-database', q3b).dataframe

question3b
# %%
q3c = '''
SELECT teamid, 
franchid, name
FROM Teams
where franchid = 'MIL'
LIMIT 100
'''

question3c = dw.query('byuidss/cse-250-baseball-database', q3c).dataframe

question3c
# %%
#find salary payed to player per fan attended since year 2000

q3d = '''
SELECT teams.franchid,
    TeamsFranchises.franchname,
    SUM (teams.w) as wins,
    SUM (Salaries.salary) as all_dollars_payed,
    SUM (teams.attendance) as all_time_attendance,
    SUM (Salaries.salary) / SUM (teams.attendance) as cost_of_attendance,
    SUM (teams.attendance) / (SUM (teams.w) * 10000) as loyalty 
FROM teams
    JOIN Salaries ON Salaries.teamid = teams.teamid
    JOIN TeamsFranchises ON teams.franchid = TeamsFranchises.franchid
WHERE Teams.yearid > 1999
GROUP BY Teams.franchid
ORDER BY cost_of_attendance DESC
'''

question3d = dw.query('byuidss/cse-250-baseball-database', q3d).dataframe

question3d2 = question3d.query("franchid == 'TBD' or franchid == 'SFG'")

question3d

#%%
chart6 = alt.Chart(question3d).mark_circle(size=60).encode(
    alt.X(
"loyalty",
scale = alt.Scale(domain = (1.6, 4.0)),
        axis=alt.Axis(title="Loyalty")
    ),
    y=alt.Y('cost_of_attendance',
    scale = alt.Scale(domain = (.6, 1.3)),
     axis=alt.Axis(title="Cost for Attendance")
),
).properties(
    title='Best Baseball Markets'
)

chart6
#%%
chart5 = alt.Chart(question3d2).mark_circle(size=60).encode(
    alt.X(
"loyalty",
scale = alt.Scale(domain = (1.6, 4.0)),
        axis=alt.Axis(title="Loyalty")
    ),
    y=alt.Y('cost_of_attendance',
    scale = alt.Scale(domain = (.6, 1.3)),
     axis=alt.Axis(title="Cost for Attendance")
),
color=alt.Color('franchname', scale=alt.
                    Scale(scheme='dark2'))
).properties(
    title='Best Baseball Markets'
)

chart5
# %%
chart7 = chart6 + chart5
chart7

chart7.save('Best_Baseball_markets.png')

# %%
