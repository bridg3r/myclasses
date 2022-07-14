
public class ClockTest {

	public static void main(String[] args) {
		Clock c1 = new Clock ();
		
		for(int i = 1; i < 1441;i++){
			c1.incrementTimer(1);
			System.out.print(i+ " ");
			System.out.println(c1.toString());
		}
			
	}
} 
