import numpy as np

np.random.seed(10)

n = 50
x = np.random.randn(n)
y = x * np.random.randn(n)

mu = 0
sigma = 1
samples = 10
s = np.random.normal(mu, sigma, samples)

groups_of_data = [np.random.normal(mu, sigma, samples) for mu in [1.0, 4.0, 3.0, 2.0]]


