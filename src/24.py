import numpy as np

layer_outputs = [
    [4.8, 1.21, 2.385],
    [8.9, -1.81, 0.2],
    [1.41, 1.051, 0.026],
]

print(np.sum(layer_outputs)) # 18.172

print(np.sum(layer_outputs, axis=None)) # 18.172

print(np.sum(layer_outputs, axis=0)) # [15.11   0.451  2.611]

print(np.sum(layer_outputs, axis=1)) # [8.395 7.29  2.487]

print(np.sum(layer_outputs, axis=1, keepdims=True))
"""
[[8.395]
 [7.29 ]
 [2.487]]
"""
