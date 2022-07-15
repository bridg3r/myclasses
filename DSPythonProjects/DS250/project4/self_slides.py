#%%
import sys
!{sys.executable} -m pip install seaborn scikit-learn
#%%
# the full imports
import pandas as pd 
import numpy as np
import seaborn as sns
import altair as alt

#%%
# the from imports
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics

#%%
from sklearn.metrics import accuracy_score

#%%
dwellings_denver = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv")
dwellings_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")
dwellings_neighborhoods_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv")   

#alt.data_transformers.enable('json')

# %%
# Question 1: Create 2-3 charts that evaluate potential relationships between the home variables and before1980.
h_subset = dwellings_ml.filter(['livearea', 'finbsmnt',
    'basement', 'yearbuilt', 'nocars', 'numbdrm', 'numbaths', 
    'stories','netprice', 'yrbuilt', 'before1980']).sample(500)

sns.set(font_scale=2)
correlation = sns.pairplot(h_subset, hue = 'before1980')

correlation.savefig('save_as_a_png.png')

corr = h_subset.drop(columns = 'before1980').corr()
# %%
heatmap = sns.heatmap(corr)
heatmap.savefig('heatmap.png')
# num of baths, stories, living area
#%%
#Question 2: Can you build a classification model (before or after 1980) that has at least 90% accuracy for the state of Colorado to use (explain your model choice and which models you tried)?

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

#add in the neighborhood dataset that provides one more extra feature
ml = dwellings_ml.merge(dwellings_neighborhoods_ml)

# X_pred has all data excpet for our targets of before 1980 and yrbuilt. Parcel is dropped becuase it is the only non-numeric value
# why do we need to include the axis = 1 argument?
X_pred = ml.drop(['before1980', 'yrbuilt', 'parcel'], axis = 1)
# array with target columns 
y_pred = ml.filter(["before1980"], axis = 1)

# each array is split into two arrays with 34% of the array being the test data and 66% being the training data
# rando_state 76 will shuffle both arrays in the same way
X_train, X_test, y_train, y_test = train_test_split(
    X_pred, 
    y_pred, 
    test_size = .34, 
    random_state = 76)   

#%%
# instantiate Decision Tree Classifier object
clf = tree.DecisionTreeClassifier()
# pass the train features along with the train targets to tree object
clf = clf.fit(X_train, y_train)
#pass in the test features and save the preictions as y_pred
y_pred = clf.predict(X_test)
y_probs = clf.predict_proba(X_test)


# %%
#works with 95.7% accuracy
score = accuracy_score(y_test,y_pred)

#%%
#Q3 Will you justify your classification model by detailing the most important features in your model (a chart and a description are a must)?
# %%
df_features = pd.DataFrame(
    {'f_names': X_train.columns, 
    'f_values': clf.feature_importances_}).sort_values('f_values', ascending = False)

# %%
f_chart = alt.Chart(df_features.query("f_values > .012")).encode(alt.X('f_values'), alt.Y('f_names', sort = "-x")).mark_bar()
f_chart.save('f_chart.png')

# %%
# Q4 Can you describe the quality of your classification model using 2-3 evaluation metrics? You need to provide an interpretation of each evaluation metric when you provide the value.

sns.set(font_scale=1)
print(metrics.confusion_matrix(y_test, y_pred))
c_matrix = metrics.plot_confusion_matrix(clf, X_test, y_test)
print(metrics.classification_report(y_test, y_pred))

# %%
metrics.plot_roc_curve(clf, X_test, y_test)

