from typing import List

inputs: List[float] = [1.2, 5.1, 2.1]
weights: List[float] = [3.1, 2.1, 8.7]
bias: float = 3

sum: float = inputs[0] * weights [0] + inputs[1] * weights [1] + inputs[2] * weights [2]

output: float = sum + bias

print(sum) # 32.7
print(output) # 35.7