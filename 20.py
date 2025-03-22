import math

layer_outputs = [4.8, 1.21, 2.385]

# E = 2.71828182846
E = math.e

exp_values = [E**output for output in layer_outputs]

print(exp_values) # [121.51041751873483, 3.353484652549023, 10.859062664920513]