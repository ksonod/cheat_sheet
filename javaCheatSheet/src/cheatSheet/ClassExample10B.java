package cheatSheet;


// Inheritance
// This is a child class, also known as subclass or derived class.
public class ClassExample10B extends ClassExample10A{
	
	// The super() method acts like the parent constructor inside the child class constructor.
	ClassExample10B(){
		super("Dog", 7.2);  // see ClassExample10A		
		System.out.println("We are now in a child class."); 
	}
	
	// Method overriding
	// - By overriding parent class methods in a child class, we can prepare a single method with slightly different meanings for different classes.
	// - The method name, return tyoe, and number and type of parameters need to be the same.
	@Override
	public void printInfo(){
		System.out.println("Here, we are overriding a parent class method in a child class.");
		System.out.println(animalSpecies + "'s average weight is " + averageWeight + " kg.");
		
		System.out.println("Next, we call the parent class method using *super* followed by the dot operator (.)");
		super.printInfo();
	}
	
}
