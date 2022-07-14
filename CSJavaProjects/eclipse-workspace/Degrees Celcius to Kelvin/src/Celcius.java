import java.util.Scanner;

public class Celcius {

	
	public static void main(String[] args) {
		
		
		Scanner s = new Scanner (System.in); 
		float z = 0;
		String K = "k";
		String F = "f";
		String type; 
		boolean a;
		
		type = s.next();
		
			
		if (type.equalsIgnoreCase(K)) 
		{
		
		z = s.nextFloat(); 
		z = z - (float) 273.15; 
		System.out.printf("%.2f", z);
		
		}
		
		
		if (type.equalsIgnoreCase(F))
		{
		
			z = s.nextFloat(); 
			z = (z - 32) * (float) 5/9; 
			System.out.printf("%.2f", z);
	
		}
		
	
		
		
	}
	}
