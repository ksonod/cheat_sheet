package cheatSheet;


// Inheritance
// This is a parent class, also known as superclass or base class.
public class ClassExample10A {
	
	public String animalSpecies;
	public double averageWeight;
	
	public ClassExample10A(String animalSpecies, double averageWeight){
		this.animalSpecies = animalSpecies;
		this.averageWeight = averageWeight;
		System.out.println("This is a constructor of a parent class.");
	}
	
	public void printInfo() {
		System.out.println("Animal species: " + animalSpecies + ". Average weight: " + averageWeight + " kg.");
	}

	
	
	
}
