package cheatSheet;

//Example 1: Summation

// "public" means that other classes can access this method
public class ClassExample1 {
	
	// state of an object
	int int1;
	int int2;

	// Constructor
	/* - A constructor is used to create instances of the class. 
	   - This has the same name as the class.
	 */
	public ClassExample1(int int1, int int2) {
		System.out.println("Constructor of ClassExample1");
		this.int1 = int1; // "this" keyword allows us to access the instance variable.
		this.int2 = int2; 
	}	
	
	// Method
	public int sum()
	{
		return int1 + int2;
	}

}