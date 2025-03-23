import math
import numpy as np

layer_outputs = [4.8, 1.21, 2.385]

# E = 2.71828182846
E = math.e

exp_values = np.exp(layer_outputs)
print(exp_values) # [121.51041752   3.35348465  10.85906266]

norm_values = exp_values / np.sum(exp_values)
print(norm_values) # [0.89528266 0.02470831 0.08000903]
print(np.sum(norm_values)) # 0.9999999999999999