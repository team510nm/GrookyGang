'''
@Title of program: Robotics Java Tutorial
@Author: Chinmay Patil
@Date of last edit: <2019-01-05 21:23:40>
@Amount of saves: <24>
'''
from reference import *
from parse import *
from os import popen

# Template to use in the reference file
##req##requirementsDone = True ## Uncomments after requirements file finishes completly

if requirementsDone == False:
	from requirements import reqComplete # run requirements file

if requirementsDone or reqComplete:
	print("Actual Code here")


	### MENU HERE (Or something) ###
	choice = "Lesson1"


	lesson = parseLesson(choice)

	### SUB LESSON MENU HERE ###
	ln = "1" # lesson number

	print("You are doing lesson {}".format(ln))

	print(lesson[ln]["Text"])

	input("Press [Enter] to continue onto the testing portion.")


	### // TESTING PORTION // ###

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
	building = popen("cd .running && javac main.java")

	if popen == "":
		print("An error arose during the compiling of your program:")
		print(building)
	else:
		pass