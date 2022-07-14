int circleX = 0;
int circleY = 0;
void setup() {
 size(500, 500);
}
void draw() {
 background(255);
 stroke(0);
 fill(175);
 ellipse(250, 250, circleX, circleY);
 circleX = circleX + 1;
 circleY = circleY + 1;
}