// Java code to Segregate 0s and 1s in an array 
class GFG { 
	
	// function to segregate 0s and 1s 
	static void segregate0and1(int arr[], int n) 
	{ 
        int right = 0;
        int left = n-1;
        while(left > right){
            if(arr[right] == 0 && left > right){
                right++;
            }
            if(arr[left] == 1 && left > right){
                left--;
            }
            if(left > right){
                arr[right] = 0;
                arr[left] = 1;
                right++;
                left--;
            }
        }
	} 
	
	// function to print segregated array 
	static void print(int arr[], int n) 
	{ 
		System.out.print("Array after segregation is "); 
		for (int i = 0; i < n; i++) 
			System.out.print(arr[i] + " ");	 
	} 
	
	// driver function 
	public static void main(String[] args) 
	{ 
		int arr[] = new int[]{ 0, 1, 0, 1, 1, 1 }; 
		int n = arr.length; 

		segregate0and1(arr, n); 
		print(arr, n); 
		
	} 
}