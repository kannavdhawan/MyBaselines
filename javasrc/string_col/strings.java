package string_col;

public class strings {
	public static void main(String[] args) {
		// creating a string s1
		
		String s1 = "kannav";
		
		
		// creating string using new keyword
		
		String s2 = new String("kannav");
		
		// Character to string 
		
		char[] ch  = {'a','b','c'};
		String s3 = new String(ch);
		
		System.out.println(s1);
		System.out.println(s2);
		System.out.println(s3);
		
		
		s1.concat(" Dhawan");
		System.out.println(s1);
		
		s1 = s1.concat(" Dhawan");
		System.out.println("ref concat " +  s1);
		
		
		
		System.out.println(s1.equals(s3));
		System.out.println(s1.equals("kannav Dhawan"));
		
		System.out.println("Equals Ignore case " + s1.equalsIgnoreCase("kannav dhawan"));
		
		
		System.out.println(s1==s2);//false(because s3 refers to instance created in nonpool)
		
		System.out.println(s3.compareTo(s1));
		
		
		String s="Kannav"+" Dhawan";
		System.out.println(s);
		
		s = s.concat(s);
		System.out.println(s);
		
		
		System.out.println(s.substring(0,7));//he  

		System.out.println(s.toLowerCase());//sachin  

		System.out.println(s.toUpperCase());//sachin  
		
		System.out.println(s.trim());
		
		System.out.println(s.startsWith("K"));
		System.out.println(s.charAt(0));//S  
		System.out.println(s.length());//6  
		String replaceString=s.replace("K","kk");
		System.out.println(replaceString);

	}
}
