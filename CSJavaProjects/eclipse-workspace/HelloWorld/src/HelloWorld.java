import java.util.Scanner;

public class HelloWorld {

	public static void main(String[] args) {
		
		Scanner s = new Scanner (System.in); 
		double N;
		int Count = 0;
		
		N = s.nextDouble();
		
		if(N <= 0 )
			System.out.print("Illegal Input");
		
	
			
		while (N >= 1) {
			N = N/2d;
			Count = Count + 1;
			
		}
		
		if (Count >= 0 && N > 0)
		System.out.print(Count);
		
	}

}
