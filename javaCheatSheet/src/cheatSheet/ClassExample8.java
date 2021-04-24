package cheatSheet;

public class ClassExample8 {
	
	// constructor
	public ClassExample8() {
		System.out.println("\n--ClassExample8: Using \"this\" with methods --");			
	}
	
	public int addNumbers(int int1, int int2) {
		return int1 + int2;
	}
	
	public void showAddedNumbers(int int1, int int2) {
		int summedNum = this.addNumbers(int1, int2); // "this" is used instead of creating a new object.
		System.out.println("Summation" + int1 + " + " + int2 + " = " + summedNum);
	}
	
}
