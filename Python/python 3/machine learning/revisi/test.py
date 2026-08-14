import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Dataset
df = pd.DataFrame({
    'Luas_Tanah': [100, 150, np.nan, 200, 120, 300, 180, 90, 250, 110],
    'Jml_Kamar': [2, 3, 3, 4, 2, 5, 3, 2, 4, np.nan],
    'Kondisi': ['Baru', 'Lama', 'Baru', 'Baru', 'Lama', 'Baru', 'Lama', 'Lama', 'Baru', 'Lama'],
    'Harga_Juta': [500, 750, 800, 1000, 600, 2500, 850, 450, 2000, 550]
})

# 2. Split Data
X = df.drop('Harga_Juta', axis=1)
y = df['Harga_Juta']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Preprocessing Pipeline
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer([
    ('num', num_pipe, ['Luas_Tanah', 'Jml_Kamar']),
    ('cat', cat_pipe, ['Kondisi'])
])

# 4. Transformed Target Regressor (Pipeline Lengkap)
model = TransformedTargetRegressor(
    regressor=Pipeline([
        ('prep', preprocessor),
        ('algo', LinearRegression())
    ]),
    transformer=StandardScaler()
)

# 5. Training & Evaluasi
model.fit(X_train, y_train)
prediksi = model.predict(X_test)

print("Aktual:", y_test.values)
print("Prediksi:", np.round(prediksi, 2))
print("MAE: Rp", np.round(mean_absolute_error(y_test, prediksi), 2), "Juta")
print("R2 Score:", np.round(r2_score(y_test, prediksi), 2))