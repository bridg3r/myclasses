Tribble[]Tribbles = new Tribble[200];


void setup() {
 size(400, 400);
 frameRate(20);
 // Initialize Tribble object
 for (int i = 0; i < Tribbles.length; i++) {
 Tribbles[i] = new Tribble(color(random(255), random(255), random(255)),
 random(10,390), random(10, 390), int(random(100)));
}
}

void draw() {
 background(255);
 // Operate Tribble object
 for (int i = 0; i < Tribbles.length; i++)
 {
 Tribbles[i].display();
 Tribbles[i].vibrate(); 
 }
//Makes tribbles appear fuzzy
filter(BLUR, 1);
}

class Tribble {
 color c;
 float xpos;
 float ypos;
 float counterV;
 
 Tribble(color c1, float xpos1, float ypos1, float counterV1) {
 c = c1; 
 xpos = xpos1; 
 ypos = ypos1; 
 counterV = counterV1; 
 }
 
 
 void display() {
 // The Tribble is a ellipse of random color
 fill(c);
 noStroke();
 ellipse(xpos, ypos, 10, 10);
 
 }
 
 
 void vibrate() {
 // Every 5 seconds, Tribble will move one pixel to the right and back
 counterV = counterV + 1;
  if (counterV%100==2)
   {xpos = xpos + 1;} 
   if (counterV%100==3)
   {xpos = xpos - 1;}
 }
 
}