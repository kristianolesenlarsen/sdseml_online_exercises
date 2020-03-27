library(magrittr)
library(tidyverse)
library(grf)

# Read data
df <- read.csv("data.csv", header = TRUE)

# Create matrices
X <- df %>%
  select(X0, X1, X2, X3, X4, D) %>%
  as.matrix()

y <- df %>%
  select(y) %>%
  as.matrix()

W <- df %>%
  select(Treat) %>%
  as.matrix()

# Train a causal forest
cf <- causal_forest(X, y, W)

# Predict treatment effects
tau <- predict(cf, X)

# Save predicted treatment effects
write.csv(tau, "individual_treatment_effects.csv")
