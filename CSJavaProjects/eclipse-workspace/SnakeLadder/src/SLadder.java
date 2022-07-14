class Game {

	private Board board;
	private Player[] players;
	private Player currentPlayer;
	private int turn;
	
	public Game(Board board, Player[] players) {
		this.board = board;
		this.players = players;
		this.turn = 0;
	}
	public Game(Player[] players) {
		this.board = new Board(10);
		this.players = players;
		this.turn = 0;
	}
	
	public Player currentPlayer() {
		if(turn != players.length) {turn++;}
		else {turn= 0;}
		return this.currentPlayer=players[turn];
	}
	
		
	public void addPlayer(Player p) {
		Player[] temporary = new Player[players.length+1];
		for(int i=0; i < players.length; i++)
			temporary[i]= players[i];
		temporary[temporary.length-1]= p;
		players = temporary;
	}
	
	public boolean winner() {
		if(currentPlayer.getPosition() == board.getCells().length)
			return true;
		else
			return false;
	}
	
	public void movePlayer(int n) {
		currentPlayer.setPosition(currentPlayer.getPosition()+n);
		if(currentPlayer.getPosition() > board.getCells().length)
			currentPlayer.setPosition(0);
	}
	
	public Board getBoard() {return board;}
	
	public boolean play(int moveCount) {
		movePlayer(moveCount);
		if(winner() == true)
			return true;
		else {
			currentPlayer();
			return false; }
	}
	
} 

    
class Player {

	private String name;
	private int position;
	
	public Player(String name) {	
		this.name = name;
		this.position = 1;
	}
	public void setPosition(int position) {
		this.position = position;
	}
	public int getPosition() {return position;}
	public String getName() {return name;}
	public String toString() {return name + "@" + Integer.toString(position);}

} 

    
class Cell {
    
	private int number;
	private boolean occupied;
	private Ladder ladder;
	private Snake snake;
	
	public Cell(int number) {
		this.number = number;
		boolean occupied = false;
		ladder = null;
		snake = null;
	}
	
	public void setOccupied(boolean occupied) { this.occupied = occupied;} 
	public boolean isOccupied() {return occupied;}
	public Ladder getLadder() {return ladder;}
	public Snake getSnake() {return snake;}
	public void setLadder(Ladder ladder) {this.ladder = ladder;}
	public void setSnake(Snake snake) {this.snake = snake;}
	public int getNumber() {return number;}

} 

    
class Board {
    
	private int n;
	private Cell[] cells;
	
	public Board(int n) {
		this.n = n;
		Cell[] cells = new Cell[n*n];
		for(int i=0; i < n; i++) {
				cells[i]= new Cell(i+1);
		}	
	}
	
	public void setCellToLadder(int startPosition, int endPosition) {
		cells[startPosition-1].setLadder(new Ladder(startPosition, endPosition));
	}
	
	public void setCellToSnake(int headPosition, int tailPosition) {
		cells[headPosition-1].setSnake(new Snake(headPosition, tailPosition));
	}
	
	public Cell[] getCells() {return cells;}

} 

    
class Snake {
	
	private int headPosition;
	private int tailPosition;
    
	public Snake(int headPosition, int tailPosition) {
		this.headPosition = tailPosition;
		this.tailPosition = tailPosition;
	}
	public int getTail() {return tailPosition;}
	public String toString() {return Integer.toString(headPosition) + "-" + Integer.toString(tailPosition);}

} 

    
class Ladder {
    
	private int startPosition;
	private int endPosition;
	
	public Ladder(int startPosition, int endPosition) {
		this.startPosition = startPosition;
		this.endPosition = endPosition;
	}
	
	public int getTop() {return endPosition;}
	public String toString() {return Integer.toString(startPosition) + "-" + Integer.toString(endPosition);}
}