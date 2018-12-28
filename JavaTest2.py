"""
@Title of program: JavaTest2.py
@Author: Chinmay Patil
@Date of creation: 2018-12-23 - 21:35
"""


from os import popen, system
'''
out = pOpen("echo \"Test\"").read()

print(out)
'''

preCode = '''/*
Hello. Welcome to the Code Editor.
This is where you will write your java code.

To save, press [Ctrl+O] then [Enter]
To exit, press [Ctrl+X]
*/'''

reminder = """/*
Remember to add a ; at the end of every line.
Start coding after this comment ends.
*/"""

openFile = open("Lesson1.txt")
data = openFile.read().split("#####")
openFile.close()
while '' in data:
	data.remove('')
lesson = {}
for x in range(0,len(data),2):
	lesson[data[x]] = data[x+1]

## Each separate sub lesson ##
for x in range(1,4):
	lesson[str(x)] = lesson[str(x)].split("###")
	while '' in lesson[str(x)]:
		lesson[str(x)].remove('')
	while '\n' in lesson[str(x)]:
		lesson[str(x)].remove('\n')

	cLesson = {}
	for y in range(0, len(lesson[str(x)]), 2):
		cLesson[lesson[str(x)][y]] = lesson[str(x)][y+1]
	lesson[str(x)] = cLesson





for x in range(3,4):

	ln = str(x)

	print("You are doing lesson {}".format(ln))

	print(lesson[ln]["Text"])

	input("Press [Enter] to continue onto the testing portion.")

	'''
	userCode = ""

	while True:
		currentLine = input("Enter Code, type 'exit()' to quit:\n")
		if currentLine == "exit()":
			break
		else:
			if currentLine[-1:] != ";":
				print("Invalid, you need a ';' at the end of every line")
			else:
				userCode += currentLine

		print("")
	'''

	assignment = lesson[ln]["Requirements"]

	beforeCode = preCode
	beforeCode += "\n\n/*\nYour requirements for this assignment are:{}*/\n\n".format(assignment)
	beforeCode += reminder


	tempFile = open("TempEditor.java","w")
	tempFile.write(beforeCode)
	tempFile.close()

	system("nano TempEditor.java")
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
	print("Building Java Code")
	system("cd .running && javac main.java")


	print("\nExecuting Java program\n~~~~~~~~~~~~~~~\n")
	out = popen("cd .running && java main").read()
	system("cd .running && rm *.class")

	print(out)

	print("\n~~~~~~~~~~~~~~~\n")

	expectedOut = lesson[ln]["Output"][1:]
	if expectedOut == out:
		print("Hey, you succeeded")
	else:
		print("You failed")
