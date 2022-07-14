import java.util.Scanner;

public class jersey {

	public static void main(String[] args) {
		
		int[][] players = new int [5][3]; 
		
		Scanner s = new Scanner (System.in); 
		
		for(int j = 0; j < players.length; j++)
		{
			int a = j + 1;
			System.out.println("Enter player "+a+"'s jersey number:");
			
			for(int i =0; i < players[i].length; i++)
			{
				if(i==0)
					players[j][i] = a;
				else 
					{
				players [j][i] = s.nextInt();
					if(i==1)
						System.out.println("Enter player "+a+"'s rating:");
					else
						System.out.println();
					}
			}
		}
		
		System.out.println("ROSTER");
		
		for(int j = 0; j < players.length; j++)
		{
			
			
			for(int i =0; i < players[i].length; i++)
			{
				if(i==0)
				System.out.print("Player "+ players[j][i]+ " -- Jersey number: " );
				else
					if(i==1)
					System.out.print(players[j][i]+ ", Rating: ");
					else
					System.out.println(players[j][i]);
			}
			
		}
		
		System.out.println();
		System.out.println("MENU");
		System.out.println("u - Update player rating");
		System.out.println("a - Output players above a rating");
		System.out.println("r - Replace player");
		System.out.println("o - Output roster");
		System.out.println("q - Quit");
		System.out.println();
		System.out.println("Choose an option:");
		
		String input= s.next();
		
		if (input.equalsIgnoreCase("o"))
		{
			System.out.println("ROSTER");
			
			for(int j = 0; j < players.length; j++)
			{
				
				
				for(int i =0; i < players[i].length; i++)
				{
					if(i==0)
					System.out.print("Player "+ players[j][i]+ " -- Jersey number: " );
					else
						if(i==1)
						System.out.print(players[j][i]+ ", Rating: ");
						else
						System.out.println(players[j][i]);
				}
				
			}
		 }
			
		else{
		
				if(input.equalsIgnoreCase("u"))
				{
					int k = s.nextInt()-1;
					players[k][2] = s.nextInt();
					
					String input2= s.next();
					
					if (input2.equalsIgnoreCase("o"))
					{
						System.out.println("ROSTER");
						
						for(int j = 0; j < players.length; j++)
						{
							
							
							for(int i =0; i < players[i].length; i++)
							{
								if(i==0)
								System.out.print("Player "+ players[j][i]+ " -- Jersey number: " );
								else
									if(i==1)
									System.out.print(players[j][i]+ ", Rating: ");
									else
									System.out.println(players[j][i]);
							}
							
						}
					 }
					
				}
		}
			
}
}
