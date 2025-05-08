import numpy as np
import matplotlib.pyplot as plt

# Sample data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 6, 8])

# Perform linear least squares fit
slope, intercept = np.polyfit(x, y, 1)  # 1 means linear fit

# Generate fitted line
y_fit = slope * x + intercept

# Plot data points and best-fit line
plt.scatter(x, y, label='Data points')
plt.plot(x, y_fit, color='red', label=f'Best-fit line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Linear Least Squares Fit')

plt.show()
