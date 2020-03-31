library("tidyverse")
library("grf")
library("dplyr")

setwd("/Users/karlbindslev/Documents/Studie/SDS_Econometrics_ML/Exercises")

df = read_csv("/Users/karlbindslev/Documents/Studie/SDS_Econometrics_ML/Exercises/Ex5_export_to_R.csv", col_names = TRUE)


### ----- Ex. 4.1.5: 
X <- df %>% select(X0, X1, X2, X3, X4, D) %>% as.matrix()
y <- df %>% select(y) %>% as.matrix()
W <- df %>% select(T) %>% as.matrix() # name the matrix W, since T is reserved in R


### ----- Ex. 4.1.6:

# set up a causal forest:
cf <- causal_forest(X, y, W)

# Estimate treatment effects for the training data using out-of-bag prediction.
tau <- predict(cf)
hist(tau.hat.oob$predictions)

# save the treatment effects in a csv file:
write.csv(tau, "individual_treatment_effects.csv", row.names=FALSE)

