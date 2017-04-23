import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.arange(6).reshape(3, 2)

poly = PolynomialFeatures(degree=2)
poly.fit_transform(X)
