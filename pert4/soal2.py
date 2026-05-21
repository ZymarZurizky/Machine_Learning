import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
dataset = pd.read_csv('/Users/macbook/Applications/Machine_learning/src/multi_linear_regression/sample1/Dataset.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Encoding
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Regressor
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Soal 2: Print koefisien dan persamaan regresi
print("Koefisien regresi:", regressor.coef_)
print("Intercept:", regressor.intercept_)