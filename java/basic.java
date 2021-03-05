class Simple
{
public static void main(String args[])
{
  System.out.print("Hello World");
}

}

class Narrow_wide
{
public static void main(String args[])
{
int a = 10;
float f = a;
float x =  10.4f;
int xint = (int)x;
System.out.println(a);
System.out.println(f);
System.out.println(xint);

}

}

class Ifelse
{
  public static void main(String args[])
  {
    int a = 18;
    if(a>18)
    {
    System.out.println("a>18");

    }
    else{

      System.out.println("a<18");
    }

  }
}

class Leapyear
{
  public static void main(String args[])
  {
    int year = 2020;

    if(((year%4 == 0) && (year%100 != 0)) || (year%400 == 0) )
    {
      System.out.println(true);
    }
  }
}

// if(){} else if(){} else if() {} else {}
// if no break after a case, it will execute all the statements after the match is found including default
class Scase{
  public static void main(String args[])
  {
int n = 2;
switch(n){

case 1: System.out.println("1");
break;

case 2: System.out.println("2");
break;

case 3: System.out.println("3");
break;

default: System.out.println("Not Found");

}

  }
}

class Loops{
public static void main(String[] args)
{

for(int i = 0; i <10 ; i++)
{

System.out.println(i);

}
}

}





class PyramidExample {  
public static void main(String[] args) {  
for(int i=1;i<=5;i++){  
for(int j=1;j<=i;j++){  
        System.out.print("* ");  
}  
System.out.println();//new line  
}  
}  
}  



class Main {  
public static void main(String[] args) {  
    int arr[] = {1,2,3,4};
    
    for(int i: arr){
        
        System.out.println(i);
    }
    
    
}
}



//A Java program to demonstrate the use of labeled for loop  
class LabeledForExample {  
public static void main(String[] args) {  
    //Using Label for outer and for loop  
    aa:  
        for(int i=1;i<=3;i++){  
            bb:  
                for(int j=1;j<=3;j++){  
                    if(i==2&&j==2){  
                        break aa;  
                    }  
                    System.out.println(i+" "+j);  
                }  
        }  
}  
}

