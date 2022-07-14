/*Draw a square with a a red outline made up of 4 traingles that are black and 
white in color. The square repeats across the entire window, but flips the color
of it's triangles in the center of the screen
*/

//pattern variables
float x=0;
float y=0;


void setup()
{
  size(500, 500);
  background(255);
}

void draw()
{

  //Draw Pattern
  while(x<500 && y<500)
  {
  //Draw red outline
  noStroke();
  fill(255, 0, 0);
  rect(x,y, 50, 50);
  //Flip the colors for inside pattern vs outside pattern
  if(x>=100 && x<400 && y>=100 && y<400)
  {
  fill(255);
  }
  else
  {fill(0);}
  //
  triangle(x+1, y+1, x+49, y+1, x+25, y+25);
  triangle(x+1, y+49, x+49, y+49, x+25, y+25);
   if(x>=100 && x<400 && y>=100 && y<400)
  {
  fill(0);
  }
  else
  {fill(255);}
  triangle(x+1, y+1, x+1, y+49, x+25, y+25);
  triangle(x+49, y+1, x+49, y+49, x+25, y+25);
  
  x=x+50;
  } 

x=0;
y=y+50;
  

  


  
}