import numpy as np

softmax_output = np.array([
    [0.7, 0.1, 0.2],
    [0.1, 0.5, 0.4],
    [0.02, 0.9, 0.08],
])

class_targets = [0, 1, 1]

print(softmax_output[
    range(len(softmax_output)),
    class_targets,
]) # [0.7 0.5 0.9]

print(-np.log([0.7, 0.5, 0.9])) # [0.35667494 0.69314718 0.10536052]

neg_log = -np.log(softmax_output[
    range(len(softmax_output)),
    class_targets,
])

print(neg_log) # [0.35667494 0.69314718 0.10536052]

average_loss = np.mean(neg_log)

print(average_loss) # 0.38506088005216804