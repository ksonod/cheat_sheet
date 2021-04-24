package cheatSheet;

/** String method **/

public class ClassExample6 {

	String s1 = "Hello";
	String s2 = " World!";
	String s3 = "hello";
	// Constructor
	public ClassExample6() {
		System.out.println("\n--ClassExample6: String method--");
		
	}
	
	public void testStrings(){
		
		// When comparing objects, use equals(). You cannot use the primitive equality operator ==.
		System.out.println("Hello and hello are the same (case-sensitive): " + s1.equals(s3)); 
		System.out.println("Hello and hello are the same (not case-sensitive): " + s1.equalsIgnoreCase(s3)); 
		System.out.println("Concat (Hello + World): " + s1.concat(s2));
		System.out.println("Get an index of o in Hello: " + s1.indexOf("o"));
		System.out.println("Get a character at the index 2 of Hello: " + s1.charAt(2));
	}
	
}
