import sys
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

print('Python:', sys.version) # Python: 3.10.16 (main, Dec 11 2024, 16:24:50) [GCC 11.2.0]
print('Numpy:', np.__version__) # Numpy: 2.2.4
print('Matplotlib:', matplotlib.__version__) # Matplotlib: 3.10.1

# Test NumPy
print("NumPy Test:", np.array([1, 2, 3]) + 1)

# Test Pandas
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print("Pandas Test:\n", df)

# Test Matplotlib
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Matplotlib Test")
plt.show()
