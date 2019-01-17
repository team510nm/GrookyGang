"""
@Title of program: menu.py
@Author: Raeed Asif
@Date of creation: 2019-01-12 - 20:44
"""

from sys import exit

def mainMenu(validLessons):
	menu = """
 ~~~~~~~~~~~~~~~~~~~~~~~~~ Main Menu ~~~~~~~~~~~~~~~~~~~~~~~~~ 
Enter the number/roman numeral of the option you wish to choose
1) Get New Lessons
2) Exit
{Lessons}
"""


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

	lessonNumber = 0
	for x in validLessons:
		lessonNumber+=1
		menu = menu.replace("{Lessons}",roman[lessonNumber]+") "+x+"\n{Lessons}")

	menu = menu.replace("{Lessons}","")

	print(menu)

	while True:
		userin = input("Enter your choice: ").upper()
		for index in roman:
			if roman[index] == userin:
				lessonNumber = "Lesson"+str(index)
				if lessonNumber in validLessons:
					return lessonNumber
				else:
					print("That is not a lesson.")
		if userin == "1":
			print("In order to get more lessons [Ctrl] click the following link:\n{LINK}")
		elif userin == "2":
			exit()
		else:
			print("Invalid Input.")
		print("")

	#return userin

def submenu(lesson):
	subLessons = lesson["Lesson Plan"]
	print(" ~~~~~~~~~~~~~~~~~~~~ Sub-Lessons Menu ~~~~~~~~~~~~~~~~~~~~ ")
	print("Enter the number of the sub-lesson you would like to complete")
	print("")
	print("0) Exit")
	print(subLessons)
	print("")
	while True:
		lessonNumber = input("Sub-Lesson Number : ")
		if lessonNumber == "0":
			return lessonNumber
		try:
			lesson[lessonNumber]
			return lessonNumber
		except:
			print("Invalid Input.")
		print("")
