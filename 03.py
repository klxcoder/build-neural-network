from typing import List

inputs: List[float] = [1, 2, 3]
weights: List[float] = [0.2, 0.8, -0.5]
bias: float = 2

sum: float = inputs[0] * weights [0] + inputs[1] * weights [1] + inputs[2] * weights [2]

output: float = sum + bias

print(sum) # 0.30000000000000004
print(output) # 2.3