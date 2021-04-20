package Math_funcs;

public class rec_fact {
	
	static int fact(int n) {
		
		if(n ==1) {
			return 1;
		}
		else
		{
			return (n * fact(n-1));
		}
	}

	public static void main(String[] args) {
		
		System.out.println("Factorial is: " + fact(5));
	}
}
