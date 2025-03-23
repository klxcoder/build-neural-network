import numpy as np

softmax_output = np.array([
    [0.7, 0.2, 0.1],
    [0.5, 0.1, 0.4],
    [0.02, 0.9, 0.08],
])

class_targets = [0, 1, 1]

predictions = np.argmax(softmax_output, axis=1)

accuracy = np.mean(predictions == class_targets)

print(accuracy) # 0.6666666666666666