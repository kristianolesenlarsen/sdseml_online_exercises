library(tidyverse)
library(grf)

df <- read.csv("~/Dropbox/Msc/Econ & ML/Ex_5.csv")

X <- df %>% select(x1, x2, x3, x4, x5, D) %>% as.matrix()

Y <- df %>% select(y) %>% as.matrix()

W <- df %>% select(T) %>% as.matrix()

# Train a causal forest.
cf <- causal_forest(X, Y, W)

# Estimate treatment effects for the training data using out-of-bag prediction.
tau <- predict(cf, X)
#hist(tau.hat.oob$predictions)

write.csv(tau, "individual_treatment_effects.csv")
