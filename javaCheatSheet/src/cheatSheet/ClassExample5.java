package cheatSheet;

import java.util.Arrays; // This package is needed for printing out arrays.
import java.util.ArrayList; // This package is needed for using the ArrayList.


public class ClassExample5 {

	/** Array and ArrayList **/
	// - An array stores a list of elements of the SAME DATATYPE. The size is fixed and cannot be modified.
	// - An ArrayList is used to represent a dynamic list. The size can be modified by adding or removing elements. Moreover, it is possible
	//   for a single ArrayList to possess different data types (e.g., the first element is int, the second one is String). However, it is 
	//   more preferable to stick to the same data type.
	
	int[] array1 = {1,10,0,20}; // creating an array explicitly
	int[] array2 = new int[4]; // empty array

	int[][] twoDArray1 = {{1,2,3},
    					  {4,5,6}}; // 2D array
	int[][] twoDArray2 = new int[2][3]; // Empty 2D array
	

	// Constructor
	public ClassExample5(){
		System.out.println("\n--ClassExample5: Array and ArrayList--");
	}
	
	// method
	public void arrayListTest() {
		
		/** Array **/
		System.out.println("\n-Handling an array-");
		
		// Arrays.toString() is needed to visualize the elements If you do not use it, you will only see memory address.
		System.out.println("Empty array: " + Arrays.toString(array2)); 
		
		array2[0] = 2; // the number 2 is stored in the first element
		System.out.println("Partially filled array: " + Arrays.toString(array2));
		System.out.println("Length: " + array2.length);
		
		/** ArrayList **/
		ArrayList<String> arrayList1 = new ArrayList<String>(); // ArrayList
		
		// Adding and removing elements to an ArrayList.
		System.out.println("\n-Handling an ArrayList-");
		arrayList1.add("John");
		arrayList1.add("Max");
		arrayList1.add("Kai");
		arrayList1.add("Anna");
		arrayList1.add("Kristina");
		System.out.println("Initial ArrayList: " + arrayList1 + " (size=" + arrayList1.size() + ")");
		arrayList1.remove(0); // removing based on an index.
		System.out.println("first element is removed: " + arrayList1 + " (size=" + arrayList1.size() + ")");
		arrayList1.remove("Kai"); // removing based on a specific value.
		System.out.println("Kai is removed: " + arrayList1 + " (size=" + arrayList1.size() + ")");
		
		arrayList1.add(2,"Kate"); // An index is specified.
		System.out.println("Kate is added to index 2: " + arrayList1 + " (size=" + arrayList1.size() + ")");
		
		arrayList1.set(0, "Sophia"); // An index is specified.
		System.out.println("Max is replaced by Sophia: " + arrayList1 + " (size=" + arrayList1.size() + ")");		
		
		System.out.println("An index of Kristina is " + arrayList1.indexOf("Kristina"));
		
		// 2D array
		System.out.println("\n-Handling a 2D Array-");
		System.out.println("Number of rows: " + twoDArray1.length);
		System.out.println("Number of columns: " + twoDArray1[0].length);
	}
}
