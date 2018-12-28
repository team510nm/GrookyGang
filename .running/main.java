
class gamepad {
	public boolean x = false;
	public boolean a = false;
	public boolean b = false;
	public boolean y = true;
	public boolean start = false;
	public boolean select = false;
};

class Motor {
	public static void setPower(double power) {
		System.out.println(power);
	};
};

class main {
	public static void main(String[] args) {
		gamepad gamepad1 = new gamepad();
		Motor left_back = new Motor();
		/*
Hello. Welcome to the Code Editor.
This is where you will write your java code.

To save, press [Ctrl+O] then [Enter]
To exit, press [Ctrl+X]
*/

/*
Your requirements for this assignment are:
For your task, you are to test if the 'y' button on gamepad 1 is pressed
if it is pressed, then set the motor 'left_back' to run at half speed (1 is full speed & 0 is off)
*/

/*
Remember to add a ; at the end of every line.
Start coding after this comment ends.
*/
if (gamepad1.y) {left_back.setPower(0.5);}

		
	}
}




