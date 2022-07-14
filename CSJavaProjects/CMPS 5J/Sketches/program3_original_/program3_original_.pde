//Mouse Chasing Cheese by Bridger Hackworth

int cheeseCount=0;
float cheeseAngle=0;

//int circleX=0;
void setup() {
 size(500, 500);
}

void draw() {
 background(0);
 
 
 //Maze 
 fill(255);
 rect(50, 50, 400, 400);
 fill(0);
 rect(150, 150, 200, 200);
 
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
 
 
 //Move the Cheese
 if(cheeseCount/300 < 1)
 {
 translate(cheeseCount, 0);
 }
 else
 { translate (300, 0);
 }
 
  if(cheeseCount-300 > 0)
  {
    translate(0, cheeseCount-300);
}
 
 if (cheeseCount-600 > 0)
 {
   translate (0, -cheeseCount+300);
   translate(-cheeseCount+600, 300);
 }
 
 if (cheeseCount-900 > 0)
 {
   translate(cheeseCount-600,0);
   translate(-300, -cheeseCount+900);
   
 }

 
 //Cheese
 noStroke();
 fill(254, 255, 0);
 rect(80, 80, 40, 40);
 fill(255);
 ellipse(80, 80, 10, 10);
 ellipse(95, 110, 10, 10);
 ellipse(100, 90, 10, 10);
 ellipse(115, 100, 8, 8);
 
 if (cheeseCount == 1200)
 {
 cheeseCount = 0;
 }
 
 else
 {
 cheeseCount = cheeseCount + 6;
 }


}