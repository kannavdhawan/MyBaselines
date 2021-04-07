package demo;

import java.util.ArrayList;
import java.util.List;

public class String_reverse {
	
	public String reverse(String name) {
		
		if (name.length() <=1) {
			return name;
		}
		else
		{
			return name.charAt(name.length()-1) + reverse(name.substring(0, name.length()-1));
			
		}
		
	}
	
	public static void list1()
	{
		List<String> names = new ArrayList<>();
		names.add("kannav");
		names.add("Dhawan");
		System.out.println("Names" + names);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String_reverse s1 = new String_reverse();
		System.out.println(s1.reverse("Hello World"));
		s1.list1();
	}

}