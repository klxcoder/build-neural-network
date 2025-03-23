import numpy as np

layer_outputs = [
    [4.8, 1.21, 2.385],
    [8.9, -1.81, 0.2],
    [1.41, 1.051, 0.026],
]
max_values = np.max(layer_outputs, axis=1, keepdims=True)
layer_outputs -= max_values

exp_values = np.exp(layer_outputs)

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

print(norm_values)
"""
[[8.95282664e-01 2.47083068e-02 8.00090293e-02]
 [9.99811129e-01 2.23163963e-05 1.66554348e-04]
 [5.13097164e-01 3.58333899e-01 1.28568936e-01]]
"""