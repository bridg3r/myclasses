import java.util.Scanner;

public class lecture5 {

	public static void main(String[] args) {   
		
		String a = "Enter Weight ";
		double total = 0;
		double max;
		
		double [] weight = new double [5];
		 
		
		
		Scanner s = new Scanner (System.in); 
		 
	
		for(int i = 0; i < weight.length; i++)
		{
			int b = i+1; 
			
		System.out.println(a+b+":");
		weight[i] = s.nextDouble();
		}
	
		System.out.print("You Entered: ");
		
		for(int i=0; i < weight.length; i++)	
			System.out.print(weight[i]+" ");
		
		
		System.out.println();
		System.out.println();
		
		System.out.print("Total weight: ");
		
		max = weight[0];
		for(int i=0; i < weight.length; i++){
		total += weight[i];
		if(max < weight[i])
		     max = weight[i]; 
		
		if( i == weight.length-1) {
			System.out.println(total);
			System.out.println("Average weight: "+ total/weight.length);
			System.out.println("Max weight: "+ max);
		}
	
		}
		 
		
	}
	
}
