"""
@Title of program: menu.py
@Author: Chinmay Patil
@Date of creation: 2019-01-12 - 20:44
"""

def mainMenu(validLessons):
	menu = """
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

	input("Enter")