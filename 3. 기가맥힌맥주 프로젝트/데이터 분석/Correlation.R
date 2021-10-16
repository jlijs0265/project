library(readr); library(dplyr); library(stats); library(ggplot2); library(corrplot)

bier <- read.csv('beer_data_trans_weight.csv')
head(bier)
bier %>% str
bier %>% summary
bier %>% colnames
cor(bier)

ggplot(data=bier) + geom_histogram()
corrplot(cor(bier),method = 'color', addCoef.col='Black',order='hclust')

bier_t <- bier[4:14]
corrplot(cor(bier_t),method = 'color', addCoef.col='Black')

summary(lm(ABV ~ Alcohol, bier))
ggplot(bier_t,aes(Sour,Fruits)) + geom_point() + geom_smooth(method=stats::lm)
ggplot(bier_t,aes(Sour,Fruits)) + geom_point() + geom_smooth
plot(Salty ~ Fruits,bier_t) + abline(lm(Sour ~ Fruits, bier_t))
ggplot(bier,aes(ABV,Alcohol)) + geom_point() + geom_smooth(method=stats::lm)
