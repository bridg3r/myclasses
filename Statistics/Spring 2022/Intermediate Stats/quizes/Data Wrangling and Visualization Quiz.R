library(mosaic)
library(tidyverse)

table(KidsFeet$domhand, KidsFeet$sex)
?airquality
View(airquality)

summary()
mean(airquality$Wind)

KidsFeet %>%
  group_by(sex) %>% 
  summarise(min = min(length),
            Q1 = quantile(length, 0.25),
            med = median(length), 
            Q3 = quantile(length, 0.75), 
            max = max(length),
            max = max(length),
            std = sd(length),
            sampleSize = n())

airquality %>%
  group_by(Month) %>% 
  summarise(mean = mean(Temp))

stripchart(Temp ~ Month, data=airquality, ylab="Month", xlab="Temperature", main="LaGuardia Airport (May to September 1973)", pch=16, col="slategray", method="stack")

?airquality
View(airquality) 
library(mosaic)

?Orange
View(Orange)

Orange %>%
  group_by(age) %>% 
  summarise(medain_circ =median(circumference))

airquality %>% 
  group_by(Month) %>% 
  summarise(mt = mean(Temp))


library(mosaicData)
View(Riders)
Riders %>%
  group_by(day) %>% 
  summarise( num=sum(riders))

mtcars %>% 
filter(cyl == 8) %>% 
  group_by(am) %>% 
  summarise(num = mean(hp))

g <- mtcars %>%
  arrange(cyl, wt)

View(g)

mtcars %>% 
  group_by(am) %>% 
  summarise(num = mean(hp))

ggplot(mtcars, aes(x=carb, y = qsec)) +
  geom_point()

palette(c("skyblue","firebrick"))

plot(mpg ~ qsec, data=mtcars, col=as.factor(am), pch=16, xlab="Quarter Mile Time (seconds)", ylab="Miles per Gallon", main="1974 Motor Trend Vehicles")
legend("topright", pch=16, legend=c("automatic","manual"), title="Transmission", bty='n', col=palette())
