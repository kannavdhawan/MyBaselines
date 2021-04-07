package demo;

public class Construct {
	
	int id;
	String EName;
	
	public Construct(int i, String n) {
		id = i;
		EName = n;
		
	}
	
	public String display() {
		String strid = Integer.toString(id);
		return strid + " " + EName;
		
	}
		
	public static void main(String args[]) {
		
		Construct c1 = new Construct(1,"Kannav");
		System.out.println(c1.display());
		
		
	}
}
