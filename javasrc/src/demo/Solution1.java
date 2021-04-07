package demo;

import java.util.*;

public class Solution1 {
    int solution(int X, int Y, int[] A) {
        int N = A.length;
        int result = -1;
        int nX = 0;
        int nY = 0;
        for (int i = 0; i < N; i++) {
        	
            if (A[i] == X)
                nX += 1;
            if (A[i] == Y)
                nY += 1;
            if (nX == nY)
                result = i;
        }
        return result;
    }
    
    public static void main(String args[]) {
    	
    	Solution1 s1 = new Solution1();
    	int[] intArray = {6,42,11,7,1,42};
    	System.out.println(s1.solution(7,42,intArray));
    	
    }
}