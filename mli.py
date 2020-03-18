import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
dataset = pd.read_csv('C:/Users/Dell/Documents/kamli/AppleStoreproject.csv')
dataset.shape
(17,5836)
dataset.head()
dataset.describe()
dataset.plot(x='user_rating', y='price', style='o')  
plt.title('price based user rating')  
plt.xlabel('user_rating')  
plt.ylabel('price')  
plt.show()  
dataset.head()
dataset.describe()  
X = dataset[['price', 'user_rating', 'rating_count_tot']]
y = dataset['user_rating']
from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  
from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
print(coeff_df)  
y_pred = regressor.predict(X_test)  
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(df)  
from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))  
