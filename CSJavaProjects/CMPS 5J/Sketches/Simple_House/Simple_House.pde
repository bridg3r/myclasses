//This is a simple house created by Bridger Hackworth

size(400, 300);
background(255);

//house base
fill(173,224,255);
rect(100, 120, 200, 180);

//roof
fill(250, 209, 241);
triangle(80, 120, 320, 120, 200, 70);

//door
fill(255);
rect(180, 225, 40, 75 );
rect(186, 230, 10, 30);
rect(203, 230, 10, 30);
rect(203, 265, 10, 30);
rect(186, 265, 10, 30);
fill(255, 198, 41);
ellipse(216, 270, 7, 7);

//left bottom window
fill(244,252, 235);
rect(110, 225, 60, 34);

fill(255);
rect(140, 225, 2, 34);
rect(110, 241, 60, 2);


//right bottom window
fill(244, 252, 235);
rect(230, 225, 60, 34);
fill(255);
rect(259, 225, 2, 34);
rect(230, 241, 60, 2);

//top window
fill(244, 252, 235);
ellipse(200, 170, 100, 50);
fill(255);
rect(150, 169, 100, 2);
rect(199, 145, 2, 50);

 