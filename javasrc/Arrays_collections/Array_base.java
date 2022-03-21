package Arrays_collections;


class Array1 {

	public static void base() {
		
		int array[] = new int[2];

		array[0] = 1;
		array[1] = 2;

		for(int i =0; i< array.length; i++){
		System.out.println(array[i]);
		}
	
	}

}


class Array2{
	
	public static void base() {
		
		int a[] = {1,2,3};
		
		for(int i: a) {
			System.out.println(i);
		}
		
	}
}

class FindMin{
	
	public static int min(int arr[]) {
		
		int min = arr[0];
		
		for(int element: arr) {
			
			if(min > element) {
				min = element;
				
			}
			
		}
		return min;
		
		
	}
}

class Return_array{
	
	public static int[] return_a() {
		
		return new int[] {111,23,24};
	}
	
}


class Copy_array{
	

	public static void copy(char[] copyfrom, int s, char[] copyto, int s1, int l) {
		// TODO Auto-generated method stub
		System.arraycopy(copyfrom, s, copyto, s, l);
        System.out.println(String.valueOf(copyto));  

		
	}
}

public class Array_base{
	
	public static void main(String[] args) {
			
		Array1.base();
		Array2.base();
		int sample_arr[] = {11,2,3,4};
		int minimum_val = FindMin.min(sample_arr);
		System.out.println(minimum_val);
		
		int arr_returned[] = Return_array.return_a();
		for(int i: arr_returned)
		{
		System.out.println(i);
		}
		char[] Copyfrom = {'k','a','n','n','a','v'};
		char[] Copyto = new char[4];
		Copy_array.copy(Copyfrom,0,Copyto,0,4);
		
		
	}
}