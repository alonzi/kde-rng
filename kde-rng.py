# Demonstration in R of creating a random number generator from kernel density estimation       

# Packages
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt




# generate data from standard normal distribution
np.random.seed(42)
data = np.random.randn(100)

# estimate the kernel density
kde = stats.gaussian_kde(data)

# generate random numbers from the kernel density
random_numbers = kde.resample(1000)

# make a rug plot of the data
plt.plot(data, np.zeros_like(data), '|', color='black')
plt.plot(random_numbers, np.zeros_like(random_numbers)+1, '|', color='blue')
plt.ylim(-1, 2)  # Set y-axis range from -1 to 2
plt.show()

