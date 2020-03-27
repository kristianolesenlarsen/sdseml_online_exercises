# Ex. 4.1.4.
#install.packages("tidyverse")
#install.packages("grf")

library(grf)
library(tidyverse)

setwd("C:/Users/tcg865/Dropbox/PhD/Courses/Machin learning/session5/")
raw_data <- read.csv(file = 'export_dataframe.csv')

par_ols   <- read.csv(file = 'param_ols.csv')
par_bonus <- read.csv(file = 'param_bonus.csv')

aa = seq(-3, 3, length.out = 101)

X.test <- matrix(0, 101, 6)
X.test[, 1] <- seq(-3, 3, length.out = 101)

y <- raw_data %>%
  select(y) %>%
  as.matrix()

D <- raw_data %>%
  select(D) %>%
  as.matrix()

X <- raw_data %>%
  select(X0,X1,X2,X3,X4,X5) %>%
  as.matrix()

W = 1-D

tau.forest <- causal_forest(X, y, W)

# Estimate treatment effects for the training data using out-of-bag prediction.
tau.hat.oob <- predict(tau.forest)
hist(tau.hat.oob$predictions)

# Estimate treatment effects for the test sample.
tau.hat <- predict(tau.forest, X.test)
plot(X.test[, 1], tau.hat$predictions, ylim = range(tau.hat$predictions, 0, 2), xlab = "x", ylab = "tau", type = "l")
lines(X.test[, 1], 10/(1+exp(-3*X.test[, 1])), col = 2, lty = 2)

# Estimate the conditional average treatment effect on the full sample (CATE).
average_treatment_effect(tau.forest, target.sample = "all")

# Estimate the conditional average treatment effect on the treated sample (CATT).
# Here, we don't expect much difference between the CATE and the CATT, since
# treatment assignment was randomized.
average_treatment_effect(tau.forest, target.sample = "treated")

