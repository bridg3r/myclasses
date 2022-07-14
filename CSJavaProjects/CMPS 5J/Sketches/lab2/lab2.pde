//Bridger's Zoog that follows the mouse and grows in size the fast the mouse moves

void setup(){
background(255);
size(300, 300);
}

void draw(){
  background (255);
float mouseSpeedX = abs(mouseX-pmouseX);
float mouseSpeedY = abs(mouseY-pmouseY);

//Draw Zoog Body
rect(mouseX-10, mouseY, mouseSpeedX+20, mouseSpeedY+75);

//Draw Zoog Head
fill(255);
ellipse(mouseX, mouseY, mouseSpeedX+50, mouseSpeedY+50);

//Draw Zoog's Eyes
fill(0);
ellipse(mouseX+10, mouseY, 16+mouseSpeedX, 32+mouseSpeedY);
ellipse(mouseX-10,mouseY, 16+mouseSpeedX, 32+mouseSpeedY);

// Draw Zoog's legs
stroke(0);
strokeWeight(mouseSpeedX);
strokeWeight(mouseSpeedY);
line(mouseX+10,mouseY+75,mouseSpeedX+mouseX+25,mouseSpeedY+mouseY+90);
line(mouseX-10, mouseY+75,mouseX-25-mouseSpeedX,mouseSpeedY+mouseY+90);


}