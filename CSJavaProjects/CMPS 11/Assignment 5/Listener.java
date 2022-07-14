import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;

public class Listener extends JFrame {
	
	class ButtonListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent arg0) {
			String f1 = F1.getText();
			char [] reverse = new char[f1.length()];
			int j = reverse.length-1;
			for(int i = 0; i < reverse.length; i++) {
				reverse[i] = f1.charAt(j);
				j--;
			}
			String f2 = new String(reverse);
			F2.setText(f2);
		}
	}
	
	JButton reverse;
	JTextField F1;
	JTextField F2;
	
	Listener(){
		
		
		F1 = new JTextField(10);
		reverse = new JButton("reverse");
		F2 = new JTextField(10);
		
		reverse.addActionListener(new ButtonListener());
		F1.addActionListener(new ButtonListener());
		
		this.add(F1);
		this.add(reverse);
		this.add(F2);
		
		FlowLayout layout = new FlowLayout();
		this.setLayout(layout);
		this.setSize(200, 200);
		this.setVisible(true);
		this.setTitle("Bridger's Listener");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public static void main(String[] args) {
		 new Listener();
	 }
	
}
