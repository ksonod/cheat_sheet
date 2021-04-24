package cheatSheet;

public class ClassExample9 {
	
	// Static variable
	// If you change it to non-static variable, you will see that numCats will be always 1.
	public static int numCats = 0;
	
	// another static variable. We will only consider cats. Hence, this information is stored for the entire class
	// (not for a specific object of the class).
	public static String animalSpecies = "cat";
	
	// These are not static variables because we want to assign specific weight and name to each cat.
	public double weight;
	public String catName;
	
	
	public ClassExample9(String catName) {
		numCats += 1;
		this.catName = catName;
		System.out.println("A cat called " + this.catName + " comes.");
		System.out.println("Now, the total number of cats is " + numCats + ".");
	}
	
	
	public void setWeight(double weight) {
		 // You can use the "this" keyword because you are now in a non-static method.
		this.weight = weight; 
		
		// A non-static method can interact with static variables. In the current example, animalSpecies is a static variable.
		System.out.println("The weight of the " + animalSpecies + " " + this.catName + " is " + this.weight + "kg.");
	}
		
	// Static method
	// - A static method can handle only static variables. In this case, only numCats and animalSpecies can be used here.
	// - Non-static variables cannot be used.
	// - You cannot use the "this" keyword in a static method because the static method is associated with an entire class.
	public static void checkNumCats() {
		System.out.println("Checking number of " + animalSpecies + "s using a static method: " + numCats);
	}
	
	
}
