void setup()
{
  size(600,600);
  frameRate(20);
}

void draw()
{
  
  float mouseSpeedX = abs(mouseX-pmouseX);
  float mouseSpeedY = abs(mouseY-pmouseY);
  float mouseSpeed=  sqrt(pow(mouseSpeedX, 2)+pow(mouseSpeedY, 2));
  float points = 500-mouseSpeed;



    if(points < 400 && points > 200)
    background(0, 0, 255);
    else{
    if(points <= 200)
    background(0, 255, 0);
    else
    background(255,0,0);
    }

  line(0, 200, 600, 200);
  line(0, 400, 600, 400);
  
  fill(0);
  rect(250, points, 100, 100);
  
 

}