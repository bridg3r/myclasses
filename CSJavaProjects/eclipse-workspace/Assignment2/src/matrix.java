import java.util.Scanner;

public class matrix {


	public static void main(String[] args) {
		Scanner s = new Scanner (System.in);
		
		int m = s.nextInt();
		int n = s.nextInt();
		
		int[][] matrix = new int [m][n];
		
	
		for(int j = 0; j < matrix.length; j++)
			for(int i =0; i < matrix[n].length; i++)
				matrix[m][n] = s.nextInt();
		
}
}