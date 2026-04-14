# pyright: reportMissingModuleSource=false
import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy training data
X = np.array([[90], [95], [100], [105], [110]])
y = np.array([95, 100, 105, 110, 115])

model = LinearRegression()
model.fit(X, y)

# Save model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained & saved!")