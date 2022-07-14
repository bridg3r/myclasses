import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.*;


public class Calc extends JFrame {

	Calc(){
		  JFrame Calculator = new JFrame();
          Calculator.setVisible(true);
          Calculator.setSize(200, 175);
          Calculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         
          FlowLayout layout = new FlowLayout();
          Calculator.setLayout(layout);
          
          JTextField F1 = new JTextField(10);
          Calculator.add(F1);
          
          JButton add = new JButton("+");
          ClickListener addition = new ClickListener();
	        Calculator.add(add);
	        add.addActionListener(addition);
	        
	        JButton subtract = new JButton("-");
	        Calculator.add(subtract);
	        JButton multiply = new JButton("*");
	        Calculator.add(multiply);
	        JButton divide = new JButton("/");
	        Calculator.add(divide);
          
          JTextField F2 = new JTextField(10);
          Calculator.add(F2);
          
          JLabel space = new JLabel("");
          Calculator.add(space);
          JLabel output = new JLabel("output");
          Calculator.add(output);
	}
	
	    public static void main(String[] args) {
	    	new Calc();
      
	    }
	    class ClickListener implements ActionListener{

			public void actionPerformed(ActionEvent arg0) {
				JOptionPane.showMessageDialog(null, "output");
			}
	    	
	    }
	}
