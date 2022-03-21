package demo;

 class Address{
	int aptno;
	String city;
	String country;
	
	public Address(int aptno,String city,String country)
	{
		this.aptno = aptno;
		this.city = city;
		this.country = country;	
	}
}
 
 
public class Employee {
	
	String name;
	int age;
	int salary;
	Address address;
	public Employee(String name, int age, int salary, Address address) {
		this.name = name;
		this.age = age;
		this.salary = salary;
		this.address = address;
		
	}
	
	public void display() {
		System.out.println(name + " " + age + " " + salary);
		System.out.println(address.city + address.country );
	}
	
	public static void main(String args[]) {
		
		Address A1 = new Address(181,"Waterloo", "Canada");
		Address A2 = new Address(161, "Delhi","India");
		
		Employee E1 = new Employee("Kannav", 23, 75000, A1);
		Employee E2 = new Employee("Dhawan", 23, 7500000, A2);
		
		E1.display();
		E2.display();
		
	}

}
