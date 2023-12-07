"""
Create a Python file named lab_8-7.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using the nested list rows from the "Nested Data" slide, write a function that prints each person's name 
BONUS: Make each name be possessive. Remember,
 if a name ends in s, only add an apostrophe. If the name does not end in s, add, 's.

"""
rows = [["bob" , "sam", "jack",], ["kim", "naz"], ["jacob", "alex"]]
for row in rows:
    for name in row:
        namer = name[::-1]
        if namer[0] == "s":
            print (name,"s")
        else:
            print (name,"'s")
