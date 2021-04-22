#include <iostream>
#include "funcs.h"
#include "oops.h"

#include <cmath>

using namespace std;

int main() {
  string fname = "kannav ";
  string lname = "Dhawan";

  string fullname = fname.append(lname);

  cout<<"Full Name is: "<< fullname<<endl;
  cout<<"Size full name is: "<<fullname.length()-1; 
  cout<<endl;
  math_test();

  cout<<endl;
     
  elseif(20);

  cout<<endl;
  loops();

  cout<<endl;
  arrays();
  cout<<endl;
  references();
  cout<<endl;
  pointers();
  
  cout<<endl;

  functions("kannav");
  cout<<endl;
  cout<<"default"<<endl;
  functions1();

  Car sedan;
  Car suv;

  sedan.brand = "BMW";
  sedan.model = "Series 3";
  sedan.year = 2021;

  suv.brand = "BMW";
  suv.model = "X5";
  suv.year = 2021;

  cout<<endl<<suv.brand<<endl;
  cout<<sedan.brand<<endl;

  sedan.getter();
  // cout<<"test";
  cout<<sedan.brand;
  // cout<<"test";
  Outsideclassmethod_classname ob;
  ob.out();


  Car_2 ob1;
  int s1;
  s1 = ob1.speed(100);

  cout<<s1;

  Construct_ex ob3("Kannav",10000000);
  
  encap e1;
  e1.set_salary(1000000);
  // cout<<"test";
  int y = e1.get_salary();
  // cout<<"test";
  cout<<y;

  

  // inheritance multiple

  Driver d1;
  d1.setter(100000, 10000, "Kannav", "Dhawan");
  d1.getter();

  return 0;
}