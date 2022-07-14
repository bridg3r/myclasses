import java.util.Scanner;


public class Boolean {

	 public static void main(String[] args) {    
		 Scanner s = new Scanner (System.in); 
		 int x;
		 int y;
		 int z;
		 boolean a;
		 
		 
		x = s.nextInt();
		y = s.nextInt();
		z = s.nextInt();
		
		if (x > y && y > z)
			 a = true;
		
		else {
		
		if (x < y && y < z)
			 a = true;
			 
		else 
			a = false;
		
		}
	     
	System.out.print(a);
	
}
}
