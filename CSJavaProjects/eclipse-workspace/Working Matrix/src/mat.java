
import java.util.Scanner;

public class mat {
	


	public static void main(String[] args) {
	
		Scanner s = new Scanner (System.in); 
		
		int m = s.nextInt();
		int n = s.nextInt();
		
		int[][] matrix = new int [m][n]; 
		
		
		for(int j = 0; j < m; j++)
			for(int i =0; i < n; i++) 
				matrix [j][i] = s.nextInt();

		/*for(int j = 0; j < m; j++) {
			for(int i =0; i < n; i++) 
				System.out.print(matrix [j][i]+ " ");
		System.out.println();	
		}*/

		String command = s.next();		
		
		while(!command.equals("Q")) {			

			if(command.equals("T")) {
				for(int j = 0; j < n; j++) {
					for(int i = 0; i < m; i++)
						if(i == m-1)
							System.out.print(matrix[i][j]);
						else
						System.out.print(matrix[i][j]+" ");
				System.out.println();}
				}
			else {
				int x = 1;
				if(command.equals("R")) {
					for(int j = 0; j < m; j++) {
						for(int i =0; i < n; i++) 
							x = x * matrix[j][i];
					if(j == m-1)
						System.out.print(x);
					else
						System.out.print(x+" ");
					x = 1;}
					System.out.println();
					}
			
				else {
					if(command.equals("C")) {
						for(int j = 0; j < n; j++) {
							int y = matrix[0][j];
							for(int i = 0; i < m; i++)
								if(matrix[i][j] < y)
									y = matrix[i][j];
						if(j == n-1)
							System.out.print(y);
						else
							System.out.print(y+ " ");
						
						y = 1;
						}
						System.out.println();
						}
					}
		
			}

			command = s.next();
			}	
		
		
}
}
		
			
	


