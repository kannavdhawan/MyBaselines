package demo;

public class Sol3 {
public static void main(String args[]) {
	String String_a = "abcabce";
	String x;
	int length_a ;
	
	length_a = String_a.length();
	
	char[] al = new char[100];

	
	for(int i = 0; i <String_a.length(); i++) {
		char y;
		y = String_a.charAt(i);
		al[i] = y;
		
	}
	
	for(char i: al) {
		System.out.println(i);
	}
	
	
}
}




