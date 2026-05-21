import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load dataset (build path relative to this file)
dataset_path = Path(__file__).resolve().parent.parent / 'src' / 'multi_linear_regression' / 'sample1' / 'Dataset.csv'
if not dataset_path.exists() or dataset_path.stat().st_size == 0:
	raise FileNotFoundError(f"Dataset tidak ditemukan atau kosong: {dataset_path}")
dataset = pd.read_csv(dataset_path)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# 2. Encoding categorical data ('State')
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# 3. Split data menjadi training dan test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 4. Melatih model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# 5. Prediksi untuk data berikut:
# "R&D Spend = 160000, Administration = 130000, Marketing Spend = 300000, State = California"
# One-hot encoding California di posisi 1
# Urutan: [California, Florida, New York, RnD, Admin, Marketing]
input_data = [[1, 0, 0, 160000, 130000, 300000]]
hasil_prediksi = regressor.predict(input_data)
print("Prediksi profit:", hasil_prediksi[0])