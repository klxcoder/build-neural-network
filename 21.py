import math

layer_outputs = [4.8, 1.21, 2.385]

# E = 2.71828182846
E = math.e

exp_values = [E**output for output in layer_outputs]
print(exp_values) # [121.51041751873483, 3.353484652549023, 10.859062664920513]

norm_base = sum(exp_values)
print(norm_base) # 135.72296483620437

norm_values = [value/norm_base for value in exp_values]
print(norm_values) # [0.8952826639572619, 0.024708306782099374, 0.0800090292606387]
print(sum(norm_values)) # 0.9999999999999999