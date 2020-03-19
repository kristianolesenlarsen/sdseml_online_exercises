rm(list=ls())
library(Rcpp)


library(tidyverse)
library(grf)


### tried to solve it with this code, but get an error message which says: 
### In install.packages("Rcpp") :
### Installation des Pakets ???Rcpp??? hatte Exit-Status ungleich 0

### which means that the installation of the Rcpp package failed, which is somehow essential for tidyverse or grf
### exit-status is unequal to zero
### still trying to find out where the error is

setwd("~/Desktop/UCPH/Social Data Science/Exercises")
df <- read.csv("simulated_data.csv")


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
