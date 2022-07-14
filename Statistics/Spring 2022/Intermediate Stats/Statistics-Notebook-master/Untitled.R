airquality %>%
  summarise(mean = mean(airquality$Wind), std =sd(airquality$Wind), median = median(airquality$Wind), min = min(airquality$Wind), max = max(airquality$Wind))

airquality %>%
  ggplot(aes(x=Temp, y=Wind)) + 
  geom_point(color = 'gray') +
  labs(x = 'Daily Average Temperature', y = 'Daily Average Wind Speed')

airquality %>%
  ggplot(aes(x=Solar.R)) + 
  geom_histogram(fill = 'orange', color = 'black', bins = 7) +
  labs(x = 'RAd', y = 'Freq') +
  theme_classic()

ggplot(airquality, aes(x=Month, y=Solar.R)) +
  geom_boxplot()

boxplot(Solar.R ~ Month, data=airquality)

boxplot(Solar.R ~ Month,
        data = airquality,
        col=c("gray","gray","orangered","gray","gray"),
        main='DAuily Radiation',
        xlab='Month',
        ylab='Radiation') 
       