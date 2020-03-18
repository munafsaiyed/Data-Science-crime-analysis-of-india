import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
data=pd.read_csv('project_file.csv')
print(data.tail())
data['Open-Close'] = (data.Open - data.Close)/data.Open
data['High-Low'] = (data.High - data.Low)/data.Low
data['percent_change'] = data['Adj Close'].pct_change()
data['std_5'] = data['percent_change'].rolling(5).std()
data['ret_5'] = data['percent_change'].rolling(5).mean()
data.dropna(inplace=True)
X = data[['Open-Close', 'High-Low', 'std_5', 'ret_5']]

# Y is the target or output variable
y = np.where(data['Adj Close'].shift(-1) > data['Adj Close'], 1, -1)
 Total dataset length
dataset_length = data.shape[0]

# Training dataset length
split = int(dataset_length * 0.75)
print(split)
X_train, X_test = X_test[:split], X_test[split:]
y_train, y_test = y_test[:split], y_test[split:]

# Print the size of the train and test dataset
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)
clf = RandomForestClassifier(random_state=5)
model = clf.fit(X_train, y_train)
from sklearn.metrics import accuracy_score
print('Correct Prediction (%): ', accuracy_score(y_test, model.predict(X_test), normalize=True)*100.0)
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
report = classification_report(y_test, model.predict(X_test))
print(report)
data['strategy_returns'] = data.percent_change.shift(-1) * model.predict(X)

import matplotlib.pyplot as plt
plt.show()
(data.strategy_returns[split:]+1).plot()
plt.ylabel('user_ratib(%)')
plt.show()
