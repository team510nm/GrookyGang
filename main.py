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
'''
Template to use in the reference file
requirementsDone = True ## Uncomments after requirements file finishes completly
'''

# If the requirements are not done
if not requirementsDone:
	from requirements import reqComplete # run requirements file and try to get if they had the requirements

    
# If requirements have been done
if requirementsDone or reqComplete:

	while True:
		system("clear")

		### Main menu ###
		choice = mainMenu(validLessons)

		# Example of an output of mainMenu:
		# choice = "Lesson1"


		# Change lesson
		lesson = parseLesson(choice)


		while True:

			### SUB LESSON MENU###
			system("clear")
			ln = submenu(lesson)
			if ln == "0": # If they select to exit, break out of while loop back to main menu.
				break

			system("clear")
			print("You are doing {}, sub-lesson {}".format(choice,ln))

			print(lesson[ln]["Text"]) # Print lesson

			input("Press [Enter] to continue onto the testing portion.") # Wait for enter


			### // TESTING PORTION // ###

			while True:
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

				assignment = lesson[ln]["Requirements"] # Get assignment details

				# Add assignment, and reminders into the code editor (in a comment)
				beforeCode = preCode
				beforeCode += "\n\n/*\nYour requirements for this assignment are:{}*/\n\n".format(assignment)
				beforeCode += reminder

				tempFile = open("TempEditor.java","w")
				tempFile.write(beforeCode)
				tempFile.close()


				system("nano TempEditor.java -\$wS -m -l") # user inputs code in here

				# Read user's code then remove the editor file
				tempFile = open("TempEditor.java")
				userCode = tempFile.read()
				tempFile.close()
				system("rm TempEditor.java")

				code = lesson[ln]["Code"] # Get code template

				code = code.replace("// Code Here", userCode) # Input user code into the code template


				openFile = open(".running/main.java","w") # write code into the running file
				openFile.write(code)
				openFile.close()

				print("") # Build the file, if success, print out complete so we can tell it finished
				building = popen("cd .running && javac main.java && echo 'complete'").read()

				validYes = ["y", ""]

				if not building == "complete\n": # If the building was not completed tell user
					print("")
					print("An error arose during the compiling of your program (Visible above)")
					# Ask user weither or not to exit to lesson menu
					redo = input("Would you like to redo this test? (Y/n) : ").lower()
					if not (redo in validYes):
						break # break out of testing loop to sub-lesson menu loop
				else:
					out = popen("cd .running && java main").read() # Run the file
					expectedOut = lesson[ln]["Output"][1:] # Get the expected output
					if expectedOut == out: # If the expected output is the same as the output
						print("You passed the test.") # Tell user they passed, then exit the testing loop
						break
					else:
						print("You failed the test, the following was the output of your code:")
						print(out)
						# Ask user weither or not to exit to lesson menu
						redo = input("Would you like to redo this test? (Y/n) : ").lower()
						if not (redo in validYes):
							break # break out of testing loop to sub-lesson menu loop
				print("\n")
			print("")
			input("Press [Enter] to return to menu.") # Confirmation to exit back to the sub-lesson menu