import java.util.Scanner;

public class string {

	public static void main(String[] args) {
		
		Scanner s = new Scanner (System.in);
		
		int n = s.nextInt();
		
		int count = 0;
		String words[] = new String [n];
		
		for(int i =0; i < n; i++) 
			words [i] = s.next();
		
		
		for(int a = 0 ; a < words.length; a++) {
		String [] word = words[a].split("");
		int kill = 0;
		
			for(int i = 0 ; i < word.length; i++) {
				for (int j = i+1; j < word.length; j++) 
					if (word[i].equals(word[j])) 
						kill++;
					
				if(i == word.length-1 && kill == 0) {
					if(a == words.length-1) {
						count++;
						System.out.print(words[a]); }
					else {
						count++;
						System.out.print(words[a]+ " "); }
					
				}
				
				
			}
		}

	if (count == 0)
		System.out.print("NONE");
}
}
