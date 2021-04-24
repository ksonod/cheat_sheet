package cheatSheet;

public class Main {

	/* In Java applications, the main() method should always be created.
	   All other methods are used from the main() method. The name of a 
	   class should be the same as the program file name.
	*/ 
	public static void main(String[] args) {
		
		/* 
		  **System** is a class from the core library provided by Java.
		  **out** is an object.
		  **println()** is a method
		*/
		System.out.println("This is a java cheatsheet.");
		
		/** Data types **/
		// Static typing: The type of a variable is checked at compile time. 
		 
		boolean bool = true; //  boolean
		char c = 'a'; // a single character enclosed in single quotes.
		String s = "strings"; // Multiple characters enclosed in double quotes.
		int integer1 = 3; // integer
		int integer2 = integer1 + 8; // integer
		double number = 1.2; // double
		
		
		/** ---Class Example 1 **/
		// Constructor has parameters. Methods have no parameters.
		System.out.println("\n--ClassExample1: Summation of 2 Numbers--");
		
		// Creating a new instance of a class
		ClassExample1 summation = new ClassExample1(integer1, integer2);
		System.out.println("Memory address: " + summation);
		
		// dot "." notation is used to access variables and method
	    System.out.println("Values received in this constructor: " + summation.int1 + " and " + summation.int2);
		System.out.println("Summed number = " + summation.sum()); // summation
		
		
		/** ---Class Example 2 **/
		// almost the same as Example 1, but method parameters are used in a different way.
		System.out.println("\n--ClassExample2: Multiplication of 2 Numbers--");
		
		// creating a new instance of a class
		ClassExample2 multiplication = new ClassExample2();
		System.out.println("prod: " + multiplication.prod(integer1, integer2)); // product
		
		
		/** ---Class Example 3 **/
		// Basic usage of a class
		System.out.println("\n--ClassExample3: Basic usage of a class--");
		
		// creating a new instance of a class
		ClassExample3 car1 = new ClassExample3("Toyota");
		car1.printCurrentSpeed(); // 0
		car1.accelerate(); 
		car1.printCurrentSpeed(); // 10
		
		/** ---Class Example 4 **/
		// Method overloading allows us to have multiple methods having the same name, but with different
		// parameters.
		System.out.println("\n--ClassExample4: Overloading--");
		ClassExample4 math1 = new ClassExample4() ;
		System.out.println("------");
		math1.simpleMath(2, 5);
		System.out.println("------");
		math1.simpleMath(2, 5, "Multiplication"); // same method name, but it has an additional string parameter.
		System.out.println("------");
		
		/** --Class Example 5 **/
		// Handling arrays and ArrayLists.
		ClassExample5 arrayTest = new ClassExample5();
		arrayTest.arrayListTest();
		
		/** --Class Example 6 **/
		// String methods
		ClassExample6 stringTest = new ClassExample6();
		stringTest.testStrings();
		
		/** --Class Example 7 **/
		// - Private and Public
		// - Accessor method (getter)
		ClassExample7 privateName = new ClassExample7();
		privateName.setName("Maximilian");
		System.out.println("Using a gettor, we got this: \"" + privateName.getName() + "\".");
		
		System.out.println("--\nNow, we will use a private function to print out compliment.");
		
		// You cannot use addCompliment() here because this is a private method. It is invisible from the current Main class.
		privateName.sayCompliment("Kristina"); 
		
		/** --Class Example 8 **/
		// - Using "this" with methods 
		ClassExample8 thisMethod = new ClassExample8();
		thisMethod.showAddedNumbers(6,11);
		
		
		
		/** --Class Example 9 **/
		// - Static methods and variables.
		// It should be noted that main() method is also static. When running a Java program, 
		// the main method of a class, ClassName.main(), is called
		System.out.println("\n--ClassExample9: Static variables --");		
		
		// Static methods and variables belong to an entire class, not a particular object of the class.
		// In the next line, the static method "random()," which belongs to Math class, is used without creating a Math object.
		double randomNumber = Math.random();
		
		// See ClassExample9 class. If numCats is not static, you will always see that the total number of cats is 1.
		// Because numCats is static now, you will see that the total number increases. This behavior explains the meaning that
		// static variables do not belong to a specific object of the class.
		ClassExample9 gatheringCat1 = new ClassExample9("Kot");
		ClassExample9 gatheringCat2 = new ClassExample9("Mur"); 
		ClassExample9 gatheringCat3 = new ClassExample9("Pomes"); 
		
		System.out.println("---");
		gatheringCat1.setWeight(5.5); 
		gatheringCat2.setWeight(7.2); 
		
		System.out.println("---");
		// The following line is possible because checkNumCats() is a static method. If you change it to non-static, 
		// you will get an error.
		ClassExample9.checkNumCats(); 
				
		
		/** --Class Example 10 **/
		// - Inheritance.
		System.out.println("\n--ClassExample10: Inheritance --");		
		ClassExample10A animal1 = new ClassExample10A("Cat", 5.0);
		animal1.printInfo();
		System.out.println("---");
		ClassExample10B animal2 = new ClassExample10B();
		animal2.printInfo();
		
		
		System.out.println("\n---------------------------\nThis is the end of my cheat sheet...");
	}

}
