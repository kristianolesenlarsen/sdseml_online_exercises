
setwd("/Users/madslangsorensen/Nextcloud/Dokumenter/SDS - eandml/")

df <- read.csv(file.path("synth_data"), stringsAsFactors=FALSE)

library('tidyverse')
library('grf')

X <- df %>%
  select(X0, X1, X2, X3, X4) %>% 
  as.matrix()

y <- df %>%
  select(y) %>% 
  as.matrix()

W <- df %>%
  select(D) %>%
  as.matrix()


tau.forest <- causal_forest(X, y, W)
tau.forest

tau <- predict(tau.forest, X)

write.csv(tau, "individual_treatment_effects.csv")
