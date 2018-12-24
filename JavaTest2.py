"""
@Title of program: JavaTest2.py
@Author: Chinmay Patil
@Date of creation: 2018-12-23 - 21:35
"""

from os import popen, system
'''
out = popen("echo \"Test\"").read()

print(out)
'''

openFile = open("Lesson1.txt")
data = openFile.read().split("#####")
openFile.close()
while '' in data:
	data.remove('')
lesson = {}
for x in range(0,len(data),2):
	lesson[data[x]] = data[x+1]

## Each seperate sub lesson ##
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


print(lesson["1"]["Text"])

usercode = ""

while True:
	currentLine = input("Enter Code, type 'exit()' to quit:\n")
	if currentLine == "exit()":
		break
	else:
		if currentLine[-1:] != ";":
			print("Invalid, you need a ';' at the end of every line")
		else:
			usercode += currentLine

	print("")

code = lesson["1"]["Code"]

code = code.replace("// Code Here", usercode)


openFile = open("JavaTest.java","w")
openFile.write(code)
openFile.close()

print("")
print("Building Java Code")
system("javac JavaTest.java")


print("\nExecuting Java program\n~~~~~~~~~~~~~~~\n")
out = popen("java JavaTest").read()
system("rm JavaTest.class")

print(out)

expectedOut = lesson["1"]["Output"]
if expectedOut == out:
	print("Hey, you succeded")
else:
	print("You failed")
