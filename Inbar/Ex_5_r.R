library(tidyverse)
library(grf)

df <- read.csv("~/Dropbox/Msc/Econ & ML/Ex_5.csv")

X <- df %>% select(X0, X1, X2, X3, X4, D) %>% as.matrix()

Y <- df %>% select(Y1) %>% as.matrix()

W <- df %>% select(Tau) %>% as.matrix()

# Train a causal forest.
tcf <- causal_forest(X, Y, W)

# Estimate treatment effects for the training data using out-of-bag prediction.
tau <- predict(tcf)
#hist(tau.hat.oob$predictions)


plot(df$Tau, tau$predictions)