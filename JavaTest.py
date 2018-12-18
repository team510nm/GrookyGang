"""
@Title of program: JavaTest
@Author: Chinmay Patil
@Date of creation: 2018-12-17 - 19:57
"""
from os import system

final = []

final.append("""
import java.util.*;

class JavaTest {
""")



code = ""

while True:
	currentLine = input("Enter Method Code, type 'exit()' to quit:\n")
	if currentLine == "exit()":
		break
	else:
		code += currentLine

	print("")


final.append(code)

final.append("""

    public static void main(String[] args) {
    
    
    
""")

code = ""

while True:
	currentLine = input("Enter Code, type 'exit()' to quit:\n")
	if currentLine == "exit()":
		break
	else:
		if currentLine[-1:] != ";":
			print("Invalid, you need a ';' at the end of every line")
		else:
			code += currentLine

	print("")

final.append(code)

final.append("""



    }
}
""")


openFile = open("JavaTest.java","w")
openFile.write(''.join(final))
openFile.close()

print("")
print("Building Java Code")
system("rm JavaTest.class")
system("javac JavaTest.java")


print("\nExecuting Java program\n~~~~~~~~~~~~~~~\n")
system("java JavaTest")
