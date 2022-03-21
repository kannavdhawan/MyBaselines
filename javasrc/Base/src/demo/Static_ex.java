package demo;


class Static1
{
	int id;
	String name; 
	static int count = 0;
	
	public Static1(int i, String n ) {
		id = i;
		name = n;
		count++;
		
	}
	
	public void display()
	{	
		String strid = Integer.toString(id);
		String strcount = Integer.toString(count);
		System.out.println(strid + name + strcount);
		
	}
	
}
public class Static_ex {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Static1 s1 = new Static1(1,"Ram");
		s1.display();

		Static1 s2 = new Static1(2,"Shyam");
		s2.display();
	}

}