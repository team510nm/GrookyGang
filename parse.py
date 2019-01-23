'''
@Title of program: Parses
@Author: Chinmay Patil
@Date of last edit: <2019-01-04 21:34:35>
@Amount of saves: <9>
'''


def parseLesson(lessonname):
	'Change lesson text file into a dictionary'

	openFile = open("lessons/"+lessonname+".txt")

	data = openFile.read().split("#####") # Split along 5 hashes (Sections)
	openFile.close()

	while '' in data:
		data.remove('') # Remove all empty indexes

	lesson = {}

	for x in range(0,len(data),2): # Add info to a dictionary
		lesson[data[x]] = data[x+1]


	## Each separate sub lesson ##
	for x in range(1,4):
		lesson[str(x)] = lesson[str(x)].split("###") # Split parts 1, 2, and 3 along 3 hashes (sub sections)

		while '' in lesson[str(x)]:
			lesson[str(x)].remove('') # Remove all empty indexes

		while '\n' in lesson[str(x)]:
			lesson[str(x)].remove('\n') # Remove all newline indexes

		cLesson = {}

		for y in range(0, len(lesson[str(x)]), 2):
			cLesson[lesson[str(x)][y]] = lesson[str(x)][y+1] # Add each subsection to a dictionary


		lesson[str(x)] = cLesson # Replace old string with dictionary

	return lesson


