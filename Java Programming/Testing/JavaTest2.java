class gamepad {
	public boolean x = false;
	public boolean a = false;
	public boolean b = false;
	public boolean y = true;
	public boolean start = false;
	public boolean select = false;
};

class Motor {
	public static void setPower(int power) {
		System.out.println(power);
	};
};

class main {
	public static void main(String[] args) {
		gamepad gamepad1 = new gamepad();
		Motor left_back = new Motor();
		// Code Here
		
	}
}