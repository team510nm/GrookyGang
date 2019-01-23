"""
@Title of program: menu.py
@Author: Raeed Asif
@Date of creation: 2019-01-12 - 20:44
"""

from sys import exit

# Main menu, includes lessons and where to get more lessons
def mainMenu(validLessons):
	menu = """

Welcome to the Robotics Java Tutorial
Made by Chinmay Patil and Raeed Asif


 ~~~~~~~~~~~~~~~~~~~~~~~~~ Main Menu ~~~~~~~~~~~~~~~~~~~~~~~~~ 
Enter the number/roman numeral of the option you wish to choose
1) Get New Lessons
2) Exit
{Lessons}
"""

	# Roman dictionary, changing arabic numbers to roman
	roman = {
		1:"I",
		2:"II",
		3:"III",
		4:"IV",
		5:"V",
		6:"VI",
		7:"VII",
		8:"VIII",
		9:"IX",
		10:"X"
	}

	lessonNumber = 0 # set current lesson to 0
	for x in validLessons: # For every lesson that is agnoledged in the reference file
		# Add lesson txt to menu, and add 1 to lesson (so we can convert lesson number into a roman numeral)
		lessonNumber+=1
		menu = menu.replace("{Lessons}",roman[lessonNumber]+") "+x+"\n{Lessons}") 

	menu = menu.replace("{Lessons}","") # Remove the last Lesson placeholder

	print(menu)

	while True:
		userin = input("Enter your choice: ").upper() # Get user choice
		for index in roman: # For every arabic number in the dictionary
			if roman[index] == userin: # If the roman numeral is what the user entered
				lessonNumber = "Lesson"+str(index) # Set the lesson output to the lesson number (arabic)
				if lessonNumber in validLessons:
					return lessonNumber # If a valid lesson, output it.
				else:
					print("That is not a lesson.")
		if userin == "1": # If they choose 1, give them a link
			print("In order to get more lessons [Ctrl] click the following link:\n{LINK}")
		elif userin == "2": # IF they choose 2, exit the program
			exit()
		else:
			print("Invalid Input.") # If input is not an option, tell them.
		print("")


# Menu to select which sub-lesson to do.
def submenu(lesson):
	subLessons = lesson["Lesson Plan"]
	print(" ~~~~~~~~~~~~~~~~~~~~ Sub-Lessons Menu ~~~~~~~~~~~~~~~~~~~~ ")
	print("Enter the number of the sub-lesson you would like to complete")
	print("")
	print("0) Exit")
	print(subLessons)
	print("")
	while True:
		lessonNumber = input("Sub-Lesson Number : ") # Get user choice
		if lessonNumber == "0": # If it's 0, then return it so that main file can deal with it
			return lessonNumber
		try:
			lesson[lessonNumber] # Try to see if it is a valid lesson
			return lessonNumber # If so, return the lesson number
		except:
			print("Invalid Input.") # If not, tell user.
		print("")
