//  W3, geeks, tuts



#include <cmath>
using namespace std;

void math_test()
{
std:: cout<< sqrt(64);
cout<<endl;

std:: cout<< round(2.6);
cout<<endl;

std:: cout<< fmin(1,2);
cout<<endl;

std:: cout<< fmax(1,2);
}


void elseif(int a)
{

  int age = a;  //20

  if(age>18){

    cout<<"adult";

  }

  else if(age<18){

    cout<<"Teen";
  }

  else{
    cout<<"Not a Human";
  }

}


void scase()
{
int day = 2;

switch(day){

  case 1:
  cout<<"Day 1 ";
  break;

  case 2:
  cout<<"Day 2";
  break;

  case 3:
  cout<<"Day 3";
  break;

  default:
  cout<<"Default";

}

}


void loops(){

  for(int i =0; i<10; i++){
    cout<<i;
  }
  cout<<endl;


  int i = 0;

  while(i<5){
    cout<<i;
    i++;
  }

cout<<endl;

i = 0;

do{

  cout<<i;
  i++;

}
while(i<5);
}



void arrays()
{
string cars[4];
cars[0] = "BMW";
cars[1] = "Ford";

int cars_1[2] = {1,2};

cout<<cars[1]<<endl;

cout<<cars_1[1];

}

void references(){

  string food = "Pizza";
  string &meal = food;

  cout<<meal<<endl;
  cout<<food;
  cout<<endl;
  cout<<&meal; //memory address of food
}

void pointers(){

  string food = "Pizza";  // A food variable of type string
  string* ptr = &food;    // A pointer variable, with the name ptr, that stores the address of food

// Output the value of food (Pizza)
  cout << food << "\n";

// Output the memory address of food (0x6dfed4)
  cout << &food << "\n";

// Output the memory address of food with the pointer (0x6dfed4)
  cout << ptr << "\n";

// Dereference: Output the value of food with the pointer (Pizza)
cout << *ptr << "\n";


*ptr = "hamburger";

cout<<*ptr;
cout<<food;

}


void  functions(string fname){

// Note: If a user-defined function, such as myFunction() is declared after the main() function, an error will occur. It is because C++ works from top to bottom; which means that if the function is not declared above main(), the program is unaware of it.

cout<<"fname is "<<fname;


}
//default parameter value
void functions1(string name = "kannav"){
  cout<<name;
}

// pass by reference. This can be useful when you need to change the value of the arguments:



// void swapNums(int &x, int &y) {
//   int z = x;
//   x = y;
//   y = z;
// }

// int main() {
//   int firstNum = 10;
//   int secondNum = 20;

//   cout << "Before swap: " << "\n";
//   cout << firstNum << secondNum << "\n";

//   // Call the function, which will change the values of firstNum and secondNum
//   swapNums(firstNum, secondNum);

//   cout << "After swap: " << "\n";
//   cout << firstNum << secondNum << "\n";

//   return 0;
// }

#include<string>

class Car{

  public:
    string brand;
    string model;
    int year;

    void getter(){
      brand = "BMMW";
      // return brand;
    }
};


class Outsideclassmethod_classname{
  public:
    int x;
    void out();

};

void Outsideclassmethod_classname::out(){
  cout<<"I was declared outside the class";
}


class Car_2 {
  public:
    int speed(int maxSpeed);
};

int Car_2::speed(int maxSpeed) {
  return maxSpeed;
}


class Construct_ex{
  public:
    string name;
    int salary;

    Construct_ex(string x, int y);

};

Construct_ex::Construct_ex(string x,int y){
  name = x;
  salary = y;
  cout<<name;
}



class encap{

  private :
    int salary;

  public :

    void set_salary(int s ){

      salary = s;
    }

    int get_salary(){
      // cout<<endl;
      return salary;
    }
};

