'''
@Title of program: Robotics Java Tutorial
@Author: Chinmay Patil
@Date of last edit: <2019-01-05 21:23:40>
@Amount of saves: <24>
'''
from reference import *
from parse import *
from menu import *
from os import popen,system

# Template to use in the reference file
##req##requirementsDone = True ## Uncomments after requirements file finishes completly

if not requirementsDone:
	from requirements import reqComplete # run requirements file

if requirementsDone or reqComplete:
	print("Actual Code here")

	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	### MENU HERE (Or something) ###
	mainMenu(validLessons)
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

	choice = "Lesson1"


	lesson = parseLesson(choice)

	### SUB LESSON MENU HERE ###
	ln = "1" # lesson number

	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("You are doing lesson {}".format(ln))

	print(lesson[ln]["Text"])

	input("Press [Enter] to continue onto the testing portion.")


	### // TESTING PORTION // ###

	while True:

		assignment = lesson[ln]["Requirements"]

		beforeCode = preCode
		beforeCode += "\n\n/*\nYour requirements for this assignment are:{}*/\n\n".format(assignment)
		beforeCode += reminder

		tempFile = open("TempEditor.java","w")
		tempFile.write(beforeCode)
		tempFile.close()


		# User Input Here
		system("nano TempEditor.java -\$wS -m -l")
		tempFile = open("TempEditor.java")
		userCode = tempFile.read()
		tempFile.close()
		system("rm TempEditor.java")

		code = lesson[ln]["Code"]

		code = code.replace("// Code Here", userCode)


		openFile = open(".running/main.java","w")
		openFile.write(code)
		openFile.close()

		print("")
		building = popen("cd .running && javac main.java && echo 'complete'").read()

		#print(building)

		if not building == "complete\n":
			print("An error arose during the compiling of your program (Visible above)")
			#print(building)
			validYes = ["y", ""]
			redo = input("Would you like to redo this test? (Y/n)").lower()
			if not (redo in validYes):
				break
		else:
			out = popen("cd .running && java main").read()
			expectedOut = lesson[ln]["Output"][1:]
			if expectedOut == out:
				print("You passed the test.")
				break
			else:
				print("You failed the test, the following was the output of your code:")
				print(out)
				print("\n\n")
				validYes = ["y",""]
				redo = input("Would you like to redo this test? (Y/n)").lower()
				if not (redo in validYes):
					break
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")