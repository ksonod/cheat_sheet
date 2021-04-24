package cheatSheet;

// Example 4

// Overloading allows us to have multiple methods having the same name, but with different
// parameters.
public class ClassExample4 {
	
	// Method 1
	public void simpleMath(int inputInt1, int inputInt2) {
		int summedNum = inputInt1 + inputInt2;
		System.out.println("You did not specify method. Summation will be calculated.");
		System.out.println("Summation: " + inputInt1 + " + " + inputInt2 + " = " + summedNum);
	}
	
	// Method 2
	public void simpleMath(int inputInt1, int inputInt2, String method) {
		System.out.println("You specified a method: " + method);
		System.out.println("Multiplication: " + inputInt1 + " x " + inputInt2 + " = " + inputInt1 * inputInt2);		
	}
	
}
