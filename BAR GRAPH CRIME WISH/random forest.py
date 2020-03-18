import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
import datetime
features = pd.read_csv('project_file.csv')
features.head(5)
print('The shape of our features is:', features.shape)
features.describe()
features = pd.get_dummies(features)
features.iloc[:,5:].head(5)
labels = np.array(features['murder'])
features= features.drop('murder', axis = 1)
feature_list = list(features.columns)
print(feature_list)
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)
baseline_preds = test_features[:, feature_list.index('year')]
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(train_features, train_labels);
predictions = rf.predict(test_features)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
mape = 100 * (errors / test_labels)
ccuracy = 100 - np.mean(mape)
tree = rf.estimators_[5]
print('Accuracy:', round(accuracy, 2), '%.')
#New random forest with only the two most important variables
rf_most_important = RandomForestRegressor(n_estimators= 1000, random_state=42)
months = features[:, feature_list.index('month')]
days = features[:, feature_list.index('day')]
years = features[:, feature_list.index('year')]

