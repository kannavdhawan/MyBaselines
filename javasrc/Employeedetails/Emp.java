package Employeedetails;

public class Emp {
	int id;
	String name;
	Address address;
	public Emp(int id, String name, Address address) {
		this.id = id;
		this.name = name;
		this.address = address;
	}
	
	void display() {
		System.out.println(this.id + this.name + this.address.streetname + this.address.streetno);
	}
	
	public static void main(String[] args) {
		Address a1 = new Address(1,"Lester");
		Address a2 = new Address(2,"Erb");
		
		Emp e1 = new Emp(11,"Kannav",a1);
		Emp e2 = new Emp(12,"Kannav Dhawan",a2);
		e1.display();
		e2.display();
		
	}

}
