
library(mosaic)
?SaratogaHouses

SH2 <- filter(SaratogaHouses, bedrooms == 3,  newConstruction=="Yes")
View(SH2)

mylm <- lm(price ~ livingArea + fireplaces + fireplaces:livingArea, data = SH2)
summary(mylm)

plot(price ~ livingArea, data = SH2, col=c("skyblue","orange")[as.factor(fireplaces)], pch=21, bg="gray83", main="Two-lines Model using SH2 data set", cex.main=1)
legend("topleft", legend=c("Baseline (fireplace==0)", "Changed-line (fireplace==1)"), bty="n", lty=1, col=c("skyblue","orange"), cex=0.8)

b <- coef(mylm)
# Then b will have 4 estimates:
# b[1] is the estimate of beta_0: -9.0099
# b[2] is the estimate of beta_1:  1.4385
# b[3] is the estimate of beta_2: -14.5107
# b[4] is the estimate of beta_3: 1.3214
curve(b[1] + b[2]*x, col="skyblue", lwd=2, add=TRUE)  #baseline (in blue)
curve((b[1] + b[3]) + (b[2] + b[4])*x, col="orange", lwd=2, add=TRUE) #changed line (in orange)


par(mfrow=c(1,3))
plot(mylm, which=1)
qqPlot(mylm$residuals, id=FALSE)
plot(mylm$residuals)

?airquality
View(airquality)

(lm.quad <-lm(Temp ~ Month + I(Month^2), data=airquality))

par(mfrow=c(1,3))
plot(lm.quad, which=1)
qqPlot(lm.quad$residuals, id=FALSE)
plot(lm.quad$residuals)

predict(lm.quad,newdata = data.frame(X1=7))

plot(Temp ~ Month, data=airquality, col="skyblue", pch=21, bg="gray83", main="Quadratic Model using airquality data set", cex.main=1)

#get the "Estimates" automatically:
b <- coef(lm.quad)
# Then b will have 3 numbers stored inside:
# b[1] is the estimate of beta_0: -95.73
# b[2] is the estimate of beta_1: 48.72
# b[3] is the estimate of beta_2: -3.28
curve(b[1] + b[2]*x + b[3]*x^2, col="skyblue", lwd=2, add=TRUE)

lines(c(7.129, 7.129), c(0, 84.78), lty=2, col="firebrick")

lines(c(0, 7.129), c(84.78, 84.78), lty=2, col="firebrick")

points(7.129, 84.78, cex=1.2, col="red")

text(7.129, 84.78, "Predicted Temp", cex=0.5, pos=3)

library(mosaic)
?RailTrail
View(RailTrail)

RailTrail <- RailTrail %>% mutate(rain = case_when( RailTrail$precip > 0 ~ 1, TRUE ~0))

palette(c("orange","skyblue"))
plot(volume ~ hightemp, data=RailTrail, col=as.factor(rain), main="RailTrail Data Set")
legend("topleft", legend=c("No Rain", "Rain"), col=palette(), pch=16)

curve( 46.6863 + 5.1655*x, add=TRUE, col="orange")
curve(-36.6327+ 5.1655*x, add=TRUE, col="skyblue")

mylm <- lm(volume ~ hightemp + rain + rain:hightemp, data = RailTrail)
summary(mylm)

mylm <- lm(volume ~ hightemp + rain, data = RailTrail)
summary(mylm)

par(mfrow=c(1,3))
plot(mylm, which=1)
qqPlot(mylm$residuals, id=FALSE)
plot(mylm$residuals)

library(mosaic)
View(KidsFeet)
?KidsFeet

mylm <- lm(length ~ width + sex + sex:width, data = KidsFeet)
summary(mylm)

View(cars)
?cars

mylm <- lm(dist ~ speed, data = KidsFeet)
summary(mylm)

lm.quad <-lm(dist ~ speed + I(speed^2), data=cars)
summary(lm.quad)

