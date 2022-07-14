//Bridger's Race Track

void setup(){
background(255);
size(500, 300);
}

//Draw Racetrack
void draw(){
background(255);
fill(0);
ellipse(250, 150, 450, 200);
fill(255);
ellipse(250, 150, 300, 100);

//Draw Finish/Start Line
rect(245, 50, 10, 50);
noStroke();
fill(0);
rect(245, 50, 5, 5);
rect(245, 60, 5, 5);
rect(245, 70, 5, 5);
rect(245, 80, 5, 5);
rect(245, 90, 5, 5);
rect(250, 55, 5, 5);
rect(250, 65, 5, 5);
rect(250, 75, 5, 5);
rect(250, 85, 5, 5);
rect(250, 95, 5, 5);

//Draw Car
fill(255, 0 , 0);
rect(mouseX-17, mouseY-5, 27, 6);
ellipse(mouseX-1, mouseY-4, 20, 10);
fill(152,240, 255);
ellipse(mouseX-1, mouseY-4, 18, 8);
fill(255, 0, 0);
rect(mouseX-17,mouseY-5, 27, 6);
triangle(mouseX+10, mouseY-5, mouseX+10, mouseY+1, mouseX+20, mouseY+1);
fill(50);
ellipse(mouseX-7, mouseY+1, 5, 5);
ellipse(mouseX+7, mouseY+1, 5, 5);

}