from typing import List

import numpy as np

inputs: List[List[float]] = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8],
]

weights: List[List[float]] = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87],
]

biases: List[float] = [2, 3, 0.5]

weights2: List[List[float]] = [
    [0.1, -0.14, 0.5],
    [-0.5, 0.12, -0.33],
    [-0.44, 0.73, -0.13],
]

biases2: List[float] = [-1, 2, -0.5]

layer1_output = np.dot(inputs, np.array(weights).T) + biases

print(layer1_output)
"""
[[ 4.8    1.21   2.385]
 [ 8.9   -1.81   0.2  ]
 [ 1.41   1.051  0.026]]
"""

layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2
print(layer2_output)
"""
[[ 0.5031  -1.04185 -2.03875]
 [ 0.2434  -2.7332  -5.7633 ]
 [-0.99314  1.41254 -0.35655]]
"""