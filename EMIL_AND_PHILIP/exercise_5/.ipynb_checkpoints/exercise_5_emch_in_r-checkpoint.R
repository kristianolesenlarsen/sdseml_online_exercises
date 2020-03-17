library('tidyverse')
library('grf')

# Load dataframe from drive
drive <- "C:\\Users\\pdj165\\Documents\\PhD-kursur\\econometrics_and_ml\\sdseml_online_exercises\\EMIL_AND_PHILIP\\exercise_5\\"
df    <- read.csv(paste0(drive,'reg_data.csv')) 


## create matrices for grf computations
X <- df %>%
  select(X0,X1,X2,X3,X4,D) %>%
  as.matrix()

y <- df %>%
  select(y) %>%
  as.matrix()

W <- df %>%
  select(D) %>%
  as.matrix()


## EXERCISE TASKS 
cf       <- causal_forest(X,y,W)
tau_pred <- predict(cf,X)

## Add predicted treatment effects to df
df$tau_pred_grf <- tau_pred$predictions

## Write the new df to new .csv-file
write.csv(df,paste0(drive,"individual_treatment_effects.csv"))



##########################################################################################
## SANDBOX PLAYING AROUND grf USING DOCUMENTATION IN https://github.com/grf-labs/grf)   ##
##########################################################################################

## Train a causal forest 
tau.forest <- causal_forest(X,y,W)


# Estimate treatment effects for the training data using out-of-bag prediction.
tau.hat.oob <- predict(tau.forest)
hist(tau.hat.oob$predictions)

# Estimate the conditional average treatment effect on the full sample (CATE).
average_treatment_effect(tau.forest, target.sample = "all")

# Estimate the conditional average treatment effect on the treated sample (CATT).
# Here, we don't expect much difference between the CATE and the CATT, since
# treatment assignment was randomized.
average_treatment_effect(tau.forest, target.sample = "treated")







