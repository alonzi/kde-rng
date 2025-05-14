# Demonstration in R of creating a random number generator from kernel density estimation       









# generate data from standard normal distribution
set.seed(42)
data <- rnorm(10)

# estimate the kernel density
density <- density(data)

# generate random numbers from the kernel density
random_sample <- sample(density$x, size=1000, replace=TRUE, prob=density$y)

# plot the random numbers
plot(data, rep(0, length(data)), pch=16, col="black", xlab="Value", ylab="", main="Rug Plot of Data",xlim=c(-3, 3), ylim=c(-1, 2))
points(random_sample, rep(1, length(random_sample)), pch=16, col="blue")

