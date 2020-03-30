### Set wd and load data 

setwd("/Users/madsemillarsen/Documents/Education/MachineLearning/sds_eml_2020/material/session_5")

df = read_csv("/Users/madsemillarsen/Documents/Education/MachineLearning/sds_eml_2020/material/session_5/ex5_simulated_data.csv", col_names = TRUE)


### Ex. 4.1.5: Split data into matrices 
X <- df %>% select(X0, X1, X2, X3, X4, D) %>% as.matrix()
y <- df %>% select(y) %>% as.matrix()
W <- df %>% select(T) %>% as.matrix() # W as T is reserved in R 


### Ex. 4.1.6: Estimate a causal forest model using the GRF package
cf <- causal_forest(X, y, W)

tau <- predict(cf, X)

# Save as csv
write.csv(tau, "individual_treatment_effects.csv", row.names=FALSE)

