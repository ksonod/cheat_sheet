package cheatSheet;

/** Getter and setter **/

public class ClassExample7 {
	
	// private. This means other classes cannot access it.
	private String name;

	// Constructor
	public ClassExample7() {
		System.out.println("\n--ClassExample7: Accessor and mutator--");	
	}
	
	// An accessor method, also known as getter, allows us to get the value of the private instance variable.
	public String getName() {
		System.out.println("You are trying to get the private instance variable.");
		return name;
	}
	
	// A mutator method, also known as setter, allows us to reset the value of the private instance variable.
	public void setName(String newName) {
		name = newName;
	}
	
	/***********************************************************/
	
	// Private method that can be used only in this class.
	private String addCompliment(String inputName){
		return inputName + " is beautiful.";
	}
	
	public void sayCompliment(String inputName) {
		// A private method can be used here because it is in the same class.
		String printOutMessage = addCompliment(inputName);
		System.out.println(printOutMessage);
	}
	
}
