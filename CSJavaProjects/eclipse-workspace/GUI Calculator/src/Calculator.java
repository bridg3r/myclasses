import javax.swing.*;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class Calculator extends JFrame {
    public static void main(String[] args) {
        
            JFrame Calculator = new JFrame();
            Calculator.setVisible(true);
            Calculator.setSize(300, 300);
            Calculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
           
            JLabel label = new JLabel("Hi");
            
            JButton button = new JButton("Calculate");
            Calculator.add(button);
            
    }
}

