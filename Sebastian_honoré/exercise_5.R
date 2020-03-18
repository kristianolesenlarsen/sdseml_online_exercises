library(tidyverse)
library(grf)

setwd("Desktop/POLIT/1. semester kandidat/Social data science/sds_eml_2020/material/session_5")

df <- read_csv("exercise_5.csv",col_names = TRUE)

X <- df %>% select(X0, X1, X2, X3, X4, D) %>% as.matrix()
y <- df %>% select(y) %>% as.matrix()
W <- df %>% select(T) %>% as.matrix()

cf <- causal_forest(X, y, W)

tau <- predict(cf,X)

write.csv(tau, "individual_treatment_effects.csv")