import java.util.Scanner;
public class java {
	

static final Scanner in = new Scanner(System.in);

public static void main(String[] args) {
	 
	char [] a = {'a', 'b' , 'c' , 'd' , 'e'};
	char [] b = {'z', 'y'};
	
	translate(a, b);
	
	for(int i = 0; i < b.length; i++)
		System.out.print(b[i]);
	
	
}

public static void translate (char[] a, char[] b) {
	int d;
	
	if(a.length >= b.length) 
		for (int i = 0 ; i < b.length; i++) 
			b[i] = a[i];
	
	else {
		for(int i = 0 ; i < a.length; i++)
			b[i] = a[i];
		for(int i = a.length; i < b.length; i++)
			b[i] = ' ';
	}
		
	
	
	
		
	
	
}


			
}	

	
		


