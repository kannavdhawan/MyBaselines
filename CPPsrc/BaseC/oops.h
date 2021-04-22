#include<iostream>
#include<string>
using namespace std;
// Inheritance

class Base1_sal{
  protected :
  int salary;
  int bonus;

};

class Base2_details{
  protected :
  string fname;
  string lname;

};

class Driver: public Base1_sal, public Base2_details{
  
  public : 
  void setter(int s,int b,string fn,string ln){
    salary = s;
    bonus = b;
    fname = fn;
    lname = ln;

  }

  void getter(){
    cout<<endl;
    cout<<salary<<bonus<< fname<< lname;

  }

};
