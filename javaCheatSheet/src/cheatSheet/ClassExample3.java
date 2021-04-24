package cheatSheet;

// Reference: https://javatutorial.net/java-objects-and-classes-tutorial

//"public" means that other classes can access this method
public class ClassExample3 {
	
	// state of an object
	int currentSpeed = 0;
	String name;
	
	
	// Constructor 
	/* 
	   - A constructor is used to create instances of the class. 
	   - This has the same name as the class.
	 */
	public ClassExample3(String name){
		this.name = name;  
		// Usage of "this": https://www.w3schools.com/java/ref_keyword_this.asp
	}
	
	
	// method 1
	public void accelerate() {
		currentSpeed += 10; // add 10 to the currentSpeed.
		System.out.println("Accelerated");
	}
	
	public void park() {
		currentSpeed = 0;
	}
	
	public void printCurrentSpeed() {
		System.out.println("Current speed:" + currentSpeed + " km/h");
	}
	
	
}
