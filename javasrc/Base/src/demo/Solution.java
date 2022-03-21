package demo;


public class Solution{
	
	public int summation(int n) {
		
		if (n ==1 || n == 0) {
			return n;
		}
		
		else {
			return n%10 + summation(n/10);
		}
		
	}
	
	public static void main(String args[]) {
		
		int x = 14;
		Solution s = new Solution();
		System.out.println(s.summation(x));
		int sum;
		sum = s.summation(x);
		int i = x+1;
		
		while(s.summation(i) != 2*sum) {

			i++;
			
		}
		
		System.out.println("Final Sum " + i);
		
		
	}
}
;




//class Solution {
//    
//    public int summation(int number){
//        int sum = 0;
//        int l;
//        while(number !=0){
//            
//            l = number%10;  //4
//            sum = sum + l;  //4
//            number= number/10;  //1
//        }
//        
//        return sum;
//    }
//    public int solution(int N) { // 14
//        // write your code in Java SE 8
//        int s;
//        s = summation(N);
//        // System.out.println(s);
//        int x;
//        for(int i = N+1; ;i++){
//            
//            if(summation(i)==2*s){
//                x = i ;
//                break;
//            }
//
//        }
//        return x;
//
//    }
//}