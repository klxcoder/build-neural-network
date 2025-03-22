from typing import List

inputs: List[float] = [1, 2, 3, 2.5]
weights: List[float] = [0.2, 0.8, -0.5, 1.0]
bias: float = 2

sum: float = inputs[0] * weights [0] + inputs[1] * weights [1] + inputs[2] * weights [2] + inputs[3] * weights [3]

output: float = sum + bias

print(sum) # 2.8
print(output) # 4.8