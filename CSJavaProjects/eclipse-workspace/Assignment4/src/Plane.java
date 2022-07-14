class Point {
	
	private double x;
	private double y;
	
     public Point(double x, double y) {
    	 this.x = x;
    	 this.y = y;
     }
     
     public double getDistance(Point point) {
    	double a =  Math.abs(point.x - this.x);
    	double b = Math.abs(point.y - this.y);
    	double c = Math.sqrt(a*a + b*b );
    	return c;
     }
     
     public double getX() {return x;}
     public double getY() {return y;}
     
}

abstract class Shape {
	
     public abstract double getArea();
     public abstract double getPerimeter();
 
}

interface Symmetric {
	Point getPointOfSymmetry();
}

class Triangle extends Shape {
	
	private Point firstPoint;
	private Point secondPoint;
	private Point thirdPoint;
	
	public Triangle(Point firstPoint, Point secondPoint, Point thirdPoint) {
		this.firstPoint = firstPoint;
		this.secondPoint = secondPoint;
		this.thirdPoint = thirdPoint;
	
	}


	public double getArea(){
		double a = firstPoint.getDistance(secondPoint);
		double b = firstPoint.getDistance(thirdPoint);
		double c = thirdPoint.getDistance(secondPoint);
		double h = (a+b+c)/2;
		double A = Math.sqrt(h*(h-a)*(h-b)*(h-c));
		return A;
	}
	
	public double getPerimeter(){
		double a = firstPoint.getDistance(secondPoint);
		double b = firstPoint.getDistance(thirdPoint);
		double c = thirdPoint.getDistance(secondPoint);
		double P = a + b + c;
		return P;
	}
	
	public Point getFirstPoint() {return firstPoint;}
	public Point getSecondPoint() {return secondPoint;}
	public Point getThirdPoint() {return thirdPoint;}
	
}

class Rectangle extends Shape {
	
	private Point topLeftPoint;
	private double length;
	private double width;
	
	
	public Rectangle(Point topLeftPoint, double length, double width) {
		this.topLeftPoint = topLeftPoint;
		this.length = length;
		this.width = width;
	}
	
	public double getArea(){
		return length * width;
	}
	
	public double getPerimeter() {
		return width*2 + length*2;
	}
	
	public Point getTopLeftPoint() {return topLeftPoint;}
	public double getLength() {return length;}
	public double getWidth() {return width;}
}

class Trapezoid extends Shape {
	
	private Point topLeftPoint;
	private Point bottomLeftPoint;
	private double topSide;
	private double bottomSide;
	
	public Trapezoid(Point topLeftPoint, Point bottomLeftPoint, double topSide, double bottomSide) {
		this.topLeftPoint = topLeftPoint;
		this.bottomLeftPoint = bottomLeftPoint;
		this.topSide = topSide;
		this.bottomSide = bottomSide;
	}
	
	public double getArea(){
		//double h = Math.abs(topLeftPoint.y-bottomLeftPoint.y);
		double h = Math.abs(topLeftPoint.getY()-bottomLeftPoint.getY());
		double A = (topSide+bottomSide)/2 * h;
		return A;
	}
	
	public double getPerimeter(){
		//double a = Math.abs(topLeftPoint.x-bottomLeftPoint.x);
		//double b = Math.abs(topLeftPoint.y-bottomLeftPoint.y);
		//double c = Math.sqrt(a*a + b*b);
		//double d = Math.abs((bottomLeftPoint.x+bottomSide)-(bottomLeftPoint.x+topSide));
		//double e = Math.sqrt(d*d + b*b);
		double A = topLeftPoint.getDistance(bottomLeftPoint);
		double B = new Point(topLeftPoint.getX()+topSide, topLeftPoint.getY()).getDistance(new Point(bottomLeftPoint.getX()+bottomSide, bottomLeftPoint.getY()));
		double P = topSide + bottomSide + A + B;
		return P;
	}
	
	public Point getTopLeftPoint() {return topLeftPoint;}
	public Point getBottomLeftPoint() {return bottomLeftPoint;}
	public double getTopSide()  {return topSide;}
	public double getBottomSide() {return bottomSide;}
}

 class Circle extends Shape implements Symmetric {
	 
	private Point center;
	private double radius;
	 
     public Circle(Point center, double radius) {
    	 this.center = center;
    	 this.radius = radius;
     }
     
     public Point getPointOfSymmetry() {return center;}
     public double getArea() {return Math.PI * radius * radius;}
     public double getPerimeter() {return Math.PI * 2 * radius;}
     public Point getCenter() {return center;}
     public double getRadius() {return radius;}
}
 
class EquilateralTriangle extends Triangle implements Symmetric {
	
	private Point topPoint;
	private double side;
	
	public EquilateralTriangle(Point topPoint, double side) {
		super(topPoint, new Point(topPoint.getX()-side/2, topPoint.getY()-(side* Math.sqrt(3)/2)), 
				new Point(topPoint.getX()+side/2, topPoint.getY()-(side* Math.sqrt(3)/2)));
		this.side = side;
		this.topPoint = topPoint;
		
	}
	
	public Point getPointOfSymmetry() {
		double h = side * Math.sqrt(3)/2;
		Point symmetry = new Point(topPoint.getX(), topPoint.getY()-(h*2/3));
		return symmetry;
	}
	
	public double getArea() {return side * side * Math.sqrt(3)/4;}
	public double getPerimeter() {return side + side + side;}
	public Point getTopPoint() {return topPoint;}
	public double getSide() {return side;}	
}

class Square extends Rectangle implements Symmetric {
	
	private Point topLeft;
	private double side;
	
	public Square(Point topLeft, double side) {
		super(topLeft, side, side);
		this.topLeft = topLeft;
		this.side = side;
	}
	
	public Point getPointOfSymmetry() {
		Point symmetry = new Point(topLeft.getX() + side/2, topLeft.getY()-side/2);
		return symmetry;
	}
	
	public double getSide() {return side;}
}

public class Plane {
	
	private Shape [] shapes;
	
	public Plane() {
		this.shapes = new Shape [0];

	}
	
	public Shape[] getShape() {
		return shapes;
	}
	
	public void addShape(Shape shape) {
		Shape [] temporary = new Shape [shapes.length+1];

		for (int i = 0; i < shapes.length; i++){
			 temporary[i] = shapes[i];
		}
		temporary[temporary.length-1] = shape;
		shapes = temporary;
			
	}
	
	public double getSumOfAreas() {
		double totalArea = 0;
		for(int i = 0; i < shapes.length; i++) {
			totalArea += shapes[i].getArea();
		}
		return totalArea;	
	}
		
	public double getSumOfPerimeters() {
		double totalPerimeter = 0;
		for(int i = 0; i < shapes.length; i++) {
			totalPerimeter += shapes[i].getPerimeter();
		}
		return totalPerimeter;
	}
	public Point getCenterOfPointOfSymmetries() {
		double X = 0;
		double Y = 0;
		int count = 0;
		
		for(int i = 0; i < shapes.length; i++) {
			if (shapes[i] instanceof Symmetric){
				X += ((Symmetric) shapes[i]).getPointOfSymmetry().getX();
				Y += ((Symmetric) shapes[i]).getPointOfSymmetry().getY();
				count++;
			}
		}
		
		if(count == 0)
			return null;
		else {
			double X1 = X/count;
			double Y1 = Y/count;
			return new Point(X1, Y1); }
			
	}
}
