package demo;

public class Sol4 {
	
	public String oddeven(int x) {
		
		
		
		int[] array_a = new int[String.valueOf(x).length()];
		int i = 0;
		while(x != 0){
			array_a[i] = x % 10;
			x = x/10;
			i++;
		}
		int odd_c = 0;
		int even_c = 0;
		
		for(int j: array_a) {
			if(j%2 == 0) {
				even_c++;
			}
			else
			{
				odd_c++;
				
			}
		}
		
		if(even_c == odd_c) {
			
			return "True";
		}
		else {
			return "False";
		}
		
	}
	
public static void main(String args[]) {
	
int x = 10000;

Sol4 s1 = new Sol4();
System.out.println(s1.oddeven(x));
}
}

