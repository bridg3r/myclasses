public class Bingo {
	
	Player [] players;
	
	
	public Bingo (Player[] players) {
		this.players = players;
	}
	
	String play(int number) {
		String Winners = "";
		for(int d = 0; d < players.length; d++) {
			players[d].markNumber(number);
			if (players[d].isWinner() == true)
				 Winners = Winners + players[d].getName() + " ";	
		}
	 if(Winners.length() > 0)
		 Winners = Winners.substring(0, Winners.length()-1);
	 return Winners;	
	}
	
}

class Player{
	
	String name;
	Card[] Cards;
	
	public Player(String name, Card[] Cards) {
		this.name = name;
		this.Cards = Cards;
	}
	
	public String getName() {
		return name;
	}
	
	
	public Card[] getCards() {
		return Cards;
		
	}
	
	public boolean isWinner() {
		for(int a = 0; a < Cards.length; a++) {
			//Check Rows for all 5 cells marked
			for (int i=0; i<5; i++) {
				 int b = 0;
				 for (int j =0; j< 5 ; j++) {
					 if(Cards[a].isMarked(i, j) == true) {
						 b = b + 1;
						 if(b == 5)
							 return true;
					  }
		          }
			  }
			 //Check Columns for all 5 cells marked
			for (int j=0; j<5; j++) {
				 int b = 0;
				 for (int i =0; i< 5 ; i++) {
					 if(Cards[a].isMarked(i, j) == true) {
						 b = b + 1;
						 if(b == 5)
							 return true;
					  }
		          }
			  }
		 }		
				
		return false;
	}
	
	
	public void markNumber(int number) {
		for(int a = 0; a < Cards.length; a++) 
			Cards[a].markNumber(number);
	}
		
}
	


class Card {

	int [][]numbers;
	
	public Card(int [][] numbers) {
		this.numbers = numbers;
	}	
	
	public int getNumber(int Row, int Column) {
		return numbers [Row][Column];
	}
		
	
	public boolean isMarked(int row, int column) {
		
		if (numbers[row][column] == 200) 
			return true;
		else
			return false;
	}
	
	
	public void markNumber(int number) {
		 for (int i=0; i < 5; i++)
	            for (int j =0; j < 5; j++)
	            	if(numbers[i][j]==number)
	            		numbers[i][j] = 200;
	}
	

}
	

	
	

