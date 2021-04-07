package demo;

class Animal{  
Animal(){System.out.println("animal is created");}  
}  
class Dog extends Animal{  
Dog(){  
//super();  automatically added.
System.out.println("dog is created");  
}  
}  
class TestSuper3{  
public static void main(String args[]){  
Dog d=new Dog();  
}}