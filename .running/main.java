
class DcMotor {
	public static void setPower(double power) {
		System.out.println(power);
	};
};

class main {
	/*
Hello. Welcome to the Code Editor.
This is where you will write your java code.

To save, press [Ctrl+O] then [Enter]
To exit, press [Ctrl+X]
*/

/*
Your requirements for this assignment are:
For your first task, create a method that squares a number then returns the squared number.
For your second task, create a FTC main method (called 'runOpMode') that runs the method from the first task, inputting the number 5.
For you third task, create a DcMotor object in the main method and set its power to the output of the previous task.
*/

/*
Remember to add a ; at the end of every line.
Start coding after this comment ends.
*/
public static int s(int args) {
return args*args;
}

public static void runOpMode() {
DcMotor m = new DcMotor();
m.setPower(s(5));
}


	public static void main(String[] args) {
	    runOpMode();
	}
}




