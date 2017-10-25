import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])

bias = -0.1

output = sigmoid(np.dot(weights, inputs) + bias)

print('Output:')
print(output)
