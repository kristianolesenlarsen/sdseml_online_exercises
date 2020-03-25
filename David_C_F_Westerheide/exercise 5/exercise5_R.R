#Exercise 5
#install.packages("tidyverse")
#install.packages("grf")
library(tidyverse)
library(grf)

df=read.csv("exercise5_R.csv")

X <- df %>% select(X0, X1, X2, X3, X4, D) %>% as.matrix()
y <- df %>% select(y) %>% as.matrix()
W <- df %>% select(T) %>% as.matrix()

cf <- causal_forest(X,y,W)
tau <- predict(cf, X)
write.csv(tau, "individual_treatment_effects.csv")
