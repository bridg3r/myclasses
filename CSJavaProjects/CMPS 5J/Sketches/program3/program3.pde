//Mouse Eating Cheese by Bridger Hackworth

int mouseCount=0;
float angle=0;

void setup() {
 size(500, 500);
}

void draw() {
 background(255);

 translate(150, 82);
 
//Move the Mouse in and out of Grass
 if (mouseCount < 82 )
 {translate(0, -mouseCount);
 }
if(mouseCount >= 82)
{
  translate(0, -164+mouseCount);
}

  //Draw Mouse
 //Body
 fill(125);
 triangle(95, 160, 105, 160, 100, 230); 
 ellipse(100, 180, 20, 40);
 ellipse(100, 160, 15, 15);
 ellipse(100, 153, 7, 10);
 fill(0);
 ellipse(100, 148, 3, 3);
 //Ears
 fill(100);
 ellipse(95, 166, 8, 10);
 ellipse(105, 166, 8, 10);
 fill(250, 141, 187);
 ellipse(95, 166, 6, 8);
 ellipse(105, 166, 6, 8);
 fill(125);
 rect(93, 160, 15, 3); 
 //Eyes
 fill(255);
 ellipse(97, 155, 5, 5);
 ellipse(103, 155, 5, 5);
 fill(0);
 ellipse(97, 153, 2, 2);
 ellipse(103, 153, 2, 2);
 
 //Keep Cheese from moving
  if (mouseCount < 82 )
 {translate(0, +mouseCount);
 }
 else
{
translate(0, 164-mouseCount);
} 

 
 //Draw Grass
 translate(-150, -76);
 fill(0, 150, 0);
rect(0, 220, 500, 300); 

//Spin Cheese
translate(width/2, 120);
rotate(angle);
translate(-width/2, -120);

translate(150, 20);
 //Draw Cheese
 noStroke();
 fill(254, 255, 0);
 rect(80, 80, 40, 40);
 fill(255);
 ellipse(80, 80, 10, 10);
 ellipse(95, 110, 10, 10);
 ellipse(100, 90, 10, 10);
 ellipse(115, 100, 8, 8);
 
 
 if (mouseCount == 164)
 {
 mouseCount = 0;
 }
 else
 {
 mouseCount = mouseCount + 1;
 }
angle=angle+.15;


}