// Java code to Segregate 0s and 1s in an array 
class GFG { 
	
	// function to segregate 0s and 1s 
	static void segregate0and1(int arr[], int n) 
	{ 
        int left = 0;
        int right = n-1;
        while(left < right){
            while(arr[left] == 0 && left < right){
                left++;
            }
            while(arr[right] == 1 && left < right){
                right--;
            }
            if(left < right){
                arr[left] = 0;
                arr[right] = 1;
                left++;
                right--;
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