#!/opt/conda/bin/python3

# is compares the memory locations of two objects
# usually, two identical strings are efficiently put
# to the same memory location
var1 = "ABC"
var2 = "ABC"
print ("Will compare the memory address of var1:\n" + str(id(var1)) + "\nto the memory address of var2:\n" + str(id(var2)))
if (var1 is var2):
    print("var1 is var2 validated as True")
else:
    print("var1 is var2 validated as False")
    
# a string is read from STDIN, it is stored in a different
# place:
print("Please type ABC and press enter:")
var3 = input()
var3.strip()
print("The memory location of var3: " + str(id(var3)))
print("The contents of variables: var3=" + var3 + ",var2=" + var2 + ",var1=" + var1)
# Thus, the comparison with is must validate False
if (var1 is var3):
    print("var1 is var3 with is validated as True")
else:
    print("var1 is var3 with is validated as False")
# Actual contents of string variables can be compared with ==
# but usually, that is less efficient
if (var1 == var3):
    print("var1 == var3 with is validated as True")
else:
    print("var1 == var3 with is validated as False")

if(var1 == var2):
    print("var1 == var2 with is validated as True")
else:
    print("var1 == var2 with is validated as False")
