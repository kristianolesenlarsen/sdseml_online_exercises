install.packages("grf")

library(grf)
library(tidyverse)

df <- read.csv("simulated_data.csv")
# 5.1.6 Extracting T as matrix
head(df)
# and splitting Xs and y in seperate matrices

X <- df %>%
  select(X0, X1, X2, X3, X4, D) %>% 
  as.matrix()

y <- df %>%
  select(y) %>% 
  as.matrix()

W <- df %>%
  select(T) %>%
  as.matrix(T)

# 5.1.7
?causal_forest
#cf <- causal_forest(X,y,W) # on X, y and treatment T=W
# the function complains since W is not numeric but logical, i.e. true/false
# need to turn W with "True" and "False" into numeric, binary 1 and 0 for treatment
W<-as.numeric(W[,1] == "True" )
cf <- causal_forest(X,y,W)
tau <- predict(cf,X)

write.csv(tau, "individual_treatment_effects.csv")
