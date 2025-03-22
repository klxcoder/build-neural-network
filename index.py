import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Test NumPy
print("NumPy Test:", np.array([1, 2, 3]) + 1)

# Test Pandas
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print("Pandas Test:\n", df)

# Test Matplotlib
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Matplotlib Test")
plt.show()
