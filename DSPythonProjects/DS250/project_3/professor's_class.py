#%%
import pandas as pd
import numpy as np
import sys
import datadotworld as dw
#%%

results = dw.query('byuidss/cse-250-baseball-database', 
    'SELECT * FROM batting LIMIT 2')



batting5 = results.dataframe


batting5
#%%

q = '''
SELECT b.teamid, 
    t.name, 
    b.yearid,
    p.namegiven, 
    b.ab, 
    b.r, 
    b.ab/b.r as runs_atbat
FROM batting as b
    JOIN people as p ON p.playerid = b.playerid
    JOIN teams as t ON t.teamid = b.teamid
        AND t.yearid = b.yearid
ORDER BY r DESC
LIMIT 100
'''

batting_calc = dw.query('byuidss/cse-250-baseball-database', q).dataframe

batting_calc
# %%
# order by career runs
q = '''
SELECT 
    p.namegiven, SUM(b.ab) as atbat, SUM(b.r) as runs, 
    SUM(b.ab)/SUM(b.r) as runs_atbat
FROM batting as b
    JOIN people as p ON p.playerid = b.playerid
    JOIN teams as t ON t.teamid = b.teamid
        AND t.yearid = b.yearid
-- WHERE b.ab  > 1000 -- bad deal nah
GROUP BY b.playerid, p.namegiven
HAVING atbat < 1000
ORDER BY atbat DESC
LIMIT 100
'''

batting_calc = dw.query('byuidss/cse-250-baseball-database', q).dataframe

batting_calc
# %%
