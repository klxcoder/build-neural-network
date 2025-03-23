inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
output = [max(i, 0) for i in inputs]

print(output) # [0, 2, 0, 3.3, 0, 1.1, 2.2, 0]