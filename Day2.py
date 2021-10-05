import numpy as np
import matplotlib.pyplot as plt
height = np.random.normal(140,20,1000)
plt.figure(dpi=200)
plt.title("Height Distribution")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.hist(height, bins=30, ec="gold")
plt.show()