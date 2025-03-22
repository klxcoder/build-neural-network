from typing import List

import numpy as np

inputs: List[List[float]] = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8],
]
weights1: List[float] = [0.2, 0.8, -0.5, 1.0]
weights2: List[float] = [0.5, -0.91, 0.26, -0.5]
weights3: List[float] = [-0.26, -0.27, 0.17, 0.87]

weights: List[List[float]] = [
    weights1,
    weights2,
    weights3,
]

bias1: float = 2
bias2: float = 3
bias3: float = 0.5

biases: List[float] = [2, 3, 0.5]

output = np.dot(inputs, np.array(weights).T) + biases

print(output)
"""
[[ 4.8    1.21   2.385]
 [ 8.9   -1.81   0.2  ]
 [ 1.41   1.051  0.026]]
"""