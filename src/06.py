from typing import List

import numpy as np

inputs: List[float] = [1, 2, 3, 2.5]
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

output = [np.dot(neuron_weights, inputs) + neuron_bias for neuron_weights, neuron_bias in zip(weights, biases)]

print(output) # [np.float64(4.8), np.float64(1.21), np.float64(2.385)]