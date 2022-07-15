glasses <- cbind( Males = c(Glasses = 5, Contacts = 12, None = 18), Females = c(Glasses = 4, Contacts = 14, None = 22))

glasses

barplot(glasses, beside=TRUE, legend.text=TRUE, args.legend=list(x = "topleft", bty="n"))


chis.glasses <- chisq.test(glasses)

chis.glasses$expected 

chis.glasses$residuals

education <- cbind( `United States` = c(Engineering = 61941, `Natural Science` = 111158, `Social Science` = 182166), `Western Europe` = c(Engineering = 158931, `Natural Science` = 140126, `Social Science` = 116353), Asia = c(280772, 242879, 236018))

education

barplot(education, beside=TRUE, legend.text=TRUE, args.legend=list(x = "topleft", bty="n"))

chis.education <- chisq.test(education)

chis.education$expected 

chis.education$residuals

View(InsectSprays)

barplot(InsectSprays, beside=TRUE, legend.text=TRUE, args.legend=list(x = "topleft", bty="n"))

chis.insect <- chisq.test(InsectSprays)

chis.insect$expected 

chis.insect$residuals

ins.aov <- aov(count ~ spray, data = InsectSprays)
summary(ins.aov)

par(mfrow = c(1,2))
plot(chick.aov, which = 1:2)


library(mosaic)

Kids2 <- KidsFeet %>%     
  mutate(        
    season = case_when(            
      birthmonth %in% c(12,1,2) ~ "Winter",            
      birthmonth %in% c(3,4,5) ~ "Spring",            
      birthmonth %in% c(6,7,8) ~ "Summer",            
      birthmonth %in% c(9,10,11) ~ "Fall"        
    )    
  )

x <- table(Kids2$domhand, Kids2$season)

chis.kids <- chisq.test(x)

barplot(x, beside=TRUE, legend.text=TRUE, args.legend=list(x = "topleft", bty="n"))

air2 <- airquality %>%
  mutate(Wind12 = case_when(Wind > 12 ~ "Windy", TRUE ~ "Calm"),
         Temp80 = case_when(Temp > 80 ~ "Hot", TRUE ~ "Fair"))

x <- table(air2$Wind12, air2$Temp80)

chis.kids <- chisq.test(x)


