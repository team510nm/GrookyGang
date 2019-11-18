# Developing and you. Volume 1
## How to create a lesson
All lessons must start off with a lesson plan. This plan provides the sub lesson menu.
An example of this is below:
```md
#####Lesson Plan#####
Whatever you want goes in here
This is what the user sees
It is recommended that you put sub lesson numbers and their names here
```
After this lesson plan, you need to add the actual lessons. The layout of a lesson is below. The text inside braces represent text that you would replace.
```md
#####{Lesson Number}#####
###Text###
{Insert Lesson text here}
###Requirements###
{Insert assignment details here}
###Code###
{Enter full java template code here (including classes). Use '//Code here' to specify where user code will be placed}
###Output###
{Enter the expected output of your code here.}
```

An example of this is:
```md
#####2#####
###Text###
This is a lesson about stuff
All the stuff
Yes
###Requirements###
For your first task, make var = 1.
###Code###
class main {
    public static void main(String[] args) {
        //Code Here
        System.out.println(var)
    }
}
###Output###
1
```
It is also very important that you rememeber to leave an empty line at the end of your file (Otherwise your last output section will not function correctly)
## How to add your lesson to the menu
To add your lesson to the menu, name it Lesson{Number}.txt, then put it in the lesson folder.
Then navigate to the reference file, and at the very bottom, add your lesson's file name to the list.