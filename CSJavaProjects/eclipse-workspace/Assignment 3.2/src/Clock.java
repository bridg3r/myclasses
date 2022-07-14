
class Clock{
	
	int hours;
	int minutes;
						

	public Clock() {
	hours = 0;
	minutes = 0;
	}
	
	public Clock(int h) {
		hours = h;
		minutes = 0;
	}
						

	public Clock(int h, int m) {
	hours = h;
	minutes = m;
	}
	
	
	public int getHour() {
		return hours;
	}

	public int getMinute() {
		return minutes;
	}

	public void incrementTimer() {
		minutes = minutes + 1;
		if(minutes > 59) {
			minutes = 0;
			hours = hours + 1;
			if(hours > 23)
				hours = 0;
		}
	}
	
	public void incrementTimer(int x) {
		minutes = minutes + x;
		if(minutes > 59 ) {
			hours = hours + 1;
			int y = minutes%60;
			minutes = y;
			if(hours > 23)
				hours = 0;
		}
		
	}
	
	
	public void setTime(int h, int m) {
		if (h > 23 || m > 59)
			System.out.println("Invalid Input");
		else {
			hours = h;
			minutes = m;
		}
	}
	
	public String toString() {
		
		
		switch(hours) {
		case 0 :
			if(minutes < 10 )
				return  "12:0" + minutes + " AM";
			else 
				return "12:" + minutes + " AM";
		case 1 : case 2: case 3: case 4: case 5: case 6: case 7: case 8: case 9:
			if(minutes < 10 )
				return "0"+ hours + ":0" + minutes + " AM";
			else
				return "0" + hours + ":" + minutes + " AM";
		
		case 10: case 11:
			if(minutes < 10 )
				return hours + ":0" + minutes + " AM";
			else
				return hours + ":" + minutes + " AM";
		case 12:
			if(minutes < 10 )
				return hours + ":0" + minutes + " PM";
			else
				return hours + ":" + minutes + " PM";
		case 13: case 14: case 15: case 16: case 17: case 18: case 19: case 20: case 21:
			int h = hours - 12;
			if (minutes < 10)
				return "0" + h + ":0" + minutes + " PM";
			else
				return "0" + h + ":" + minutes + " PM";
		case 22: case 23:
			int H = hours - 12;
			if (minutes < 10)
				return H + ":0" + minutes + " PM";
			else
				return H + ":" + minutes + " PM";
		}
	
		return "ERROR";
				
		
	}
			
	

}

