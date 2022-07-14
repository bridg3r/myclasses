import java.util.Scanner;

public class tets {

	public static void main(String[] args) {
			
		Scanner s = new Scanner (System.in);
		
		String palabra = s.next();
		
		String [] word = palabra.split("");
		
		for(int i = 0 ; i < word.length; i++) {
			for (int j = i+1; j < word.length; j++) {
				if (word[i].equals(word[j])) {
					return;
				}
			}
			if(i == word.length-1)
				System.out.print(palabra);
				
		}
				
	
}
}