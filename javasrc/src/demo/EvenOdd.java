package demo;
import java.util.Scanner;

public class EvenOdd {

	
public static void main(String args[]){
        
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number");
        
        int num = scan.nextInt();
        
        Eo n = new Eo();
        n.findEvenOdd(num);
        
        
    }
}
