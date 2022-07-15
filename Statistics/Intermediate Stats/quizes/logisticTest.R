View(infert)
?infert
infert.glm <- glm( (spontaneous > 0) ~ age, data=infert, family=binomial)

summary(infert.glm)
plot( (spontaneous > 0) ~ age, data=infert)

table(infert$age)

pchisq(334.01, 246, lower.tail=FALSE)


library(mosaic)
View(Galton)
?Galton

Galton2 <- Galton %>% mutate(sex = case_when(Galton$sex == 'M' ~ 1,
                                                 Galton$sex == 'F' ~ 0))

galton.glm <- glm( (sex == 'M') ~ height, data=Galton, family=binomial)
summary(galton.glm)

plot( sex == 'M' ~ height, data=Galton)

#Getting the coeffiencts
b <- coef(galton.glm)
curve(exp(b[1]+b[2]*x)/(1+exp(b[1]+b[2]*x)), add=TRUE)

exp(b[2])

predict(galton.glm, newdata = data.frame(height = 65), type = "response")

library(ResourceSelection)
hoslem.test(galton.glm$y, galton.glm$fitted, g=10)


iris.glm <- glm( (Species == 'setosa') ~ Petal.Width, data=iris, family=binomial)
summary(iris.glm)

plot( Species == 'setosa' ~ Petal.Width, data=iris)

#Getting the coeffiencts
b <- coef(iris.glm)
curve(exp(b[1]+b[2]*x)/(1+exp(b[1]+b[2]*x)), add=TRUE)



