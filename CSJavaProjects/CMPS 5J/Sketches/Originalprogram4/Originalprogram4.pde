//outer pattern variables
float x=0;
float y=0;

//inner pattern variables
float w=100;
float z=100;

void setup()
{
  size(500, 500);
  background(255);
}

void draw()
{
 
  
  //Draw Outer Pattern
  while(x<500 && y<500)
  {
  noStroke();
  fill(255, 0, 0);
  rect(x,y, 50, 50);
  fill(0);
  triangle(x+1, y+1, x+49, y+1, x+25, y+25);
  triangle(x+1, y+49, x+49, y+49, x+25, y+25);
  fill(255);
  triangle(x+1, y+1, x+1, y+49, x+25, y+25);
  triangle(x+49, y+1, x+49, y+49, x+25, y+25);
  
  x=x+50;
  


  }
 
  
  //Draw inner Pattern
   while(w<400 && z<400 )
  {
    noStroke();
  fill(255, 0, 0);
  rect(w,z, 50, 50);
  fill(255);
  triangle(w+1, z+1, w+49, z+1, w+25, z+25);
  triangle(w+1, z+49, w+49, z+49, w+25, z+25);
  fill(0);
  triangle(w+1, z+1, w+1, z+49, w+25, z+25);
  triangle(w+49, z+1, w+49, z+49, w+25, z+25);
  
  w=w+50;
  
  }
  

x=0;
z=z+50;
w=100;
y=y+50;
  

  


  
}