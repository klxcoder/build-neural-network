def get_params(layer_sizes):
    # layer_sizes[0] is input layer
    weights = 0
    biases = 0
    for i in range(len(layer_sizes) - 1):
        weights += layer_sizes[i] * layer_sizes[i + 1]
        biases += layer_sizes[i + 1]
    return {
        'weights': weights,
        'biases': biases,
        'params': weights + biases,
    }

if __name__ == "__main__":
    print(get_params([10, 8, 8, 8, 2])) # {'weights': 224, 'biases': 26, 'params': 250}
    print(get_params([10, 16, 16, 16, 2])) # {'weights': 704, 'biases': 50, 'params': 754}
    print(get_params([10, 32, 32, 32, 2])) # {'weights': 2432, 'biases': 98, 'params': 2530}
    print(get_params([10, 64, 64, 64, 2])) # {'weights': 8960, 'biases': 194, 'params': 9154}
    print(get_params([10, 128, 128, 128, 2])) # {'weights': 34304, 'biases': 386, 'params': 34690}
