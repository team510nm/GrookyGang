"""
@Title of program: requirements
@Author: Chinmay Patil
@Date of creation: 2018-12-29 - 19:41

Test for if the user has the correct requirements to run the program
"""
from os import popen,system
from reference import *

if requirementsDone != True: # If they havent already done this

	reqComplete = False # Used when testing requirements in main file

	# Java test text
	testText = """
	class main {
		public static void main(String[] args) {
			System.out.println("Test");
		}
	}
	""" 

	# Nano test text
	testText2 = """


If this text is displayed, go to the start of the file.
At the start of the file, type the following without quotes: 'nano'
	"""




	testFile = open(testFile,"w")
	testFile.write(testText)
	testFile.close()

	system("cd .running && javac JavaTest.java") # Test for JDK
	systemLog = popen("cd .running && java main").read() # Test for JRE
	remove = popen("cd .running && rm *.class").read() # Test for bash
	system("cd .running && rm JavaTest.java")

	if systemLog != "Test\n": # If test didn't pass
		print("Sorry, you appear to either not be using a Unix device, or be missing the Java JDK")
		print("Please install either bash or the latest openJDK.")
		print("For more instructions, please follow the link below:")
		print("")
		print("{LINK}")

		input("Please press [Enter] to proceed.")

	else:
		# If compiling will work, test for editing files
		testFile = open("NanoTest.txt", "w")
		testFile.write(testText2)
		testFile.close()
		system("nano NanoTest.txt")
		testFile = open("NanoTest.txt", "r")
		text = testFile.read()
		testFile.close()
		system("rm NanoTest.txt")



		if text[:4] == "nano": # if first bit of file says nano
			print("Congratulations, you have passed all checks, you are now able to use the program.")
			print("We respect your time, and as such, you will only be made to do this test once per computer.")
			print("To redo this test, please run the requirements file included.")
			print("Thank you for your time.")
			print("")


			# Change requirements variable from False to True in the reference file
			referenceFile = open("reference.py","r")
			reference = referenceFile.read()
			reference = reference.replace("requirementsDone = False","requirementsDone = True")
			referenceFile.close()

			referenceFile = open("reference.py","w")
			referenceFile.write(reference)
			referenceFile.close()

			reqComplete = True # Main file will try to import this variable (when importing file runs)

			input("Please press [Enter] to proceed.")

		else: # If first bit of file says anything else (or nothing)
			print("Sorry, you appear to be having issues with nano, the text editor we use.")
			print("If you are opening this from inside an IDE, then it will also not work.")
			print("Please either install nano, or run this within a proper terminal.")
			print("For more instructions on the installation of nano, follow the link below:")
			print("")
			print("{LINK}")

			input("Please press [Enter] to proceed.")

