library(mosaic)
library(tidyverse)
# linear regression
mylm <- lm(length ~ width, data = KidsFeet)
summary(mylm)

RT <- RailTrail

RT$Season <- as.factor(with(RT, 2*spring + 3*summer + 2*fall))

#anova
rt.aov <- aov(precip ~ Season, data = RT)
summary(rt.aov)    

par(mfrow = c(1,2))
plot(chick.aov, which = 1:2)  

# linear regression
rt.lm <- lm(volume ~ hightemp + Season + Season:hightemp, data=RT)
summary(rt.lm)

KidsFeet$length[KidsFeet$birthyear==88] %>% mean()

#logisic regression
trash.glm <- glm( (sex == 'B') ~ width, data=KidsFeet, family=binomial)
summary(trash.glm)

predict(trash.glm, newdata = data.frame(width = 9.5), type = "response")

#nonparamtric 

wilcox.test(KidsFeet$width,
            mu = 0, paired=FALSE, alternative = “two.sided”, conf.level = 0.95)

wilcox.test(KidsFeet$width, mu = 8, alternative = 'two.sided', paired=FALSE, conf.level = 0.95)

their.glm <- glm( (volume>350) ~ hightemp + weekday, data=RailTrail, family=binomial)

plot ( (volume>350)  ~ hightemp, 
      data=RailTrail, col=weekday, ylim= c(0,1),
      ylab="Probability there are Over 200 Trail Users", 
      xlab="Daily High Temperature") 
#Don't spend too much time reading the plotting code. It's just a fancy way of showing the data more clearly in the plot.

b <- coef(their.glm)
curve(exp(b[1]+b[2]*x)/(1+exp(b[1]+b[2]*x)), add=TRUE)


RT <- RailTrail

RT$Season <- as.factor(with(RT, spring + 4*summer + 3*fall))

warp.aov <- aov(hightemp ~ weekday + Season + weekday:Season, data = RT)
summary(warp.aov)    

par(mfrow = c(1,2))
plot(warp.aov, which = 1:2) 

trash.glm <- glm( (Season == 4) ~ avgtemp, data=RT, family=binomial)
summary(trash.glm)

RT <- RailTrail

RT$Season <- as.factor(with(RT, spring + 2*summer + 3*fall))
kruskal.test(volume ~ Season, data = RT)

boxplot(volume ~ Season, data=RT, col='grey', ylab="Hourly Wage", main="Math 221 Students", xlab="Class Rank")


mylm <- lm(length ~ width, data = KidsFeet)
summary(mylm)

par(mfrow=c(1,3))
plot(mylm,which=1:2)
plot(mylm$residuals)

mylm <- lm(hightemp~lowtemp, data=RT)
summary(mylm)
plot(hightemp~lowtemp, data=RT)
abline(mylm)

predict(mylm, data.frame(lowtemp=50))

tg <- RailTrail %>% filter(summer == 1)

t.test(RT[summer==1], mu = 20, alternative = “two.sided”, conf.level = 0.95) 
t.test(hightemp ~ weekday, data = tg, mu = 0, alternative = 'two.sided', conf.level = 0.95)
