mean(airquality$Temp)
?airquality
a <- airquality
a$Celcius <- (a$Temp - 32) * 5/9\
a
plot(Temp ~ Ozone, 
     data=airquality, 
     pch=1)  

hist(airquality$Ozone, col="azure") 

yeah <- CO2 %>% 
  filter(Treatment == "chilled" & conc == 250) 

que <- CO2 %>% 
filter(Treatment == "chilled" & conc == 250 & Type == 'Quebec') 
 
Miss <- CO2 %>% 
  filter(Treatment == "chilled" & conc == 250 & Type == 'Mississippi') 
 
mean(que$uptake)

ggplot(CO2, aes(x=Type, y=))+ 
  geom_dotplot()
coord_flip( ) +
geom_dotplot(binaxis = "y", stackdir = "up", position = "dodge", dotsize = 0.75, binwidth = 0.5)

stripchart(uptake ~ Type, data=yeah, method="stack")

favstats(que$uptake)

t.test(uptake ~ Type, data = yeah, mu = 0, alternative = "two.sided", conf.level = 0.95)


