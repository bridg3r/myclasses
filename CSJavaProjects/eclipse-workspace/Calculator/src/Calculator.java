import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class Calculator extends JFrame{
	
	class addListener implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			if(F1.getText().equals("") || F2.getText().equals("")) {
				output.setText("ERORR!");
				return;
			}
			String f1 = F1.getText();
			String f2 = F2.getText();
			double n1 = Double.parseDouble(f1);
			double n2 = Double.parseDouble(f2);
			double n3 = n1 + n2;
			String f3 = Double.toString(n3);
			output.setText(f3);
		}
	}
	
	class subtractListener implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			if(F1.getText().equals("") || F2.getText().equals("")) {
				output.setText("ERORR!");
				return;
			}
			String f1 = F1.getText();
			String f2 = F2.getText();
			double n1 = Double.parseDouble(f1);
			double n2 = Double.parseDouble(f2);
			double n3 = n1 - n2;
			String f3 = Double.toString(n3);
			output.setText(f3);
		}
	}
	
	class multiplyListener implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			if(F1.getText().equals("") || F2.getText().equals("")) {
				output.setText("ERORR!");
				return;
			}
			String f1 = F1.getText();
			String f2 = F2.getText();
			double n1 = Double.parseDouble(f1);
			double n2 = Double.parseDouble(f2);
			double n3 = n1 * n2;
			String f3 = Double.toString(n3);
			output.setText(f3);
		}
	}
	
	class divideListener implements ActionListener {
		public void actionPerformed(ActionEvent arg0) {
			if(F1.getText().equals("") || F2.getText().equals("")) {
				output.setText("ERORR!");
				return;
			}
			String f1 = F1.getText();
			String f2 = F2.getText();
			double n1 = Double.parseDouble(f1);
			double n2 = Double.parseDouble(f2);
			double n3 = n1 / n2;
			String f3 = Double.toString(n3);
			output.setText(f3);
		}
	}
	
	class F1copyListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent arg0) {
			F1.setText(output.getText());
		}
	}
	
	class F2copyListener implements ActionListener {

		@Override
		public void actionPerformed(ActionEvent arg0) {
			F2.setText(output.getText());
		}
	}
	
	JLabel output;
	JTextField F1;
	JTextField F2;
	JButton add;
	JButton subtract;
	JButton multiply;
	JButton divide;
	JButton copyF1;
	JButton copyF2;
	
	Calculator(){
		this.setSize(200, 220);
		F1 = new JTextField(10);
		add = new JButton("+");
		subtract = new JButton("-");
		multiply = new JButton("*");
		divide = new JButton("/");
		F2 = new JTextField(10);
		output = new JLabel("");
		copyF1 = new JButton("F1");
		copyF2 = new JButton("F2");
	
		
		add.addActionListener(new addListener());
		subtract.addActionListener(new subtractListener());
		multiply.addActionListener(new multiplyListener());
		divide.addActionListener(new divideListener());
		copyF1.addActionListener(new F1copyListener());
		copyF2.addActionListener(new F2copyListener());
		
		FlowLayout layout = new FlowLayout();
		this.setLayout(layout);
		
		this.add(F1);
		this.add(F2);
		this.add(add);
		this.add(subtract);
		this.add(multiply);
		this.add(divide);
		this.add(copyF1);
		this.add(copyF2);
		this.add(output);
		this.setVisible(true);
		this.setTitle("Bridger's Calculator");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
	}
	
	 public static void main(String[] args) {
		 new Calculator();
	 }
}

