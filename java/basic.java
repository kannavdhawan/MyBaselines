// import javax.print.event.PrintJobListener;

// class Simple
// {
// public static void main(String args[])
// {
//   System.out.print("Hello World");
// }

// }

// class Narrow_wide
// {
// public static void main(String args[])
// {
// int a = 10;
// float f = a;
// float x =  10.4f;
// int xint = (int)x;
// System.out.println(a);
// System.out.println(f);
// System.out.println(xint);

// }

// }

// class Ifelse
// {
//   public static void main(String args[])
//   {
//     int a = 18;
//     if(a>18)
//     {
//     System.out.println("a>18");

//     }
//     else{

//       System.out.println("a<18");
//     }

//   }
// }

// class Leapyear
// {
//   public static void main(String args[])
//   {
//     int year = 2020;

//     if(((year%4 == 0) && (year%100 != 0)) || (year%400 == 0) )
//     {
//       System.out.println(true);
//     }
//   }
// }

// // if(){} else if(){} else if() {} else {}
// // if no break after a case, it will execute all the statements after the match is found including default
// class Scase{
//   public static void main(String args[])
//   {
// int n = 2;
// switch(n){

// case 1: System.out.println("1");
// break;

// case 2: System.out.println("2");
// break;

// case 3: System.out.println("3");
// break;

// default: System.out.println("Not Found");

// }

//   }
// }

// class Loops{
// public static void main(String[] args)
// {

// for(int i = 0; i <10 ; i++)
// {

// System.out.println(i);

// }
// }

// }





// class PyramidExample {  
// public static void main(String[] args) {  
// for(int i=1;i<=5;i++){  
// for(int j=1;j<=i;j++){  
//         System.out.print("* ");  
// }  
// System.out.println();//new line  
// }  
// }  
// }  



// class Main {  
// public static void main(String[] args) {  
//     int arr[] = {1,2,3,4};
    
//     for(int i: arr){
        
//         System.out.println(i);
//     }
    
    
// }
// }



// //A Java program to demonstrate the use of labeled for loop  
// class LabeledForExample {  
// public static void main(String[] args) {  
//     //Using Label for outer and for loop  
//     aa:  
//         for(int i=1;i<=3;i++){  
//             bb:  
//                 for(int j=1;j<=3;j++){  
//                     if(i==2&&j==2){  
//                         break aa;  
//                     }  
//                     System.out.println(i+" "+j);  
//                 }  
//         }  
// }  
// }

// class Main
// {
// public static void main(String args[]){
//   int i = 1;
//   while(i < 5){
//       System.out.println(i);
//       i++;
//   }
// }
// }

// class Dowhile 
// {
// public static void main(String args[]){
//   int i =0;
// do 
// {
// System.out.println("do");
// i++;
// } while(i <10);
// }
// }

// public class Fib{
// int a = 10;
// static int fib(int a)
// {

// if(a == 1 || a == 0){

// return a;
// }

// else{
//   return fib(a-1) + fib(a-2);
// }
// }

// public static void main(String args[])
// {

// System.out.println(fib(a));

// }

// }




// class Sample
// {
//     int i;
//     String s;
//   public static void main(String args[])
//   {
//     Sample s1 = new Sample();

//     System.out.println(s1.i);
//     System.out.println(s1.s);
//   }
// }


// class Student{  
//  int id;  
//  String name;  
// }  
// //Creating another class TestStudent1 which contains the main method  
// class TestStudent1{  
//  public static void main(String args[]){  
//   Student s1=new Student();  
//   System.out.println(s1.id);  
//   System.out.println(s1.name);  
//  }  
// }


// class Student{  
//  int id;  
//  String name;  
// }  
// class TestStudent2{  
//  public static void main(String args[]){  
//   Student s1=new Student();  
//   s1.id=101;  
//   s1.name="Sonoo";  
//   System.out.println(s1.id+" "+s1.name);//printing members with a white space  
//  }  
// }  



// // Initialization of object through - reference, Method, Constructor



// // By Method 


// class Employee{

// int id;
// String name;
// Float salary;

// void insert(int i, String n, Float f){
// id = i;
// name = n;
// salary = f;
// }

// void display(){System.out.println(id + "" + name + "" + salary);}
// }

// public class Test{
// public static void main(String args[]){

// Employee e1 = new Employee();
// // e1.id = 1; //by reference

// e1.insert(1,"Kannav",75000.0f);
// e1.display();

// }
// }



// class Demo   
// {  
// public static void main(String[] args)   
// {  
// // using the max() method of Math class  
// System.out.print("The maximum number is: " + Math.max(9,7));  
// }  
// }  




