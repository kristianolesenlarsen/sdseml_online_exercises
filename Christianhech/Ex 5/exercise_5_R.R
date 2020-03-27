install.packages("tidyverse")
install.packages("grf")
library(tidyverse)
library(grf)
install.packages("magrittr") # package installations are only needed the first time you use it
install.packages("dplyr")    # alternative installation of the %>%
library(magrittr) # needs to be run every time you start R and want to use %>%
library(dplyr)    # alternatively, this also loads %>%


df = read.csv("simulated_data.csv")

X <- df %>%
  select(X0, X1, X2, X3, X4, D) %>% 
  as.matrix()

y <- df %>%
  select(y) %>% 
  as.matrix()

W <- df %>%
  select(T) %>% 
  as.matrix()

cf <- causal_forest(X, y, W)
tau <- predict(cf, X)

write.csv(tau, "individual_treatment_effects.csv")