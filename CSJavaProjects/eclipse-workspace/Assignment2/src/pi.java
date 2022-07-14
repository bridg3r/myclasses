import java.util.Scanner;

public class pi {

	public static void main(String[] args) {
	
		Scanner s = new Scanner (System.in); 
		
		int N = s.nextInt();
		
		double o = 0;
		for(int i=0; i < N; i++) {
			int d = 1 + 2*i;
			
			if(i==0)
				o = o + ((double)4/d);
			else
			{
				if(i==1)
					o = o - ((double)4/d);
				else
				{
					if(i%2 == 0)
						o = o + ((double)4/d);
					else
						o = o - ((double)4/d);
				}
				
				
			}
			
			
				
			
		}
		System.out.printf("%.2f", o);
			
	}

}
