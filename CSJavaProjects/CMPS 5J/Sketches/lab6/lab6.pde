//Bridger's code that changes F(Ferenheit) to C(Celsius)

//Input number to the function
void draw()
{
  convertToCelsius(50.0);
 noLoop(); 
}

// Create function that uses Formula: C = (F – 32) * (5/9)
void convertToCelsius(float F)
{
  float C = (F - 32.0)/9 * (5);
  
 println(C);

}