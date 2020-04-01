# Retrive packages
install.packages(c("grf", "ggplot2", "hexbin", "utils", "tidyverse"))
Packages <- c("grf", "ggplot2", "hexbin", "utils", "tidyverse", "readr")
lapply(Packages, library, character.only = TRUE)

# Set working directory
setwd("C:/Users/mfr.eco/Dropbox/PhD/Machine learning/SDS2020/Week 5/session_5")
getwd()

############## 4.1.5 ###############
# Copy the following code into R to split your dataframe into two matrices, X, and y. 
# Implement the exact same procedure to create a third matrix W which contains the
# treatment indicator (Note T is a reserved name in R, so name your third matrix W).

### Read and view data
df <- read_csv("data_exercise5")
View(df)

# Rename treatment variable
install.packages("gdata")
library("gdata")
df=rename.vars(df, from="T", to="W", info=TRUE)

View(df)

## Split data frame
X <- df %>%
  select(X0, X1, X2, X3, X4, D) %>% 
  as.matrix()

y <- df %>%
  select(y) %>% 
  as.matrix()

W <- df %>%
  select(W) %>% 
  as.matrix()

############## 4.1.6 ###############

# Estimate a causal forest model using the GRF package, and store the result 
# in a new variable cf. Then use the following line to create a dataframe of 
# predicted treatment effects on the same data that you trained the model on. 

cf <- causal_forest(X, y, W)
tau <- predict(cf, X)

# Add predictions to dataframe
data<-cbind(df, tau)

#Check
head(data)

# Export as csv
write.csv(data)

attach(data)
plot(X0, predictions, main="Scatterplot, X0 and tau",
     xlab="X0 ", ylab="Predictions", pch=19)